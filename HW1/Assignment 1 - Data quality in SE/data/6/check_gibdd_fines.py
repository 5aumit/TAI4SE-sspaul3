import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import emailwork
import re

debug = True
WebDriverWaitInSec = 30
binary = FirefoxBinary('c:\geckodriver\geckodriver.exe')


def init_driver():
    binary = r'c:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    options = Options()
    options.binary = binary
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True #optional
    return webdriver.Firefox(options=options, capabilities=cap, executable_path="c:\\geckodriver\\geckodriver.exe")


def sleep(secs, place='whatever'):
    ttlsecs = secs
    while secs > 0:
        time.sleep(1)
        print('now: {} - {} of {} in {}'.format(datetime.datetime.now(), secs, ttlsecs, place))
        secs -= 1


cars = {'х988то750': 'https://xn--90adear.xn--p1ai/check/fines#%D1%85988%D1%82%D0%BE+750+9907379357',
        'в691ем777': 'https://xn--90adear.xn--p1ai/check/fines#%D0%B2691%D0%B5%D0%BC+777+5047741110'}


if __name__ == "__main__":
    for car, link in cars.items():
        browser = init_driver()
        sleep(10, 'стартуем')
        browser.get(link)
        sleep(20, 'открываем сайт гибдд')
        btn_check = browser.find_element_by_xpath('//*[@id="checkFines"]/p[4]/a')
        btn_check.click()
        sleep(180, 'ждем проверку')
        src = browser.page_source
        text_found = re.search(r'В результате проверки не были найдены сведения о неуплаченных штрафах', src)
        if text_found is None:
            emailwork.send_mail('user@gmail.com', car + ' - есть штраф', link)
        else:
            emailwork.send_mail('user@gmail.com', car + ' - нет штрафа', link)
        browser.quit()


