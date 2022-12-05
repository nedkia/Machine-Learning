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

![image](https://user-images.githubusercontent.com/78882341/205675405-7ad492d6-7528-4be2-ba79-4b5c9207a2dc.png)

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

_______________________________________________________________________________________________

Final output messages...

![image](https://user-images.githubusercontent.com/78882341/205677539-1f038eeb-00f3-44a7-9204-45b2db8e2f22.png)
