from model.contact import Contact


def test_edit_contacts_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_firstname(Contact(firstname="New firstname", lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contacts_mobile(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test", mobile="89000000000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_firstname(Contact(mobile="+79999999999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)