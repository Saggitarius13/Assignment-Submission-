#Python Assignment 3 ---> Prem Shankar SID-21104084
#Q1.
user_input = input("Enter any sentence/word of your choice\n")
if " " not in user_input: # the case when the user enters only single word
    empty_list1 = []   # the list is created because if a user enters a word for example "hello" the program does not show "l occured two times" more than one time..

    for ch in user_input:
        if ch not in empty_list1:
            empty_list1.append(ch)
            print(f"{ch} occured {user_input.count(ch)} times")
else:
    splits = user_input.split()
    empty_list2 = []


    for words in splits:
        if words not in empty_list2:
            empty_list2.append(words)
            print(f"{words} occured {user_input.count(words)} times")

#Q2.
day = int(input("Enter the Day\n"))
if day>31 or day<=0:
    print("Invalid date input")
else:
    month =int(input("Enter the Month\n"))
    if month>12 or month<1:
        print("Invalid month input")
    else:
        year = int(input("Enter the Year\n"))
        if year>2025 or year<1800:
            print("Invalid year Input")
        else:
            if day==31 and month==12:
                print(f"The next date is {day-30}/{month-11}/{year+1}")
            elif day==28 and month==2 and year==1800 :
                print(f"The next date is {day-27}/{month+1}/{year}")
            elif day==28 and month==2 and year==1900 :
                print(f"The next date is {day-27}/{month+1}/{year}")
            elif day==28 and month==2 and year%4==0:
                print(f"The next date is {day+1}/{month}/{year}")
            elif day==28 and month==2 and year%4!=0:
                print(f"The next date is {day-27}/{month+1}/{year}")
            elif day==30 and month!=2 and month!= 12:
                print(f"The next date is {day-29}/{month+1}/{year}")
            elif day==30 and month==2:
                print("Invalid date input")
            elif day ==29 and month==2 and year==1800 :
                print("Invalid date Input")
            elif day ==29 and month==2 and year==1900:
                print("Invalid date input")
            elif day==29 and month==2 and year%4==0:
                print(f"The next date is {day-28}/{month+1}/{year}")
            elif day==29 and month==2 and year%4!=0:
                print("Invalid date input")
            elif day<30 and month<12:
                print(f"The next date is {day+1}/{month}/{year}")
            elif day==30 and month%2!=0:
                print(f"The next date is {day+1}/{month}{year}")
            elif day==30 and month==11 or month==9:
                print(f"The next date is {day-29}/{month+1}/{year}")
            elif day==30 and month%12==0:
                print(f"The next date is {day+1}/{month}/{year}")
            elif day == 31 and month == 4 or month==6 or month==9 or month==11:
                print("Invalid input date")
            elif day==31 and month==10 or month==7 or month==8 or month==1 or month==3 or month==5:
                print(f"The next date is {day-30}/{month+1}/{year}")
            elif day==30 and month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                print(f"The next date is {day+1}/{month}/{year}")

print("Thank You")

# Q3.


li1 = []
print("This is a program to print list of tuples haveing a number and  the square of the same number.")
input_details = input("Please write 'Y' to continue\n")
while(input_details=='Y'):
    numbers = int(input("Please enter the number\n"))
    k = li1.append(numbers) # to add the integers that are being entered by the users to the empty list created before
    input_details = input("Do you want to add more numbers. If yes write 'Y' otherwise 'N'\n")
    if input_details == 'N':
        li2 = [(a,a*a) for a in li1]
        print(f"The list of tuple/s with the first element as number and second element square of the number is:\n{li2}")

# Q4

grade = int(input("Enter your grade point\n"))

if grade == 4:
    print("Your Grade is 'D' and Poor performance")
elif grade == 5:
    print("Your Grade is 'C' and Below Average performance")
elif grade == 6:
    print("Your Grade is 'C+' and Average performance")
elif grade == 7:
    print("Your Grade is 'B' and Good Performance")
elif grade == 8:
    print("Your Grade is 'B+' and Very Good Performance")
elif grade == 9:
    print("Your Grade is 'A' and Excellent performance")
elif grade == 10:
    print("Your Grade is 'A+' and Outstanding performance")
else:
    print("Invalid Input Grade Point")


# Q5.
k = 0
for i in range(6):
    print(" "*i,end = "") # print spaces according to the value of i..
    j = 10
    while(j>=k):
        print(chr(75-j),end = "") # chr(75-j) print the alphabets according to the value of j..
        j = j-1
    k = k+2

    print() # to reach to the next line because "end" will not allow to do so.



# Q6.
print("Welcome to the student's data storing platform ")
k = input("Please write 'Y' to continue\n")
dict = {}
while(k=="Y"):
    name = input("Enter the name of the student\n")
    SID = int(input("Enter the SID of the student\n"))
    k = input("If you want to add more student's detais write 'Y' otherwise write 'N'\n")
    dict1 = {}
    dict1[SID] = name
    dict.update(dict1) # to constantly add the new entries to the original dictionary.
# a.
    if k=="N":
        print(f" a.The details stored in the dictionary is\n{dict}")
        sorted_name = sorted(dict.values())
        print(f"b. The sorted dictionary by student name is\n{sorted_name}")
        sorted_SID = sorted(dict.keys())
        print(f"c. The sorted dictionary by SID is \n{sorted_SID}")
        finding_details = int(input("Enter the SID of the student whose name you want to search\n"))
        print(f"d.The name of the student with this SID is {dict[finding_details]}")

# Q7.
Number_of_terms = int(input("Enter the number of terms of the fibonacci sequence you want to print\n"))

n1 = 0
n2 = 1
Sum = 0


count = 0
print("The required fibonacci sequence is:\n")
while(count <  Number_of_terms):
    print(n1,end = " ")
    Sum = Sum + n1
    n3 = n1 + n2
    n1 = n2  # giving the value of n2 to n1 .
    n2 = n3 # updating the value of n2
    count = count + 1

print(f"\nThe average value of this fibonacci series  is {Sum/Number_of_terms}")


# Q8.

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

#a.
union1 = set.union(set1,set2)
intersection = set.intersection(set1,set2)
setaa = union1 - intersection
print(f"The set of elements that are in set1 and set2 but not both is\n{setaa}\n")

#b.

seta = set.intersection(set1,set2)
union1 = set.union(set1,set2)

set4 = union1-seta

set5 = set.intersection(set4,set3)
set6 = set.union(set4,set3)
set7 = set6 - set5
print(f"The set of elements that are in only one of the three sets..set1,set2,set3 is\n{set7}\n")

#c.
set8 = set.intersection(set1,set2)
set9 = set.intersection(set1,set3)
set10 = set.union(set8,set9)
print(f"The set of the elements that are exactly in two of the sets ...set1,set2,set3 is\n{set10}\n")

#d.
set11 = {1,2,3,4,5,6,7,8,9,10}
set12 = set11 - set1
print(f"The set of integers in the range(1-10) that are not in set1 is\n{set12}\n")

#e.
set13 = set.union(set1,set2,set3)
set14 = set11 - set13
print(f"The set of integers in the range(1-10) that are not in set1,set2 and set3 is \n{set14}\n")































































































