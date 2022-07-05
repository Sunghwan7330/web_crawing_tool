from selenium import webdriver


class WebdriverBuilder:

    def __init__(self):
        # 멤버변수 초기화
        self.driver = None
        self.webdriver_type_list = ["chrome", "firefox", "edge"]
        self.window_width = 1920
        self.window_height = 1080

        self.webdriver_type = None
        self.webdriver_path = None

        return

    def setWebdriverJsonOption(self, option):
        # TODO 옵션 없을때 예외처리 필요
        self.webdriver_type = option["webdriver_type"]
        self.webdriver_path = option["webdriver_path"]

        return self

    def build(self):
        # TODO 드라이버 지원하지 않을 때 예외처리 추가
        # TODO 드라이버 파일 없을 때 예외처리 추가

        if self.webdriver_type == "chrome":
            self.__setChromeDriver()
        self.driver.set_window_size(self.window_width, self.window_height)
        return self.driver

    def __setChromeDriver(self):
        self.driver = webdriver.Chrome(self.webdriver_path)

    def __setFirefoxDriver(self):
        self.driver = webdriver.Firefox(self.webdriver_path)

    def __setEdgeDriver(self):
        self.driver = webdriver.Edge(self.webdriver_path)


