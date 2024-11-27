from testpage import OperationsHelper
import yaml
import time
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, get_title_font_size):
    logging.info("Test 1 starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['username'])
    test_page.enter_pass(testdata['password'])
    test_page.press_login_button()
    time.sleep(2)
    test_page.press_about_btn()
    time.sleep(1)
    time.sleep(testdata['sleep_time'])
    font_size = test_page.get_title_about()
    assert font_size == get_title_font_size
