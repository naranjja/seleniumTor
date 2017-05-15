# python27-selenium-tor-windows
Python 2.7 Selenium script for using The Onion Router nodes and relays in Windows (tested on Windows 10 64-bit).

## Requirements
* [Python 2.7](https://www.python.org/downloads/)
* [Tor Browser Bundle](https://www.torproject.org/download/download-easy.html.en)

## Instructions
1. Remember path to Tor Browser Bundle installation
2. Run `pip install -r requirements.txt` inside project folder
3. Open `router.py` and modify the path to binary
4. Insert Selenium code within `# do something`
5. Open an instance of Tor Browser manually using `Start Tor Browser.lnk`
5. Run script!

## Custom settings
* The `setup_tor` function contains the profile preferences for the Tor session. Modify these settings if necessary. They are implemented to ensure anonymity and default configuration changes.
* However, if SOCKS port has changed for some reason (typically to `9151`), here is where you would modify the port.
* If some webpages are displaying improperly, this may be due to JavaScript being toggled off. Simply change `javascript.enabled` to `True`. Note that this may compromise anonymity.
