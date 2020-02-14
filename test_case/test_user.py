import unittest

from config import ip, login_user, email, phone, login_pwd, new_phone
from test_case.login import login
from utils import rand_str


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = login()
        self.chrome.get("https://{}:40010/#/user?username={}".format(ip, login_user))
        self.chrome.sleep(1)

    def test_005_add_user(self):
        name = rand_str(5)
        self.chrome.by_xpath("//div[text()='添加用户']").click()
        self.chrome.by_xpath("//input[@placeholder='请输入用户']").send_keys(name)
        self.chrome.by_xpath("//input[@placeholder='请输入邮箱地址']").send_keys(email)
        self.chrome.by_xpath("//input[@placeholder='请输入手机号']").send_keys(phone)
        self.chrome.by_xpath("//input[@placeholder='请输入密码']").send_keys(login_pwd)
        self.chrome.by_xpath("//span[text()='完 成']").click()
        assert(self.chrome.is_has("添加用户成功！"))

    def test_006_edit_user(self):
        self.chrome.by_xpath("//div[text()='{}']/../..//i[@title='编辑']".format(email)).click()
        self.chrome.clear(self.chrome.by_xpath("//input[@placeholder='请输入手机号']"))
        self.chrome.by_xpath("//input[@placeholder='请输入手机号']").send_keys(new_phone)
        self.chrome.sleep(0.5)
        self.chrome.by_xpath("//div[@class='base-container']/div[5]//span[text()='完 成']").click()
        assert(self.chrome.is_has(new_phone, "div"))

    def test_007_del_user(self):
        name = self.chrome.by_xpath("//div[text()='{}']/../../td/div".format(email)).text
        self.chrome.by_xpath("//div[text()='{}']/../..//i[@title='删除']".format(email)).click()
        self.chrome.by_xpath("//span[contains(text(), '确定')]").click()
        assert(self.chrome.is_has("删除用户({})成功！".format(name)))

    def tearDown(self) -> None:
        self.chrome.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestUser("test_add_user"))
    suit.addTest(TestUser("test_edit_user"))
    suit.addTest(TestUser("test_del_user"))
    run = unittest.TestRunner()
    run.run(suit)

