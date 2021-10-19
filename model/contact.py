class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile=None, work_phone=None, fax=None, email=None, homepage=None,
                 address2=None, phone2=None, notes=None, id=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home_phone=home_phone
        self.mobile=mobile
        self.work_phone=work_phone
        self.fax=fax
        self.email=email
        self.homepage=homepage
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.id=id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname