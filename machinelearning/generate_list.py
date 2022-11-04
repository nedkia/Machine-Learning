import random
import csv
  
# field names 
fields = ['First Name','Last Name','Sex','Race', 'Age','Hair Color', 'Severity of Crime','Veredict'] 
    
# data rows of csv file 
size = input("input amount of people you want to generate\n")
counter = 0

attr1 = ["Man","Women","Man"]
attr3 = ["Middle Aged","Teenager","Middle Aged","Teenager","Old","Child"]
attr4 = ["Brown","Brown","Blonde","Blonde","Redhead"]
attr2 = ["Black","Hispanic","White"]
attr5 = ["Petty","Infractions","Misdemeanor","Felony"]
attr6 = ["Guilty","Innocent"]

with open('data', 'w') as f:  
    femaleNames = open('females.txt').read().splitlines()
    maleNames = open('males.txt').read().splitlines() 
    lastNames = open('lastnames.txt').read().splitlines()
    write = csv.writer(f)
    write.writerow(fields)
    while(counter < int(size)):
        fname =random.choice(femaleNames)
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
        counter = counter + 1

