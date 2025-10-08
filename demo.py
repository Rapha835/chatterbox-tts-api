RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'

VERSION = "1.0.0"  # Set your version
WEBUI_BUILD_HASH = "abc123"  # Set your hash

print(
    f"""
{RED}▄██████▄     ▄███████▄    ▄████████ ███▄▄▄▄              ▄█     █▄     ▄████████ ▀█████████▄  ███    █▄   ▄█  {RESET}
{RED}███    ███   ███    ███   ███    ███ ███▀▀▀██▄           ███     ███   ███    ███   ███    ███ ███    ███ ███ {RESET}
{RED}███    ███   ███    ███   ███    █▀  ███   ███           ███     ███   ███    █▀    ███    ███ ███    ███ ███▌{RESET}
{RED}███    ███   ███    ███  ▄███▄▄▄     ███   ███           ███     ███  ▄███▄▄▄      ▄███▄▄▄██▀  ███    ███ ███▌{RESET}
{RED}███    ███ ▀█████████▀  ▀▀███▀▀▀     ███   ███  ██████   ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ███    ███ ███▌{RESET}
{RED}███    ███   ███          ███    █▄  ███   ███           ███     ███   ███    █▄    ███    ██▄ ███    ███ ███ {RESET}
{RED}███    ███   ███          ███    ███ ███   ███           ███ ▄█▄ ███   ███    ███   ███    ███ ███    ███ ███ {RESET}
{RED}▀██████▀   ▄████▀        ██████████  ▀█   █▀             ▀███▀███▀    ██████████ ▄█████████▀  ████████▀  █▀   {RESET}

{YELLOW}Modified version by Prathmesh Hatwar
{f"Commit: {WEBUI_BUILD_HASH}" if WEBUI_BUILD_HASH != "dev-build" else ""}{RESET}
{GREEN}v{VERSION} - building the best AI user interface.{RESET}
{BLUE}https://github.com/open-webui/open-webui{RESET}
"""
)