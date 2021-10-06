# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Test First name", middlename="Tast Middle name",
                                       lastname="Test Last name", nickname="Test Nickname", title="Test title",
                                       company="Test Company", address="Test Address", home_phone="+74951111111",
                                       mobile="+79999999999", work_phone="Test Work",
                                       fax="Test Fax", email="Test email", homepage="Test Homepage",
                                       address2="Test Address", phone2="Home", notes="Test Notes"))
    app.return_to_main_page()
    app.session.logout()
