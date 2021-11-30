import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from model.address_in_groups import AddressInGroups

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT address_in_groups.id, group_id "
                           "FROM address_in_groups "
                           "INNER JOIN addressbook "
                           "ON address_in_groups.id = addressbook.id "
                           "WHERE addressbook.deprecated = '0000-00-00 00:00:00'")
    for row in cursor:
        (id, group_id) = row
        AddressInGroups(id=str(id), group_id=str(group_id))
        print(row)
finally:
    cursor.close()