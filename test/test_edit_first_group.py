from model.group import Group


def test_edit_group_name(app):
    app.group.edit_group(Group(name="New name"))
    app.session.logout()

def test_edit_group_header(app):
    app.group.edit_group(Group(header="New header"))