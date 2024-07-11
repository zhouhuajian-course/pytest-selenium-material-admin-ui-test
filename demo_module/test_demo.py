import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import util


class TestDemo:
    def test_search(self):
        driver = util.visit_page("https://.../list")
        # assert ... == 1
