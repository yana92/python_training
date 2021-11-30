from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    if len(orm.get_groups_without_contacts(Contact(id=contact.id))) == 0:
        app.group.create(Group(name="TestGroupName"))
    app.contact.open_home_page()
    groups = orm.get_groups_without_contacts(Contact(id=contact.id))
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(Group(id=group.id))