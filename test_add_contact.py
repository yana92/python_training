# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        wb = self.wb
        self.open_main_page(wb)
        self.login(wb)
        self.create_contact(wb)
        self.return_to_main_page(wb)
        self.logout(wb)

    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def return_to_main_page(self, wb):
        wb.find_element_by_link_text("home").click()

    def create_contact(self, wb, firstname="Test First name", middlename="Tast Middle name", lastname="Test Last name",
                       nickname="Test Nickname", title="Test title", company="Test Company", address="Test Address",
                       home_phone="+74951111111", mobile="+79999999999", work="Test Work", fax="Test Fax",
                       email="Test email", homepage="Test Homepage", address2="Test Address", phone2="Home",
                       notes="Test Notes"):
        # init contact creation
        wb.find_element_by_link_text("add new").click()
        # fill contact info
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(firstname)
        wb.find_element_by_name("middlename").click()
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(middlename)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(lastname)
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(nickname)
        wb.find_element_by_name("title").click()
        wb.find_element_by_name("title").clear()
        wb.find_element_by_name("title").send_keys(title)
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(company)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(home_phone)
        wb.find_element_by_name("mobile").click()
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(mobile)
        wb.find_element_by_name("work").click()
        wb.find_element_by_name("work").clear()
        wb.find_element_by_name("work").send_keys(work)
        wb.find_element_by_name("fax").click()
        wb.find_element_by_name("fax").clear()
        wb.find_element_by_name("fax").send_keys(fax)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(email)
        wb.find_element_by_name("homepage").click()
        wb.find_element_by_name("homepage").clear()
        wb.find_element_by_name("homepage").send_keys(homepage)
        wb.find_element_by_name("address2").click()
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(address2)
        wb.find_element_by_name("phone2").click()
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(phone2)
        wb.find_element_by_name("notes").click()
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(notes)
        wb.find_element_by_id("content").click()
        # submit contact creation
        wb.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wb, user_name="admin", password="secret"):
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(user_name)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, wb):
        wb.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wb.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
