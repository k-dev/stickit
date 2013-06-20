import datetime
from django.utils.timezone import utc
from django.test import TestCase
from django.test.client import RequestFactory, Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from django.contrib.auth.models import User
from models import OrderItem, Order, Sticker
from django.core.management import call_command

class Pythonwd(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://localhost:8000"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_stickit_signup(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").send_keys("testUser")
		driver.find_element_by_name("email").clear()
		driver.find_element_by_name("email").send_keys("test@test.ua")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").send_keys("123456")
		driver.find_element_by_name("password2").clear()
		driver.find_element_by_name("password2").send_keys("123456")
		driver.find_element_by_css_selector("form.form-signin > button.btn").click()

	def test_stickit_login(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_link_text("Store").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").send_keys("test")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").send_keys("test")
		driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
		driver.find_element_by_link_text("Log Out").click()

	def test_stickit_emptycart(self):
		driver = self.driver
		driver.get(self.base_url + "/login")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").send_keys("test")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").send_keys("test")
		driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
		driver.find_element_by_link_text("Store").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_xpath("(//a[contains(text(),'Order')])[3]").click()
		driver.find_element_by_xpath("(//a[contains(text(),'Order')])[4]").click()
		driver.find_element_by_link_text("View Cart (3)").click()
		driver.find_element_by_css_selector("#cartItem_SCI-3 > td.item-remove > a.simpleCart_remove").click()
		driver.find_element_by_css_selector("#cartItem_SCI-2 > td.item-remove > a.simpleCart_remove").click()
		driver.find_element_by_link_text("Remove").click()
		driver.find_element_by_link_text("Proceed Order").click()
		self.assertEqual("Your Cart is empty! You should add items at first.", self.close_alert_and_get_its_text())

	def test_stickit_upload(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_link_text("Stick It").click()
		driver.find_element_by_link_text("Order your sticker").click()
		# driver.find_element_by_id("id_image").clear()
		driver.find_element_by_id("id_image").send_keys("/Users/kirill/Desktop/benefits_icons.png")
		driver.find_element_by_css_selector("input.btn").click()

	def test_stickit_checkout(self):
		driver = self.driver
		driver.get(self.base_url + "/login")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").send_keys("test")
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").clear()
		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").send_keys("test")
		driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
		driver.find_element_by_link_text("Stick It").click()
		driver.find_element_by_link_text("Order your sticker").click()
		driver.find_element_by_link_text("Store").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("Order").click()
		driver.find_element_by_link_text("View Cart (7)").click()
		driver.find_element_by_link_text("Proceed Order").click()

# 	def test_pythonwd(self):
# 		driver = self.driver
# 		driver.get(self.base_url + "/")
# 		driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
# 		# i = 0
# 		# while (len(User.objects.filter(username='testUser'+str(i))) > 0):
# 		# 	i = i + 1

# 		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").clear()
# 		driver.find_element_by_css_selector("form.form-signin > input[name=\"username\"]").send_keys("new")
# 		#user_"+str(i)
# 		driver.find_element_by_name("email").clear()
# 		driver.find_element_by_name("email").send_keys("new@o.oa")
# 		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").clear()
# 		driver.find_element_by_css_selector("form.form-signin > input[name=\"password\"]").send_keys("111111")
# 		driver.find_element_by_name("password2").clear()
# 		driver.find_element_by_name("password2").send_keys("111111")
# 		driver.find_element_by_css_selector("form.form-signin > button.btn").click()

# 		driver.find_element_by_link_text("Store").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("Order").click()
# 		driver.find_element_by_link_text("View Cart (6)").click()
# 		driver.find_element_by_link_text("-").click()
# 		driver.find_element_by_link_text("Proceed Order").click()
# 		driver.find_element_by_link_text("Store").click()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def is_link_text_present(self, what):
		try: self.driver.find_element_by_link_text(what)
		except NoSuchElementException, e: return False
		return True

	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException, e: return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)