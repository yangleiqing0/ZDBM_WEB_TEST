import unittest

from config import *
from test_case.login import login
from utils import rand_str


class TestEnv(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = login()
        self.chrome.get("https://{}:40010/#/environment?username={}".format(ip, login_user))
        self.chrome.sleep(1)

    def add_source_env(self, name, _ip, port, sys_user, sys_pwd, tool_path):
        self.chrome.by_xpath("//div[text()='新增源环境']").click()
        self.chrome.by_xpath("//input[@placeholder='请输入环境名称']").send_keys(name)
        self.chrome.by_xpath("//input[@placeholder='请输入IP地址']").send_keys(_ip)
        self.chrome.clear(self.chrome.by_xpath("//input[@placeholder='请输入SSH 端口']"))
        self.padding_mes(name, port, sys_user, sys_pwd, tool_path)

    def padding_mes(self, name, port, sys_user, sys_pwd, tool_path):
        self.chrome.clear(self.chrome.by_xpath("//input[@placeholder='请输入SSH 端口']"))
        self.chrome.by_xpath("//input[@placeholder='请输入SSH 端口']").send_keys(port)
        self.chrome.clear(self.chrome.by_xpath("//input[@placeholder='请输入操作系统用户']"))
        self.chrome.by_xpath("//input[@placeholder='请输入操作系统用户']").send_keys(sys_user)
        self.chrome.by_xpath("//input[@placeholder='请输入操作系统密码']").send_keys(sys_pwd)
        self.chrome.clear(self.chrome.by_xpath("//input[@placeholder='请输入Tool包路径']"))
        self.chrome.by_xpath("//input[@placeholder='请输入Tool包路径']").send_keys(tool_path)
        self.chrome.by_xpath("//span[text()='验 证']").click()
        assert (self.chrome.is_has("主机信息验证成功！"))
        self.chrome.sleep(0.5)
        self.chrome.by_xpaths("//span[text()='确 定']")[3].click()
        assert (self.chrome.is_has("添加主机环境成功！"))
        assert (self.chrome.wait_for(180,
                                     self.chrome.is_has,
                                     "//span[text()='{}']/../../..//span[text()='在线']".format(name), xpath=True))

    def add_mdb_env(self, name, _ip, port, sys_user, sys_pwd, tool_path):
        self.chrome.by_xpath("//div[text()='新增目标环境']").click()
        self.chrome.by_xpath("//input[@placeholder='请输入环境名称']").send_keys(name)
        self.chrome.by_xpath("//span[@class='el-checkbox__inner']").click()
        self.chrome.by_xpath("//input[@placeholder='请输入IP地址']").send_keys(_ip)
        self.padding_mes(name, port, sys_user, sys_pwd, tool_path)

    def test_001_add_source_env(self):
        self.add_source_env(s1_name, s1_ip, s1_port, s1_sys_user, s1_sys_pwd, s1_tool_path)

    def test_002_add_mdb_env(self):
        self.add_mdb_env(m1_name, m1_ip, m1_port, m1_sys_user, m1_sys_pwd, m1_tool_path)

    def test_003_add_mdb_env(self):
        self.add_mdb_env(m2_name, m2_ip, m2_port, m2_sys_user, m2_sys_pwd, m2_tool_path)

    def tearDown(self) -> None:
        self.chrome.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(TestEnv("test_add_user"))
    # suit.addTest(TestEnv("test_edit_user"))
    # suit.addTest(TestEnv("test_del_user"))
    run = unittest.TextTestRunner(verbosity=3)
    run.run(suit)

