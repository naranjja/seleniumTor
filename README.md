# python27-selenium-tor-windows
Python 2.7 Selenium script for using The Onion Router nodes and relays in Windows (tested on Windows 10 64-bit).

## Requirements
* [Python 2.7](https://www.python.org/downloads/)
* [Tor Browser Bundle](https://www.torproject.org/download/download-easy.html.en)

## Instructions
1. Open `path.txt` and write absolute path to Tor Browser folder using single backslashes (`\`)
2. Run `pip install -r requirements.txt` inside project folder
3. Open `router.py` and write Selenium code within `# do something`
4. Run `router.py`!

## Custom settings
* The `setup_tor` function contains the profile preferences for the Tor session. Modify these settings if necessary. They are implemented to ensure anonymity and default configuration changes.
* However, if SOCKS port has changed for some reason (typically to `9151`), here is where you would modify the port.
* If some webpages are displaying improperly, this may be due to JavaScript being toggled off. Simply change `javascript.enabled` to `True`. Note that this may compromise anonymity.
* If initializing Tor takes longer than Selenium, pass a delay time (in seconds) as a second parameter to the `setup_tor` function.
