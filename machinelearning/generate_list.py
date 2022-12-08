#----------------------------------------------------------------

# The Following Script creates a csv file populated with X amount of people of varying attributes

#import packages
#These are needed for various library functions that are used in the script
import random
import csv
import time

# Initialize a list of attribute names to be used in the list creation 
fields = ['FIRST NAME','LAST NAME','SEX','RACE', 'AGE','HAIR COLOR',  'SEVERITY OF CRIME','VEREDICT'] 
    
# The size variable indicates the amount of people to be generated (more people = larger file size) 
size = input("input amount of people you want to generate\n")
counter = 0

# Initialize the various attributes to lists. These should contain the choices that correspond to each field variable
# These choices represent characteristics of a human excluding their name and gender.
# The frequency of how many options are in each list determine how likely each attribute will be assigned to a person
# For example, attr6 = ["Guilty","Guilty","Guilty","Innocent"] would yield a 75% chance that a generated person would be "Guilty"

attr1 = ["White","Hispanic","Black"]
attr2 = ["Middle Aged","Teenager","Middle Aged","Teenager","Old","Child"]
attr3 = ["Brown","Black"]
attr4 = ["Felony","Infractions","Misdemeanor","Felony"]
attr5 = ["Guilty","Guilty","Guily","Innocent"]


#Creating the file
with open('data.csv', 'w') as f:  
    # The person's name is generated from three text files: females.txt,males.txt,and lastnames.txt
    # These lists contain thousands of random names for the script to choose from
    femaleNames = open('females.txt').read().splitlines()
    maleNames = open('males.txt').read().splitlines() 
    lastNames = open('lastnames.txt').read().splitlines()
    write = csv.writer(f)
    write.writerow(fields)

    #loop for each person
    #This loop will run for each person that needs to be created, 500 people = 500 loops
    while(counter < int(size)):

        #Choose a random Female, Male and Last name
        fname = random.choice(femaleNames)
        mname = random.choice(maleNames)
        lname = random.choice(lastNames)

        #Randomly choose if the generated person is male or female and assign the correct name accordingly
        attr0 = [fname,mname]
        name = random.choice(attr0)
        sex = ""
        if name == fname:
            sex = "Female"
        elif name == mname:
            sex = "Male"

        #Create one row with the generate name and a random attribute from the attribute list
        rows = [ [name, lname,sex,random.choice(attr1), random.choice(attr2), random.choice(attr3),random.choice(attr4),random.choice(attr5)]]   
        write.writerows(rows)
        
        #Indicator which will output a progress message for every 50 humans generated
        if counter % 50 == 0:
            print("Generating " + str(counter) + " Humans")
            time.sleep(0.2)
        counter = counter + 1
    print("Generating " + str(size) + " Humans")    
    print("Humans Successfully Generated!") 
