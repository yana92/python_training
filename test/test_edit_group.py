from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    chanched_group = Group(name="New name")
    app.group.edit_group_by_id(group.id, chanched_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.id = chanched_group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test header"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)