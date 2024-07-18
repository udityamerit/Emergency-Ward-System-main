#from Patient.patient import patient
#from Staff.staff import staff
from Ward.ward import bed
from Feedback.feedback import feed


print("----------------Welcome to Emergency Ward System-----------------")
print("Please Choose among the following operations below")
while True:
    print("1.)Patient Information\n2.)Staff Information\n3.)Bed Information\n4.)Feedback")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Patient Info")
    elif choice == 2:
        print("Staff Info")
    elif choice == 3:
        bed.operations()
    elif choice == 4:
        feed.feed_back()
    else:
        print("Please enter a valid choice")
    retry = input("Do you want to try again('y'or'n'):")
    if retry in ['yes','y']:
        continue
    else:
        break
    break
print("Thank You for using the service!")







    

    
    