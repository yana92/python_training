from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_group(Group(name="New name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test header"))
    app.group.edit_group(Group(header="New header"))