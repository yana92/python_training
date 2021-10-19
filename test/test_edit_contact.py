from model.contact import Contact


def test_edit_contacts_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname", lastname="New lastname")
    app.contact.edit_firstname(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contacts_mobile(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test", mobile="89000000000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_firstname(Contact(mobile="+79999999999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)