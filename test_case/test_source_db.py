import unittest

from config import *
from test_case.login import login


class TestSource(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = login()
        self.chrome.get("https://{}:40010/#/environment?username={}".format(ip, login_user))

    def test_004_add_source_db(self):
        self.chrome.by_xpath("//span[text()='{}']".format(s1_name)).click()
        self.chrome.by_xpath("//div[text()='数据库信息']").click()
        self.chrome.by_xpath("//tbody/tr[last()]//span[text()='源数据库']").click()
        source_name = self.chrome.by_xpath("//p/label[text()='数据库名称']/following-sibling::span").text
        print("source_name:", source_name)
        self.chrome.by_xpath("//input[@placeholder='请输入数据库用户']").send_keys(s1_yang_user)
        self.chrome.by_xpath("//input[@placeholder='请输入数据库密码']").send_keys(s1_yang_pwd)
        self.chrome.by_xpath("//div/label[text()='数据存放存储池']/following-sibling::div/div").click()
        self.chrome.by_xpath("//div[not(contains(@style,'display'))]/div[@class='el-scrollbar']").click()
        self.chrome.by_xpath("//div/label[text()='归档日志存放存储池']/following-sibling::div/div").click()
        self.chrome.by_xpath("//div[not(contains(@style,'display'))]/div[@class='el-scrollbar']").click()
        self.chrome.by_xpath("//span[text()='验 证']").click()
        assert (self.chrome.is_has("数据库实例参数验证通过！"))
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.clear(self.chrome.by_xpath("//input[@max=4]"))
        self.chrome.by_xpath("//input[@max=4]").send_keys(4)
        self.chrome.by_xpath("//span[text()='完 成']").click()
        assert (self.chrome.is_has("添加源数据库成功！"))
        assert (self.chrome.wait_for(900,
                                     self.chrome.is_has,
                                     "//span[text()='{}']/../../..//span[text()='是']".format(source_name), xpath=True))

    def tearDown(self) -> None:
        self.chrome.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(TestEnv("test_add_user"))
    # suit.addTest(TestEnv("test_edit_user"))
    # suit.addTest(TestEnv("test_del_user"))
    run = unittest.TextTestRunner(verbosity=3)
    run.run(suit)

