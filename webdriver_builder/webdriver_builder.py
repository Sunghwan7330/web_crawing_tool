from selenium import webdriver


class WebdriverBuilder:

    def __init__(self):
        # 멤버변수 초기화
        self.driver = None
        self.webdriver_create_func_dic = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox,
            "edge": webdriver.Edge
        }
        self.window_width = 1920
        self.window_height = 1080

        self.webdriver_type = None
        self.webdriver_path = None

        return

    def setWebdriverOption(self, option):
        if "webdriver_type" in option:
            self.setWebdriverType(option["webdriver_type"])
        if "webdriver_path" in option:
            self.setWebdriverPath(option["webdriver_path"])

        return self

    def setWebdriverType(self, type):
        self.webdriver_type = type

    def setWebdriverPath(self, path):
        self.webdriver_path = path

    def build(self):
        if self.webdriver_type is None:
            return None

        if self.webdriver_path is None:
            return None

        if self.webdriver_type not in self.webdriver_create_func_dic:
            return None

        webdriver_create_func = self.webdriver_create_func_dic[self.webdriver_type]
        self.driver = webdriver_create_func(self.webdriver_path)
        self.driver.set_window_size(self.window_width, self.window_height)
        return self.driver
