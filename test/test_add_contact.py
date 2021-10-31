# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 40),
            home_phone=random_string("home_phone", 10), mobile=random_string("mobile", 10),
            work_phone=random_string("work_phone", 20), fax=random_string("fax", 10), email=random_string("email", 25),
            homepage=random_string("homepage", 30), address2=random_string("address2", 40),
            phone2=random_string("phone2", 10), notes=random_string("notes", 100))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    app.return_to_main_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
