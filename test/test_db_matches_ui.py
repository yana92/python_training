from model.group import Group
from model.contact import Contact
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: (map(clean, db.get_group_list())), number=3000))
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, db):
    print(timeit(lambda: app.contact.get_contact_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: (map(clean, db.get_group_list())), number=3000))
    ui_list = app.contact.get_contact_list()
    ui_list_new = []
    for s in ui_list:
        ui_list_new.append(s.replace(" ", ""))
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)