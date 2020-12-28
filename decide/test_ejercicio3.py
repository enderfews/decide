# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEjercicio3():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_ejercicio3(self):
    self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
    self.driver.set_window_size(550, 693)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("usuarioFalso123")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("contraseñaFalsa123")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errornote").text == "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."
  