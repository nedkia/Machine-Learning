# Machine-Learning


Purpose: The purpose of this project is to understand how machine learning algorithms can be biased using a simple python simulation.


Before we understand machine learning we must first understand the basics of a machine. Machines with intelligence are some form of hardware that is given instructions so that it is able to perform actions based on input or scenarios that have been preprogrammed. At the lowest computer level, the computer is only able to decipher if a signal has been turned on or off (usually using binary numbers in order to do so). On top of this basic signal level, machine code is implemented which is rather complicated and is very literal with how the machine manages memory. Most modern day programming languages are built to automatically compile into machine code which then is translated into turning on the correct signals at the hardware level.

This means that assuming the computer is built correctly, it is simply a machine that can execute intelligence based on what the programmer decides to do. If the machine is capable of carrying out what the programmer tells it to do, then we can assume that as long as no outside sources interfere, a computer should always successfully carry out the programmer's instruction.

When a programmer makes a machine learning algorithm, they must specifically build the intelligence and tell the machine how to learn. For example if they want to analyze data, they must tell the machine to plot points or perform other math functions based on the data that is provided. The machine does not actually understand that it is creating a graph, it is simply executing instructions that a programmer made. 

With current technology, a machine is only able to learn based on data it is provided. This data can be provided in many ways, such as by feeding the machine large files or by using an Input/Output (I/O) device to gather data that is then fed into the machine. The machine is then able to draw conlcusions or "learn" based on two primary things: The instructions or algorithm that the programmer implemented for "learning" as well as the data provided to this algorithm that influences how intepretations are made.

Therefore most machine learning biases can be interpreted in two ways: Either the algorithm was designed to exclude or "learn" in a biased way or the data that is being provided isn't accurate or inclusive enough for the machine to properly draw conclusions from. For example if someone programs a machine to find the best way to build a house, but the data being analyzed only contains instructions on how to build apartments, the machine will learn the best way to build an apartment and claim that it is the best way to build a house because the programmer did not feed the machine data on all kinds of houses. 

Biases like this happen all the time and they are usually not done with malicious intent. Programmers focus more on creating a working machine and may not take into account that this machine may be unethical or biased. 

For this experiment I will simulate an algorithm which analyzes crime rates and the human features that are associated with different levels of crime. 

I will first create a python script that reads in various user attributes as well as the severity of the crime that they committed and if they were found guilty or innocent of the crime. After the script is done analysing the data it will draw conclusions and make predictions on which attributes of a person is correlated to more crime. The purpose of this simulation is to feed the algorithm various data sets and examine how the algorithm learns differently based on the data it is being fed. I plan to feed the algorithm various kinds of data with different levels of biases. 

In the technical industry, real life algorithms use data like this to make real world decisions which means that its very important that we feed the algorithms data that is inclusive and nonbiased. To create an accurate simulation, I needed multiple data sets of various sizes and attributes. These data sets will be purposelly manipulated to be generated with some biases included in them. Then we will run the analysis script on the generated data to similuate a machine learning algorithm being fed data. Afterwards we will view the conclusion that the machine was able to come to after reading in each data set.

In order to create a lot of varying data in an efficient manner, I created the "generate_list.py file". This allows me to dynamically create a list of any size while also making it very easy to modify the attributes and data values that are generated.

_______________________________________________________________________________________________

Creating the "generate_list.py" file

The Following Script creates a csv file populated with X amount of people of varying attributes

First we import packages as these are needed for various library functions that are used in the script

Then we Initialize a list of attribute names to be used in the list creation 
The size variable indicates the amount of people to be generated (more people = larger file size)

![image](https://user-images.githubusercontent.com/78882341/205674761-8698d6a5-b7fe-4147-bee2-58f27c95481a.png)


Initialize the various attributes to lists. These should contain the choices that correspond to each field variable
These choices represent characteristics of a human excluding their name and gender.
The frequency of how many options are in each list determine how likely each attribute will be assigned to a person
For example, attr6 = ["Guilty","Guilty","Guilty","Innocent"] would yield a 75% chance that a generated person would be "Guilty"

![image](https://user-images.githubusercontent.com/78882341/206538577-6f2dfe22-1f6d-4211-a234-fb3a33ac4249.png)


Creating the file...

The person's name is generated from three text files: females.txt,males.txt,and lastnames.txt.
These lists contain thousands of random names for the script to choose from.

![image](https://user-images.githubusercontent.com/78882341/205675960-f989678c-104c-4cb2-855f-2fe1014ba06a.png)

This loop will run for each person that needs to be created, 500 people = 500 loops

![image](https://user-images.githubusercontent.com/78882341/205676353-92135882-4903-4c76-839d-2915c71ac831.png)


Choose a random Female, Male and Last name

![image](https://user-images.githubusercontent.com/78882341/205676506-080a7e06-b79e-47fc-a07e-598993282bc9.png)

Randomly choose if the generated person is male or female and assign the correct name accordingly

![image](https://user-images.githubusercontent.com/78882341/205676614-59e5cb9b-2e51-4d9b-a48b-4541d74dac84.png)

Create one row with the generated name and a random attribute from the attribute list. This is essentially piecing together
the attributes and creating a single "human"

![image](https://user-images.githubusercontent.com/78882341/205677223-bd4c6b02-6071-4635-80b1-3db4808f5fc1.png)

Indicator which will output a progress message for every 50 humans generated

![image](https://user-images.githubusercontent.com/78882341/205677410-6a3a953d-c94d-427c-a7ee-4929deaa26af.png)

Final output messages...

![image](https://user-images.githubusercontent.com/78882341/205677539-1f038eeb-00f3-44a7-9204-45b2db8e2f22.png)


Now "data.csv" is generated in the same directory that generate_list.py is located in.
_______________________________________________________________________________________________

Creating the "analysis.py" file

First we import packages as these are needed for various library functions that are used in the script

![image](https://user-images.githubusercontent.com/78882341/205706410-781c6b40-d9e1-4105-a92b-eb52768fc5bb.png)

Next, we read in the data file generated by generate_list.py

We store the data into a Dictionary, with each row being an individual human generated and each column indicates an attribute.

![image](https://user-images.githubusercontent.com/78882341/205706510-5fe9559f-0b0c-40c4-9e63-d093b290109e.png)



Creating the Algorithm...

This Algorithm first iterates through the data that was generated and populated into a list.

It then analyzes each index of the list which is correlated to a single human and there associated attributes.

We record each race and then determine if they were found guilty or not. After the veredict is determined we also record
the sex of the person and record it in order to generate our results.





![image](https://user-images.githubusercontent.com/78882341/206539593-3f2f0f5b-b3b7-47a5-b0d5-63eb5367d8c3.png)


More analysis...


![image](https://user-images.githubusercontent.com/78882341/206747302-7228789a-f429-4d63-b4f7-8524cfa4d076.png)





Sample Output #1 (relatively nonbiased data) 


Atrributes

![image](https://user-images.githubusercontent.com/78882341/206750913-cff96e62-c8c7-4041-ae1e-50f4a2a65d5d.png)


Sample Size: 1000


![image](https://user-images.githubusercontent.com/78882341/206748450-8f318767-ba9a-40d8-b07e-aab674e25f0c.png)

Analysis results:

![image](https://user-images.githubusercontent.com/78882341/206748596-adb32362-3a8b-44aa-8c69-70a287908f97.png)


Running the same attribute data with a sample size of 5 gives different results


![image](https://user-images.githubusercontent.com/78882341/206752575-5d5e57bc-c62c-4715-b128-f9d4949c12be.png)


A sample size of 20,000 also gives different results with the same attribute data

![image](https://user-images.githubusercontent.com/78882341/206753758-8e53432c-b25d-4794-836c-4f593412a990.png)


![image](https://user-images.githubusercontent.com/78882341/206753617-2e11c824-67bb-4bd4-be99-65f3178bb3c2.png)


This analysis shows that the data sample size is important when trying to make accurate judgements. More data = More accuracy.


Sample output #2 Hispanic Bias

![image](https://user-images.githubusercontent.com/78882341/206768656-1a7ecb63-238d-4d87-bba0-4d4e291424bc.png)

This sample output of 5000 people shows that by tweaking the data being fed into the machine learning algorithm, we can drastically change the results.

![image](https://user-images.githubusercontent.com/78882341/206769131-aa4d1d56-10f8-4214-b69d-2df53e50627f.png)


Sample output #3 Female bias 

The same works by manipulating the gender variable

Count: 5000

![image](https://user-images.githubusercontent.com/78882341/206769374-14c5a56d-36be-4933-8f7c-4a46abfd0060.png)

![image](https://user-images.githubusercontent.com/78882341/206772234-669dc3d4-56ae-4179-9fcb-18c54dc75be3.png)




Results/Open Source Policy

These scripts show how a machine learning algorithm can have drastically different results based on the data and algorithm it uses. Although this was a simple simulation, real world examples tend to mimic similar issues with there biases in algorithms. We were also able to see that the sample size of data also changed the machine learning outcome, which is important to understand beceause if someone is designing software for the public, they need to take into account millions of people and not just a couple thousand.

This entire project was created to research bias and allow non technical people to understand how bias in machine learning works. Anyone is allowed to expand upon this project as long as they continue to abide by open source policies and keep it open source.
