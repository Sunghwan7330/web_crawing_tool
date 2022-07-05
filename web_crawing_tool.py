from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

from webdriver_builder.webdriver_builder import WebdriverBuilder


def get_instagram_follower(insta_info, driver):
    insta_url = 'https://www.instagram.com/'
    login_url = insta_url + "accounts/login"

    driver.get(login_url)
    time.sleep(5)

    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(insta_info['user_id'])
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(insta_info['user_passwd'])
    driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
    time.sleep(5)

    target_arr = insta_info['crawing_target_id']
    for target_name in target_arr:
        target_url = insta_url + target_name
        driver.get(target_url)
        time.sleep(5)

        body = driver.find_element(By.XPATH, '/html/body')

        div_tag = body.find_element(By.TAG_NAME, 'div')
        div_id = div_tag.get_attribute('id')

        post_cnt = driver.find_element('xpath', '//*[@id="%s"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[1]/div/span' % div_id).text
        follower_cnt = driver.find_element('xpath', '//*[@id="%s"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span' % div_id).text
        following_cnt = driver.find_element('xpath','//*[@id="%s"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span' % div_id).text
        name = driver.find_element('xpath', '//*[@id="%s"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/span' % div_id).text
        info = driver.find_element('xpath', '//*[@id="%s"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/div' % div_id).text
        print("post_cnt = {}".format(post_cnt))
        print("follower_cnt = {}".format(follower_cnt))
        print("following_cnt = {}".format(following_cnt))
        print("name = {}".format(name))
        print("info = {}".format(info))


    return


def main():
    print('hello world')
    with open('configuration.json') as f:
        conf = json.load(f)
    driver = WebdriverBuilder()\
            .setWebdriverJsonOption(conf['webdriver_option'])\
            .build()

    get_instagram_follower(conf['instagram'], driver)
    return

if __name__ == "__main__":
    main()