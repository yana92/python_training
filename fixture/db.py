import pymysql.connections
from model.group import Group
from model.contact import Contact
from model.address_in_groups import AddressInGroups


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, "
                           "home, mobile, work, phone2, "
                           "email, email2, email3 from addressbook "
                           "where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home_phone, mobile, work_phone, phone2,
                 email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, home_phone=home_phone, mobile=mobile, work_phone=work_phone, phone2=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_address_in_groups(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT address_in_groups.id, group_id "
                           "FROM address_in_groups "
                           "INNER JOIN addressbook "
                           "ON address_in_groups.id = addressbook.id "
                           "WHERE addressbook.deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(AddressInGroups(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list