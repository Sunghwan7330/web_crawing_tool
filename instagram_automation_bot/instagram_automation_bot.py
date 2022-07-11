
class InstagramAutomationBot:

    def __init__(self, webdriver):
        self.insta_url = 'https://www.instagram.com/'
        self.login_url = self.insta_url + 'accounts/login'

        self.xpath_id_field = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        self.xpath_password_field = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        self.xpath_login_btn = '//*[@id="loginForm"]/div/div[3]'

        self.setWebdriver(webdriver)
        return

    def setWebdriver(self, webdriver):
        self.webdriver = webdriver
        return


    def setOption(self, option):
        return

