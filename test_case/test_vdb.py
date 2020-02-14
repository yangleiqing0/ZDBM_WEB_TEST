import unittest

from config import *
from test_case.login import login


class TestVdb(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = login()
        self.chrome.get("https://{}:40010/#/sourceDb?username={}".format(ip, login_user))

    def create_snapshot(self):
        self.chrome.get("https://{}:40010/#/virtualDb?username={}".format(ip, login_user))
        self.chrome.by_xpath("//td//span").click()
        self.chrome.by_xpath("//span[text()='创建快照']").click()
        self.chrome.by_xpath("//div[@class='el-dialog__body']/following-sibling::div//span[text()='提 交']").click()
        assert (self.chrome.is_has("//p[contains(text(),'创建成功')]", xpath=True))

    def test_008_add_vdb(self):
        self.chrome.by_xpath("//div[text()='数据库恢复助手']").click()
        self.chrome.by_xpath("//button[@class='el-button def-btn el-button--default']/span[text()='确 定']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        vdb_name = self.chrome.by_xpath("//p/label[text()='VDB名称']/following-sibling::span").text
        self.chrome.by_xpath("//span[text()='确认提交']").click()
        assert (self.chrome.is_has("添加VDB({})成功！".format(vdb_name)))
        assert (self.chrome.wait_for(900,
                                     self.chrome.is_has,
                                     "//span[text()='{}']/ancestor::tr//span[contains(text(),'运行中:READ WRITE')]".format(
                                         vdb_name), xpath=True))

    def test_009_shutdown_vdb(self):
        self.chrome.get("https://{}:40010/#/virtualDb?username={}".format(ip, login_user))
        vdb_name = self.chrome.by_xpath("//i[@title='停止']/ancestor::tr/td//span").text
        self.chrome.by_xpath("//i[@title='停止']").click()
        self.chrome.by_xpath("//span[contains(text(),'确定')]").click()
        assert (self.chrome.until_for(120, self.chrome.is_has, "//p[text()='停止VDB数据库({})成功！']".format(
                                         vdb_name), xpath=True))

    def test_010_startup_vdb(self):
        self.chrome.get("https://{}:40010/#/virtualDb?username={}".format(ip, login_user))
        vdb_name = self.chrome.by_xpath("//i[@title='启动']/ancestor::tr/td//span").text
        self.chrome.by_xpath("//i[@title='启动']").click()
        self.chrome.by_xpath("//span[contains(text(),'确定')]").click()
        assert (self.chrome.until_for(120, self.chrome.is_has, "//p[text()='启动VDB数据库({})成功！']".format(
            vdb_name), xpath=True))

    def test_011_vdb_create_snapshot(self):
        self.create_snapshot()

    def test_012_vdb_reset_snapshot(self):
        self.chrome.get("https://{}:40010/#/virtualDb?username={}".format(ip, login_user))
        vdb_name = self.chrome.by_xpath("//td//span").text
        self.chrome.by_xpath("//td//span").click()
        self.chrome.by_xpath("//i[@title='重置VDB']").click()
        self.chrome.by_xpath("//span[contains(text(),'确定')]").click()
        assert (self.chrome.wait_for(900,
                                     self.chrome.is_has,
                                     "//span[text()='{}']/ancestor::tr//span[contains(text(),'运行中:READ WRITE')]".format(
                                         vdb_name), xpath=True))

    def test_013_vdb_delete_snapshot(self):
        self.create_snapshot()
        self.chrome.by_xpath("//div[@class='item__info'][last()]//i[@title='删除快照']").click()
        self.chrome.by_xpath("//span[contains(text(),'确定')]").click()
        assert (self.chrome.is_has("//p[text()='删除数据库快照成功！']", xpath=True))

    def test_014_v2p_file(self):
        self.chrome.by_xpath("//div[text()='数据库恢复助手']").click()
        self.chrome.by_xpath("//input[@placeholder='请选择恢复范围']").click()
        self.chrome.by_xpath("//span[text()='VDB迁移至其他环境(V2P)']").click()
        self.chrome.by_xpath("//button[@class='el-button def-btn el-button--default']/span[text()='确 定']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//input[@placeholder='请输入恢复数据文件的新位置']").send_keys(v2p_path)
        self.chrome.by_xpath("//span[text()='下一步']").click()
        self.chrome.by_xpath("//span[text()='下一步']", 2).click()
        self.chrome.by_xpath("//span[text()='提 交']").click()
        assert (self.chrome.is_has("//span[text()='查看详情']", xpath=True))
        self.chrome.by_xpath("//span[text()='查看详情']").click()
        assert (self.chrome.wait_for(600, self.chrome.is_has, "//label[text()='状态']/ancestor::p/span[text()='完成']",
                                     xpath=True))

    def test_015_delete_vdb(self):
        self.chrome.get("https://{}:40010/#/virtualDb?username={}".format(ip, login_user))
        vdb_name = self.chrome.by_xpath("//i[@title='删除']/ancestor::tr/td//span").text
        self.chrome.by_xpath("//i[@title='删除']").click()
        self.chrome.by_xpath("//span[contains(text(),'确定')]").click()
        assert (self.chrome.until_for(120, self.chrome.is_has, "//p[text()='删除VDB数据库{}成功！']".format(
            vdb_name), xpath=True))

    def tearDown(self) -> None:
        self.chrome.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(TestEnv("test_add_user"))
    # suit.addTest(TestEnv("test_edit_user"))
    # suit.addTest(TestEnv("test_del_user"))
    run = unittest.TextTestRunner(verbosity=3)
    run.run(suit)

