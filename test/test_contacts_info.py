from model.contact import Contact
import re
from random import randrange


#Осталось реализовать выбор рандомного контакта

def test_contacts_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="Test Lastname", firstname="Firstname", address="Test addres",
                                           home_phone="+74951111111", mobile="+79999999999", work_phone="Test Work",
                                           email="Test email", phone2="Home"))
    list = app.contact.get_contact_list()
    index = randrange(len(list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_contacts_from_home_page_and_db(app, db):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="Test Lastname", firstname="Firstname", address="Test addres",
                                           home_phone="+74951111111", mobile="+79999999999", work_phone="Test Work",
                                           email="Test email", phone2="Home"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range (len(contacts_from_home_page)):
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
        assert contacts_from_home_page[i].all_phones_from_home_page == \
               merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_emails_from_home_page == \
               merge_emails_like_on_home_page(contacts_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home_phone, contact.mobile, contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",
                     [contact.email, contact.email2, contact.email3]))

