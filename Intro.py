import sys

phones = ('iPhone', 'Samsung', 'OnePlus', 'Pixel')
iphone = phones[0]
samsung = phones[1]
onePlus = phones[2]
pixel = phones[3]


print("Welcome to Phone Dealer")
first_Name = raw_input("What is your first name?")
second_Name = raw_input(first_Name + " , " + "what is your second name?")
print("\n")
print("Your full name is " + first_Name + " " + second_Name)

person_Age = input("How old are you?")
if person_Age <= 17:
    print("Unfortunately, you cannot purchase a phone by yourself")
    print("Do you want to quit?")
    under_Age = raw_input("yes or no")
    yes = "yes" or "Yes"
    no = "no" or "No"
    if under_Age == no:
        under_Age_Mother_Name = raw_input("What is your mother full name")
        under_Age_Mother_Age = input("How much is your mother?")
        under_Age_Father_Name = raw_input("What is your father full name")
        under_Age_Father_Age = input("How much is your father?")

        print("1. " + iphone)
        print("2. " + samsung)
        print("3. " + onePlus)
        print("4. " + pixel)
        under_Age_Select_Phone = raw_input("This are the phones we have in stock, please one:")
        print("We are out of stock!")

    if under_Age == yes:
        print("Thanks for shopping at dealer phone!")
        sys.exit()

if person_Age >= 18:
    print("1. " + iphone)
    print("2. " + samsung)
    print("3. " + onePlus)
    print("4. " + pixel)
    under_Age_Select_Phone = raw_input("This are the phones we have in stock, please one:")
    print("We are out of stock!")
