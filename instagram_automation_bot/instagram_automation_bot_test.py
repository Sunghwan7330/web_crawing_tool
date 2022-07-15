import unittest

from instagram_automation_bot import InstagramAutomationBot


class InstagramAutomationBotTest(unittest.TestCase):

    def test_bot_option(self):
        bot_option = {
            "user_id" : "aaaaaa",
            "user_passwd" : "bbbbbb",
            "crawing_target_id_list" : ["aaaa1", "aaaa2", "aaaa3"]
        }
        insta_bot = InstagramAutomationBot(None)
        insta_bot.setOption(bot_option)
        self.assertEqual(insta_bot.getUserID(), "aaaaaa")
        self.assertEqual(insta_bot.getUserPassword(), "bbbbbb")
        self.assertEqual(insta_bot.getCrawingTargetList(), ["aaaa1", "aaaa2", "aaaa3"])

    def test_run_webdriver_is_none(self):
        bot_option = {
            "user_id": "aaaaaa",
            "user_passwd": "bbbbbb",
            "crawing_target_id_list": ["aaaa1", "aaaa2", "aaaa3"]
        }
        insta_bot = InstagramAutomationBot(None)
        insta_bot.setOption(bot_option)
        res = insta_bot.run_automation()
        self.assertEqual(res, False)

    def test_get_user_info(self):
        f = open("./instagram_sample_page.html", 'r', encoding='utf-8')
        html = f.read()
        f.close()

        insta_bot = InstagramAutomationBot(None)
        res = insta_bot.getUserInfoFromHtml(html)
        self.assertEqual(res[0], 116)
        self.assertEqual(res[1], 151)
        self.assertEqual(res[2], 198)


if __name__ == "__main__":
    unittest.main()
