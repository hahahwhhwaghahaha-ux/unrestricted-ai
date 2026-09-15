import urllib.request
import os
import subprocess
import sys

def main():
    # Replace YOUR_USERNAME with your actual GitHub username
    url = "https://github.com/hahahwhhwaghahaha-ux/unrestricted-ai/raw/main/vidoe.mov"
    filename = "vidoe.mov"

    print("Downloading file...")
    try:
        urllib.request.urlretrieve(url, filename)
        print("Download complete. Opening file...")
        
        if sys.platform == 'win32':
            os.startfile(filename)
        elif sys.platform == 'darwin':
            subprocess.call(('open', filename))
        else:
            subprocess.call(('xdg-open', filename))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
