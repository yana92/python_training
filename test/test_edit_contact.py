from model.contact import Contact


def test_edit_contacts_name(app):
    app.contact.edit_firstname(Contact(firstname="New firstname", lastname="New lastname"))

def test_edit_contacts_mobile(app):
    app.contact.edit_firstname(Contact(mobile="+79999999999"))