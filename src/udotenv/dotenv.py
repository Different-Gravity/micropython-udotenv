import os

def load_dotenv(filename: str = ".env", set_environ: bool = False) -> dict:
    """Loads environment variables from a .env file.

    :param filename: Path to the .env file (default: '.env').
    :param set_environ: If True, injects the variables into os.environ.
    :return: A dictionary containing the loaded key-value pairs.
    """
    env_vars = {}
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                
                # Ignore empty lines and comments
                if not line or line.startswith("#"):
                    continue
                
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove surrounding single or double quotes
                    if (value.startswith('"') and value.endswith('"')) or \
                       (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    
                    env_vars[key] = value
                    
                    # Inject into MicroPython's os.environ if requested and available
                    if set_environ and hasattr(os, "environ"):
                        os.environ[key] = value
                        
    except OSError:
        raise FileNotFoundError(f"Could not open the .env file: {filename}")

    return env_vars