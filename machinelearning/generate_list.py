import random
import csv
import time

# field names 
fields = ['FIRST NAME','LAST NAME','SEX','RACE', 'AGE','HAIR COLOR',  'SEVERITY OF CRIME','VEREDICT'] 
    
# data rows of csv file 
size = input("input amount of people you want to generate\n")
counter = 0

attr1 = ["Man","Man"]
attr3 = ["Middle Aged","Teenager","Middle Aged","Teenager","Old","Child"]
attr4 = ["Brown","Blonde","Black"]
attr2 = ["Black","Hispanic","Black"]
attr5 = ["Felony","Infractions","Petty"]
attr6 = ["Guilty","Guilty"]

with open('data.csv', 'w') as f:  
    femaleNames = open('females.txt').read().splitlines()
    maleNames = open('males.txt').read().splitlines() 
    lastNames = open('lastnames.txt').read().splitlines()
    write = csv.writer(f)
    write.writerow(fields)
    while(counter < int(size)):
        fname = random.choice(femaleNames)
        mname = random.choice(maleNames)
        lname = random.choice(lastNames)
        attr0 = [fname,mname]
        name = random.choice(attr0)
        sex = ""
        if name == fname:
            sex = "Female"
        elif name == mname:
            sex = "Male"
        rows = [ [name, lname,sex,random.choice(attr2), random.choice(attr3), random.choice(attr4),random.choice(attr5),random.choice(attr6)]]   
        write.writerows(rows)
        if counter % 50 == 0:
            print("Generating " + str(counter) + " Humans")
            time.sleep(0.2)
        counter = counter + 1
    print("Generating " + str(size) + " Humans")    
    print("Humans Successfully Generated!")
