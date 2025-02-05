import requests
import pyperclip
from colorama import Fore, Style

# URL of the raw script file
url = "https://raw.githubusercontent.com/RealestName/Component-Hunter/refs/heads/main/script.txt"

try:
    # Fetch the script content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

    # Copy content to clipboard
    pyperclip.copy(response.text)

    # Print success message in blue
    print(Fore.BLUE + "Script has been copied to clipboard" + Style.RESET_ALL)

except requests.RequestException as e:
    print(Fore.RED + f"Failed to fetch script: {e}" + Style.RESET_ALL)
