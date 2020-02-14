import unittest
import HTMLTestRunner
import os
import time

test_dir = "./test_case/"
report_dir = "./report/"
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")


if __name__ == "__main__":
    result_path = os.path.join(report_dir, "report_{}_result.html".format(now))
    with open(result_path, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='接口自动化测试报告,测试结果如下：',
                                               description='用例执行情况：')
        runner.run(discover)


