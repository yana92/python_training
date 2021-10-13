from model.contact import Contact


def test_edit_contacts_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_firstname(Contact(firstname="New firstname", lastname="New lastname"))
    app.session.logout()

def test_edit_contacts_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_firstname(Contact(mobile="+79999999999"))
    app.session.logout()