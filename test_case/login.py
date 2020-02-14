from utils import Chrome
from config import ip, login_user, login_pwd
import time


def login():

    chrome = Chrome()
    chrome.get("https://{}:40010".format(ip))
    time.sleep(5)
    chrome.by_xpath("//input[@placeholder='请输入用户名']").send_keys(login_user)
    chrome.by_xpath("//input[@placeholder='请输入密码']").send_keys(login_pwd)
    chrome.by_xpath("//span[text()='登录']").click()
    time.sleep(2)
    # chrome.driver.get("https://{}:40010/#/user?username={}".format(ip, login_user))
    # time.sleep(2)
    return chrome


if __name__ == '__main__':
    login()
