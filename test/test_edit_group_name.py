def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_name
    app.session.logout()