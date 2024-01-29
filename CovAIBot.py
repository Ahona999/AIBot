# Symptoms Check
# Vaccination
# Helpline Numbers
# Safety Measures

def symptoms():
    count  = 0

    print("Do you have fever?")
    x = input("Enter 1 if Yes else any other key for No : ")

    if x == 1:
        count = count + 1

    print("Do you have Dry Cough?")
    x = input("Enter 1 if Yes else any other key for No : ")

    if x == 1:
        count = count + 1

    print("Do you have Tiredness?")
    x = input("Enter 1 if Yes else any other key for No : ")

    if x == 1:
        count = count + 1

    if count==0:
        print("Chances of being Covid +ve is very low")
        print("Get tested to be sure")
    elif count==1:
        print("Chances of being Covid +ve is low")
        print("Get tested to be sure")
    elif count==2:
        print("Chances of being Covid +ve is high")
        print("Get tested")
    elif count==3:
        print("Chances of being Covid +ve is very high")
        print("You must get tested")


def bookVaccine():
    print("To Book Vaccine, visit - https://www.cowin.gov.in/")

def helpLine():
    print("""HelpLine Numbers:
Health Ministry : 1075
Child : 1098
Mental Health : 9087654321
Senior Citizens : 14567
Ayush Covid-19 Counselling : 14443
MyGov Whatsapp Desk : 9013151515""")

def safety():
    print("""Some safety measures to follow:
          1 - Wear a mask
          2 - Wash your hands
          3 - Maintain a distance""")


print("Hello, Welcome to Covid AI. My name is Cov")
print("How may I assist you today\n")

# Infinite Loop takes place
while True:  
    print("""Please Enter:
      1 to Check for Symptoms
      2 to Book Vaccine
      3 to Get a list of Helpline Numbers
      4 to Get to know about safety measures\n""")

    choice = int(input("Enter your choice between: "))

    if choice == 1:
        symptoms()  
    elif choice == 2:
        bookVaccine()  
    elif choice == 3:
        helpLine()  
    elif choice == 4:
        safety()  
    else:
        print("Enter valid input")

    print("""\n\nTo start again Enter 1
    Enter any other key to Quit""")

    x = input("Enter your choice: ")  # Using input() to accept any key, not just integers

    if x != "1":  # Check for "1" to continue
        break  # Exit the loop if not "1"