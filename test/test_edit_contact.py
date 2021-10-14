from model.contact import Contact


def test_edit_contacts_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    app.contact.edit_firstname(Contact(firstname="New firstname", lastname="New lastname"))

def test_edit_contacts_mobile(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test", mobile="89000000000"))
    app.contact.edit_firstname(Contact(mobile="+79999999999"))