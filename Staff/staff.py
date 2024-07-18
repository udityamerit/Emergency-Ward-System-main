class staff:
    def __init__(self, ID, name, role, schedule):
        self.id = ID
        self.name = name
        self.role = role
        self.schedule = schedule

    def staffinfo(self):

        print( f" The ID of the Staff Employee is: {self.id}\n The Name of the Staff Employee is: {self.name}\n The role of the Staff Employee is: {self.role}\n Schedule of the Staff Employee is: {self.schedule}")


staff1 = staff( "23ER67" , "Mohan", "Doctor", "6:00 AM-3:00 Pm")
staff1.staffinfo()
