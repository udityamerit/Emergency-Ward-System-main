class bed:
    def __init__(self):
        self.total = 0

    def display_beds(self):
         with open("C:\\Users\\adiro\\Downloads\\Emergency Ward System\\Ward\\bed.txt",'r') as file:
              self.total = file.read()
              print(self.total)
         
    def register_total_beds(self):
        total = int(input("Enter the amount of beds: "))
        self.total = total
        with open("C:\\Users\\adiro\\Downloads\\Emergency Ward System\\Ward\\bed.txt",'w+') as file:
                    file.write("Total Beds:"+str(self.total))
                    file.seek(0)
                    print(file.read())
        
    def update_total_beds(self):
         total_beds = int(input("Enter the total number of beds: "))
         self.total = total_beds
         with open("C:\\Users\\adiro\\Downloads\\Emergency Ward System\\Ward\\bed.txt",'w+') as file:
                    file.write("Total Beds: "+str(self.total))
                    file.seek(0)
                    print(file.read())
                    print("Your total number of beds has been Updated successfully")
        
    def allocate_bed_to_patient(self):
         with open("C:\\Users\\adiro\\Downloads\\Emergency Ward System\\Ward\\bed.txt",'r') as file:
              data = file.read()
              self.total = int(data.split(":")[1].strip())
              print("Your total beds was:",self.total)
              self.total -= 1
              print("Your Total beds now are:",self.total)
              print("Your bed has been allocated successfully")
    def deallocate_bed_to_patient(self):
         with open("C:\\Users\\adiro\\Downloads\\Emergency Ward System\\Ward\\bed.txt",'r') as file:
              data = file.read()
              self.total = int(data.split(":")[1].strip())
              print("Your total beds was:",self.total)
              self.total += 1
              print("Your Total beds now available are:",self.total)
              print("Your bed has been deallocated successfully")
    
    def operations(self):
         while True:
            print("---------------------------------------------------------------------------------")
            print("What Operations do you want to do:\n1.Display beds\n2.Register Total Beds\n3.Update Total Beds\n4.Allocate Patient to Bed\n5.Deallocate Patient from Bed")
            choice = int(input("Enter your choice: "))
            if (choice == 1):
                 bed.display_beds()
            elif (choice == 2):
                 bed.register_total_beds()
            elif (choice == 3):
                bed.update_total_beds()
            elif (choice == 4):
                bed.allocate_bed_to_patient()
            elif (choice == 5):
                bed.deallocate_bed_to_patient()
            else:
                print("Please Enter a Valid Option")
                print("---------------------------")
            break
         
                         
bed = bed()
#bed.operations()
