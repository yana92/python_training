from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm, db):
    if len(db.get_address_in_groups()) == 0:
        if len(orm.get_contact_list()) == 0:
            app.contact.create_contact(Contact(firstname="Test"))
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="TestGroupName"))
        contacts = orm.get_contact_list()
        contact = random.choice(contacts)
        app.contact.select_contact_by_id(contact.id)
        app.contact.click_add_contact_to_group()
    old_address_in_groups = db.get_address_in_groups()
    group = random.choice(old_address_in_groups)
    app.contact.delete_contact_from_group(group.group_id, 0)
    new_address_in_groups = db.get_address_in_groups()
    assert len(old_address_in_groups)-1 ==  len(new_address_in_groups)
    old_address_in_groups.remove(group)
    assert new_address_in_groups == old_address_in_groups


#    contacts = orm.get_contact_list()
#    contact = random.choice(contacts)
#    groups = db.get_address_in_groups()
#    group = random.choice(groups)
#    app.contact.add_contact_to_group(contact.id, group.id)
#    assert contact in orm.get_contacts_in_group(Group(id=group.id))