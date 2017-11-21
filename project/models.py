from project import db

class Employee(db.Model):
    """ Employee Model with all data about business Employees. """
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    address_line_1 = db.Column(db.String)
    address_line_2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    social_security = db.Column(db.String)
    federal_withholdings = db.Column(db.Integer)
    state_line1_withholdings = db.Column(db.Integer)
    state_line2_withholdings = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    marital_status = db.Column(db.String)

    def __init__(self, last_name, first_name, address_line_1, address_line_2, city, state, zip_code, social_security, 
        federal_withholdings, state_line1_withholdings, state_line2_withholdings, salary, marital_status):
        self.last_name = last_name
        self.first_name = first_name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.social_security = social_security
        self.federal_withholdings = federal_withholdings
        self.state_line1_withholdings = state_line1_withholdings
        self.state_line2_withholdings = state_line2_withholdings
        self.salary = salary
        self.marital_status = marital_status

    def __repr__(self):
        return "<Employee(last_name='%s', first_name='%s', address_line_1='%s', address_line_2='%s', city='%s', state='%s', \
            zip_code='%d', social_security='%s', federal_withholdings='%d', state_line1_withholdings='%s', \
            state_line2_withholdings'%s', salary='%d', marital_status='%s')>" \
               % (self.last_name, self.first_name, self.address_line_1, self.address_line_2, self.city, self.state, 
                self.zip_code, self.social_security, self.federal_withholdings, self.state_line1_withholdings,
                self.state_line2_withholdings, self.self.salary, self.marital_status)

class Customer(db.Model):
    """ Customer Model with all data about Customers. """
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    address_line_1 = db.Column(db.String)
    address_line_2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, company, last_name, first_name, address_line_1, address_line_2, city, state, zip_code, price):
        self.company = company
        self.last_name = last_name
        self.first_name = first_name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.price = price

    def __repr__(self):
        return "<Customer(company='%s', last_name='%s', first_name='%s', address_line_1='%s', address_line_2='%s', \
                city='%s', state='%s', zip_code='%d', price='%d')>" \
               % (self.company, self.last_name, self.first_name, self.address_line_1, self.address_line_2,
                self.city,  self.state, self.zip_code, self.price)

class Vendor(db.Model):
    """ Vendor Model with all data about Vendor. """
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String)
    part = db.Column(db.String)
    price = db.Column(db.Integer)
    address_line_1 = db.Column(db.String)
    address_line_2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)

    def __init__(self, company, part, price, address_line_1, address_line_2, city, state, zip_code):
        self.company = company
        self.part = part
        self.price = price
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return "<Vendor(company='%s', part='%s', price='%d', address_line_1='%s', address_line_2='%s',city='%s', \
                state='%s', zip_code='%d')>" \
               % (self.company, self.part, self.price, self.address_line_1, self.address_line_2, self.city, 
                self.state, self.zip_code)

class PayrollEvents(db.Model):
    """ PayrollEvents Model with all the different payroll events that happen. """
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.Integer)
    bounce = db.Column(db.Integer)
    federal_tax_withholding = db.Column(db.Integer)
    state_tax_withholding = db.Column(db.Integer)
    social_security_tax = db.Column(db.Integer)
    medicare_tax = db.Column(db.Integer)
    employee_name = db.Column(db.String)
    total_paid = db.Column(db.Integer)

    def __init__(self, salary, bounce, federal_tax_withholding, state_tax_withholding, social_security_tax, medicare_tax, 
                employee_name, total_paid):
        self.salary = salary
        self.bounce = bounce
        self.federal_tax_withholding = federal_tax_withholding
        self.state_tax_withholding = state_tax_withholding
        self.social_security_tax = social_security_tax
        self.medicare_tax = medicare_tax
        self.employee_name = employee_name
        self.total_paid = total_paid

    def __repr__(self):
        return "<PayrollEvents(salary='%d', bounce='%d', federal_tax_withholding='%d', state_tax_withholding='%d', \
                social_security_tax='%d',medicare_tax='%d', employee_name='%s', total_paid='%d')>" \
               % (self.salary, self.bounce, self.federal_tax_withholding, self.state_tax_withholding,
                self.social_security_tax, self.medicare_tax,  self.employee_name, self.total_paid)