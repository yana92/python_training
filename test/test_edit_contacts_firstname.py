def test_edit_contacts_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_firstname()
    app.session.logout()