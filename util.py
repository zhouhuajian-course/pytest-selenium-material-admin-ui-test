from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def login(account, password):
    driver = _get_web_driver()
    driver.get("https://.../login")
    # ... = driver.find_element(By.CSS_SELECTOR, "...")
    # ....send_keys("10010286")
    # ....click()


def visit_page(url):
    driver = _get_web_driver()
    driver.get(url)
    return driver


_driver = None


def _get_web_driver():
    global _driver
    if not _driver:
        options = Options()
        # 页面加载策略 解决等待慢问题
        options.page_load_strategy = 'eager'
        _driver = webdriver.Chrome(options)
        _driver.implicitly_wait(5)
        _driver.maximize_window()
    return _driver
