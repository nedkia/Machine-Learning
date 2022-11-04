import csv
import pandas as pd
  
# read CSV file
results = pd.read_csv('data')
size = len(results)
filename ="data"
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
while i < size:
    if lst[i]['Race'] == "Black" and (lst[i]['Severity of Crime'] == "Felony" or "Misdemeanor"):
        ##print("found AA")
        bcount = bcount + 1
    if lst[i]['Race'] == "White" and (lst[i]['Severity of Crime'] == "Felony" or "Misdemeanor"):
        ##print("found AA")
        wcount = wcount + 1
    if lst[i]['Race'] == "Hispanic" and (lst[i]['Severity of Crime'] == "Felony" or "Misdemeanor"):
        ##print("found AA")
        hcount = hcount + 1
    
    i = i + 1
print("Amount of African Americans with a severe crime:",bcount)
print("Amount of White Americans with a sever crime:",wcount)
print("Amount of Hispanics with a severe crime: ",hcount)

freq_race = ""
racecount = float(0)
if bcount >= wcount and bcount >= hcount:
    print("bcount is the greatest")
    racecount = float(bcount/size) * 100
    freq_race = "Black"
if wcount >= bcount and wcount >= hcount:
    print("wcount is the greatest")
    freq_race = "Hispanic"
    racecount = float(hcount/size) * 100
if hcount >= wcount and hcount >= bcount:
    print("hcount is the greatest")
    racecount = float(wcount/size) * 100
    freq_race = "White"


print("Based on our machine learning analysis "+ freq_race + " is the highest likely race to commit a severe crime with a "+str(racecount)+ " percent chance")
