# Grabs the latest MAC address list files from the IEEE and saves them to vendorLists

import os # needed for file handling
import requests # needed for HTTP requests


DOWNLOADS = [
    ("oui.csv",   "http://standards-oui.ieee.org/oui/oui.csv"),
    ("mam.csv",   "http://standards-oui.ieee.org/oui28/mam.csv"),
    ("oui36.csv", "http://standards-oui.ieee.org/oui36/oui36.csv"),
]

VENDOR_LISTS_DIR = "vendorLists"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}


def download_mac_files():
    """Downloads the three IEEE MAC registry CSV files into vendorLists, overwriting any existing copies."""

    print("Downloading MAC address registry files from IEEE...")
    for filename, url in DOWNLOADS:
        file_path = os.path.join(VENDOR_LISTS_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        print(f"  {filename}...", end=" ")
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("done")
    print("Vendor lists up to date.")


if __name__ == "__main__":
    print("Welcome to the MAC vendor list downloader for the wifi scanner demo.")
    print("This tool will grab the 3 MAC registry lists from the publicly hosted IEEE site and download them to vendorLists.\n")
    download_mac_files()
