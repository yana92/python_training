from model.contact import Contact
import random


def test_edit_contacts_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    chanched_contact = Contact(lastname="New lastname", firstname="New firstname")
    #contact.id = old_contacts.id
    app.contact.edit_contact_by_id(contact.id, chanched_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_contacts_mobile(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="Test", mobile="89000000000"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.edit_firstname(Contact(mobile="+79999999999"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)