from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from subprocess import Popen
from os import getcwd
from time import sleep

def setup_tor(binary, delay=False):
    global driver

    Popen('initialize.bat', cwd=getcwd())

    if delay:
        sleep(delay)

    driver = webdriver.Firefox(firefox_binary=binary)

    driver.profile.set_preference('network.proxy.type', 1)
    driver.profile.set_preference('network.proxy.socks', '127.0.0.1')
    driver.profile.set_preference('network.proxy.socks_port', 9051)
    driver.profile.set_preference('network.cookie.lifetimePolicy', 2)
    driver.profile.set_preference('network.dns.disablePrefetch', True)
    driver.profile.set_preference('network.http.sendRefererHeader', 0)
    driver.profile.set_preference('privacy.clearOnShutdown.offlineApps', True)
    driver.profile.set_preference('privacy.clearOnShutdown.passwords', True)
    driver.profile.set_preference('privacy.clearOnShutdown.siteSettings', True)
    driver.profile.set_preference('privacy.sanitize.sanitizeOnShutdown', True)
    driver.profile.set_preference('signon.rememberSignons', False)
    driver.profile.set_preference('places.history.enabled', False)
    driver.profile.set_preference('javascript.enabled', False)


def check_tor():
    try:
        driver.get('https://check.torproject.org')
        if 'tor-on' in driver.find_element_by_class_name('onion').get_attribute('src'):
            print 'Connection successful.'
            print 'Configuration successful.'
            return True
        else:
            print 'Connection successful.'
            print 'Configuration error.'
            driver.quit()
            return False
    except NoSuchElementException:
        print 'Connection error.'
        driver.quit()
        return False



if __name__ == '__main__':
    binary = FirefoxBinary('{}\\Browser\\firefox.exe'.format(open('path.txt', 'r').read().strip('\n')))

    setup_tor(binary)
    check_tor()

    # do something

    driver.quit()
