import time
import json

from instagram_automation_bot.instagram_automation_bot import InstagramAutomationBot
from webdriver_builder.webdriver_builder import WebdriverBuilder


def main():
    print('hello world')

    with open('configuration.json') as f:
        conf = json.load(f)
    driver = WebdriverBuilder() \
        .setWebdriverOption(conf['webdriver_option']) \
        .build()

    insta_bot = InstagramAutomationBot(driver)
    insta_bot.setOption(conf['instagram'])
    insta_bot.run_automation()

    time.sleep(10)
    return


if __name__ == "__main__":
    main()
