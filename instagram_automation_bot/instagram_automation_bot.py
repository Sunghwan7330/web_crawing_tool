import logging
import time

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class InstagramAutomationBot:

    def __init__(self, webdriver):
        self.logger = None
        self.webdriver = None
        self.user_id = None
        self.user_password = None
        self.crawing_target_id_list = None

        self.setWebdriver(webdriver)
        self.setDefaultLogger()
        self.insta_url = 'https://www.instagram.com/'
        self.login_url = self.insta_url + 'accounts/login'

        self.xpath_id_field = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        self.xpath_password_field = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        self.xpath_login_btn = '//*[@id="loginForm"]/div/div[3]'

        self.setWebdriver(webdriver)
        return

    def run_automation(self):
        if self.webdriver is None:
            self.logger.error("Webdriver is not setting.")
            return False

        if self.user_id is None:
            self.logger.error("user id is not setting.")
            return False

        if self.user_password is None:
            self.logger.error("user password is not setting.")
            return False

        driver = self.webdriver
        driver.get(self.login_url)
        driver.implicitly_wait(3)

        driver.find_element('xpath', self.xpath_id_field).send_keys(self.user_id)
        driver.find_element('xpath', self.xpath_password_field).send_keys(self.user_password)
        driver.find_element('xpath', self.xpath_login_btn).click()
        driver.implicitly_wait(5)
        time.sleep(5)

        return True

    def setWebdriver(self, webdriver):
        self.webdriver = webdriver

    def setDefaultLogger(self):
        self.logger = logging.getLogger("InstagramAutomationBot")
        self.setLogLevel(logging.INFO)
        self.setLogFormat('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')

    def setLogLevel(self, level):
        self.logger.setLevel(level)

    def setLogFormat(self, format):
        formatter = logging.Formatter(format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def setWebdriver(self, webdriver):
        self.webdriver = webdriver
        return

    def setOption(self, option):
        option_list = [
            ("user_id", self.setUserID),
            ("user_passwd", self.setUserPassword),
            ("crawing_target_id_list", self.setCrawingTargetIdList)
        ]
        for key, set_func in option_list:
            if key in option:
                set_func(option[key])
        return

    def getKeywordFirstTagValue(self, html, keyword):
        idx = html.find(keyword) + len(keyword)

        temp = html[idx:idx + 100]
        target_tag = ''
        for i in range(len(temp)):
            if temp[i] != '<':
                continue
            idx = temp.find(' ', i, len(temp))
            target_tag = temp[i+1:idx]
            break

        soup = BeautifulSoup(temp, 'html.parser')
        res = soup.select(target_tag)
        if len(res) == 0:
            return None

        return res[0].text

    def getUserInfoFromHtml(self, html):
        feed_cnt = int(self.getKeywordFirstTagValue(html, '게시물'))
        follower_cnt = int(self.getKeywordFirstTagValue(html, '팔로워'))
        follow_cnt = int(self.getKeywordFirstTagValue(html, '팔로우'))

        return [feed_cnt, follower_cnt, follow_cnt]

    def setUserID(self, user_id):
        self.user_id = user_id

    def getUserID(self):
        return self.user_id

    def setUserPassword(self, user_password):
        self.user_password = user_password

    def getUserPassword(self):
        return self.user_password

    def setCrawingTargetIdList(self, crawing_target_id_list):
        self.crawing_target_id_list = crawing_target_id_list

    def getCrawingTargetList(self):
        return self.crawing_target_id_list
