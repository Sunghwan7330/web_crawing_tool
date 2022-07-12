import logging


class InstagramAutomationBot:

    def __init__(self, webdriver):
        self.logger = None
        self.webdriver = None
        self.user_id = None
        self.user_password = None
        self.crawing_target_id_list = None

        self.setDefaultLogger()
        self.insta_url = 'https://www.instagram.com/'
        self.login_url = self.insta_url + 'accounts/login'

        self.xpath_id_field = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        self.xpath_password_field = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        self.xpath_login_btn = '//*[@id="loginForm"]/div/div[3]'

        self.setWebdriver(webdriver)
        return


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
