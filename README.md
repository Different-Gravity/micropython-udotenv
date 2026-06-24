# udotenv

A lightweight, professional, and memory-efficient `dotenv` implementation tailored for MicroPython environments.

In MicroPython, managing sensitive configurations like Wi-Fi credentials, API keys, or environment-specific toggles can be challenging due to limited hardware resources. This module allows you to seamlessly load these configurations from a standard `.env` file. It parses the file line-by-line, strips extra whitespaces, removes surrounding single or double quotes, and safely ignores comments or empty lines.

---

## Function Documentation

### `load_dotenv(filename: str = ".env", set_environ: bool = False) -> dict`

Loads environment variables from a specified configuration file.

*   **Parameters:**
    *   `filename` *(str, optional)*: The path to your environment file. Defaults to `".env"`.
    *   `set_environ` *(bool, optional)*: If set to `True`, the function attempts to inject the parsed variables directly into `os.environ` (if your specific MicroPython port supports it). Defaults to `False`.
*   **Returns:**
    *   `dict`: A dictionary containing all the successfully parsed key-value pairs.
*   **Error Handling:**
    *   If the target file is missing, the function catches the `OSError` and fails silently, returning an empty dictionary. This ensures your code won't crash in production if environment variables are handled through an alternative fallback mechanism.

---

## Usage Examples

### 1. Preparing the `.env` file
Create a `.env` file in the root directory or `lib/` folder of your MicroPython device:

```env
# Wi-Fi Credentials
WIFI_SSID="My_Home_Network"
WIFI_PASS='SuperSecretPassword123'

# API Settings
API_URL=https://api.example.com/v1
DEBUG=True

```

### 2. Loading into a Dictionary (Recommended)

This method isolates your configuration variables, keeping memory footprints predictable and preventing global state pollution.

```python
from udotenv import load_dotenv

# Load configurations into a local dictionary
config = load_dotenv()

# Access your variables safely
wifi_ssid = config.get("WIFI_SSID")
wifi_pass = config.get("WIFI_PASS")

print(f"Connecting to SSID: {wifi_ssid}")

```

### 3. Loading directly into `os.environ`

If your project structure copies standard desktop Python architectures and relies on global environment variables, enable the `set_environ` flag.

```python
import os
from udotenv import load_dotenv

# Load and automatically inject into the system environment
load_dotenv(set_environ=True)

# Access values directly through the built-in os module
wifi_ssid = os.environ.get("WIFI_SSID")

```

