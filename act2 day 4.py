phNo = input("Enter the phone number: ")
length = len(phNo)
if length == 12 \
    and phNo[1] == "+" \
    and phNo[2] == "2" \
    and phNo[3] == "7" \
    and phNo[:3].isdigit() \
    and phNo[4:7].isdigit() \
    and phNo[8:].isdigit() :
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")
    print("========restart========")