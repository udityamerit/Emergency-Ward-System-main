class Hostpital:
    def __init__(self, name, location, department):
        self.name = name
        self.location = location
        self.department = department

    def hospitalinfo(self):

        print( f" The name of the Hospital is: {self.name}\n Location of the Hostpital is:{self.location}\n Department of the hostpital is: {self.department}\n ")

class Staff:
    def __init__(self, ID, name, role, schedule):
        self.id = ID
        self.name = name
        self.role = role
        self.schedule = schedule

    def staffinfo(self):

        print( f" The ID of the Staff Employee is: {self.id}\n The Name of the Staff Employee is: {self.name}\n The role of the Staff Employee is: {self.role}\n Schedule of the Staff Employee is: {self.schedule}")

hos = input("Enter the name of the Hostpital: ")
loc = input("Enter the Location of the Hospital: ")
depart = input("Enter the main department of the Hospital: ")

hp = Hostpital(hos,loc,depart)
hp.hospitalinfo()

staff1 = Staff( "23ER67" , "Mohan", "Doctor", "6:00 AM-3:00 Pm")
staff1.staffinfo()

