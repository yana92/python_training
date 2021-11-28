from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact info
        self.fill_contact_form(contact)
        wd.find_element_by_id("content").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
#        self.waiting_contacts_table()
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        #wd.find_elements_by_name("selected[]")[id].click()
        wd.find_element_by_xpath("//input[@id='%s']" % id).click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        #        self.waiting_contacts_table()
        self.open_home_page()
        self.contact_cache = None

    def waiting_contacts_table(self):
        wd = self.app.wd
        wd.find_element_by_id("maintable")

    def open_home_page(self):
        wd = self.app.wd
#        if not (wd.current_url.endswith("/index.php")):
        wd.find_element_by_link_text("home").click()

    def open_edit_form_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()

    def open_edit_form_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        #wd.find_elements_by_xpath('//img[@title="Edit"]')[id].click()
        wd.find_element_by_xpath("//input[@id='%s']/../..//img[@title='Edit']" % id).click()

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath('//img[@title="Details"]').click()

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_edit_form_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.waiting_contacts_table()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_edit_form_by_id(id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.waiting_contacts_table()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache=[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_xpath("td")
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                address = element.find_element_by_xpath("td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_form_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile=mobile, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile=mobile, phone2=phone2)