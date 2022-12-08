import csv
import pandas as pd

# read CSV file
results = pd.read_csv('data.csv')
size = len(results)
filename ="data.csv"
lst = [None] * size
count = 0
with open(filename, 'r') as file:
  for line in csv.DictReader(file):
    lst[count] = line
    count = count + 1
    x = line
i = 0
bcount = 0
hcount = 0
wcount = 0

male_count = 0
female_count = 0
while i < size:
    if lst[i]['RACE'] == "Black" and (lst[i]['SEVERITY OF CRIME'] == "Felony" or "Misdemeanor") and lst[i]['VEREDICT'] == "Guilty":
        bcount = bcount + 1
        if lst[i]['SEX'] == "Male":
            male_count = male_count + 1
        else:
            female_count = female_count + 1
    if lst[i]['RACE'] == "White" and (lst[i]['SEVERITY OF CRIME'] == "Felony" or "Misdemeanor") and lst[i]['VEREDICT'] == "Guilty":
        wcount = wcount + 1
        if lst[i]['SEX'] == "Male":
            male_count = male_count + 1
        else:
            female_count = female_count + 1
    if lst[i]['RACE'] == "Hispanic" and (lst[i]['SEVERITY OF CRIME'] == "Felony" or "Misdemeanor") and lst[i]['VEREDICT'] == "Guilty":
        hcount = hcount + 1
        if lst[i]['SEX'] == "Male":
            male_count = male_count + 1
        else:
            female_count = female_count + 1

    
    
    
    i = i + 1

freq_race = ""
racecount = float(0)

racecount1 = float(bcount/size) * 100
freq_race1 = "Black"

freq_race2 = "Hispanic"
racecount2 = float(hcount/size) * 100

racecount3 = float(wcount/size) * 100
freq_race3 = "White"

if bcount >= wcount and bcount >= hcount: #bcount is the greatest
    freq_race = freq_race1
    racecount = racecount1
if hcount >= wcount and hcount >= bcount: #hcount is the greatest
    freq_race = freq_race2
    racecount = racecount2
if wcount >= bcount and wcount >= hcount: #wcount is the greatest
    freq_race = freq_race3
    racecount = racecount3




print("Generating Results...")
print("Amount of African Americans with a severe crime:",bcount, "with a ", racecount1 ," % chance")
print("Amount of Hispanic Americans with a sever crime:",hcount, "with a ", racecount2 ," % chance")
print("Amount of White Americans with a severe crime: ",wcount, "with a ", racecount3 ," % chance")
print("Based on our machine learning analysis "+ freq_race + " Americans have the greated likelihood of commiting a severe crime with a "+str(racecount)+ " percent chance")
print("Likelihood of a male being found guilty: ", male_count, " with a ", float(male_count/size)*100 ," % chance")
print("Likelihood of a female being found guilty: ", female_count,"with a ", float(female_count/size)*100 , " % chance")

if(male_count > female_count):
    print("Males have a higher chance of being found guilty")
else:
    print("females have a higher chance of being found guilty")
