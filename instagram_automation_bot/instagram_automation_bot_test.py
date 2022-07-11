import unittest

from instagram_automation_bot.instagram_automation_bot import InstagramAutomationBot


class InstagramAutomationBotTest(unittest.TestCase):

    def bot_option_test(self):
        bot_option = {
            "user_id" : "aaaaaa",
            "user_passwd" : "bbbbbb",
            "crawing_target_id" : ["aaaa1", "aaaa2", "aaaa3"]
        }
        insta_bot = InstagramAutomationBot(None)
        insta_bot.setOption(bot_option)
        self.assertEqual(insta_bot.getUserID(), "aaaaa")
        self.assertEqual(insta_bot.getUserPassword(), "bbbbbb")
        self.assertEqual(insta_bot.getCrawingTargetList(), ["aaaa1", "aaaa2", "aaaa3"])


if __name__ == "__main__":
    unittest.main()
