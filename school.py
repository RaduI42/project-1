def check_marks(marks):
    if marks > 100 or marks < 0:
        print("Re-Enter Maths Marks")
        return False
    return True
    
def write_data():
    with open("record.txt", "a") as f:
        name = input("Enter Student Name: ")
        while True:
            phy = float(input("Enter Physics Marks: "))
            chem = float(input("Enter Chemistry Marks: "))
            math = float(input("Enter Maths Marks: "))
            if check_marks(math) and check_marks(phy) and check_marks(math):
                st = name + " " + str(phy) + " " + str(chem) + " "+ str(math)
                f.write(st + "\n")
                break
def read_data(d):
    with open("record.txt", "r") as f:
        for line in f.readlines():
            name, phy, chem, math = line.split(" ")
            d[name] = (float(phy) + float(chem) + float(math)) / 3
    return d


d = {}
write_data()


name = input("Input name: ")
avg = d[name]
if avg < 50:
    grade = "E"
elif avg < 60:
    grade = "D"
    
elif avg < 70:
    grade = "C"
elif avg < 80:
    grade = "B"
else:
    grade = "A"
print("{} - Average: {:.2f} - Grade: {}".format(name,avg,grade))