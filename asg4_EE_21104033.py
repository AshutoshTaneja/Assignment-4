"""-----------------question1-----------------"""
print("Question1")

def towerOfHanoi(n):
    if n==1:
        return 1
    return (2*towerOfHanoi(n-1)+1)
print(f"For a Tower Of Hanoi game with 5 disks it will take {towerOfHanoi(5)} moves to move all disks to another tower.")


"""-----------------question2-----------------"""
print("\nQuestion2")

rows = int(input("Enter the number of pascal traingles rows to print: "))

    #Iterative Method
print("Iterative Method")
prevSequence = []
currSequence = []
for a in range(1, rows+1):
    if a==1:
        print(" "*(rows-a-1), 1)
    else:
        print(" "*(rows-a), end="")
        for i in range(len(prevSequence)-1):
            currSequence.append(prevSequence[i]+prevSequence[i+1])
        currSequence.insert(0, 1)
        currSequence.append(1)
        prevSequence = currSequence
        currSequence = []
        print(*prevSequence, sep=" ")

    #Recursive Method
print("\nRecursive Method")
prevSequence = []
currSequence = []

def pascalTriangle(n, prev, curr):
    if n == 0:
        return
    if n==rows:
        print(" "*(n-1), 1)
    else:
        print(" "*n, end="")
        curr = [prev[a]+prev[a+1] for a in range(len(prev)-1)]
        curr.insert(0, 1)
        curr.append(1)
        print(*curr, )
    return pascalTriangle(n-1, curr, [])
pascalTriangle(rows, prevSequence, currSequence)


"""-----------------question3-----------------"""
print("\nQuestion3")

first = int(input("Input an integer value(dividend): "))
second = int(input("Input another integer value(divisor): "))

if second!=0: result = [first//second, first%second]

    #part a.
print("part a.", end=" ")
if callable(first) and callable(second):
    print("The values are Callable.")
else:
    print("The values are not Callabale.")

    #part b.
print("part b.", end=" ")
if first!=0 and second!=0:
    print("All values are non-zero.")
else:
    print("All values are not non-zero.")

    #part c.
print("part c.", end=" ")
result.append(4)
result.append(5)
result.append(6)
result = list(filter(lambda x: x>4, result))
print(result)

    #part d.
print("part d.", end=" ")
result = set(result)
print(result)

    #part e.
print("part e.", end=" ")
result = frozenset(result)
print(result)

    #part f.
print("part f.", end=" ")
print("The maximum value in the set is ", max(result), " and it's hash value is ", hash(max(result)), ".")


"""-----------------question4-----------------"""
print("\nQuestion4")

class Student:
    def __init__(self, name, rollNum):
        self.name = name
        self.rollNum = rollNum
        print("Object is Created.")
    def __repr__(self):
        return f"Name: {self.name}, Roll Number:{self.rollNum}."
    def __del__(self):
        print("Object is Destroyed.")

stud = Student("Ashutosh Taneja", 21104033)
print(stud)
del stud


"""-----------------question5-----------------"""
print("\nQuestion5")

employeeRecord = {"Mehak": 40000, "Ashok": 50000, "Viren": 60000}
print(*[f"{name} has a salary of {salary}." for name, salary in employeeRecord.items()], sep="\n")

    #part a.
print("part a.")
employeeRecord["Mehak"] = 70000
print(*[f"{name} has a salary of {salary}." for name, salary in employeeRecord.items()], sep="\n")

    #part b.
print("part b.")
del employeeRecord["Viren"]
print(*[f"{name} has a salary of {salary}." for name, salary in employeeRecord.items()], sep="\n")


"""-----------------question6-----------------"""
print("\nQuestion6")

scrambledWord = input("George: ")
meaningfulWord = input("Barbie: ")

if len(scrambledWord) == len(meaningfulWord):
    aBool = True
    for char in scrambledWord:
        if char not in meaningfulWord:
            aBool = False
            print("Shopkeeper: \"The friendship is fake.\"")
            break
    if aBool: print("Shopkeeper: \"The friendship is real.\"")
else:
    print("Shopkeeper: \"The friendship is fake.\"")