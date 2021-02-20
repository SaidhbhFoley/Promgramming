#This program reads students percentage and prints out the corresponding grade
#Author: Saidhbh Foley

percentage = float (input ("Enter the percentage:"))
#print (Percentage)

if (percentage < 0) or (percentage > 100):
    print ("Please enter a number between 0 and 100")
elif percentage < 39.5: 
 print ("Fail")
elif percentage < 49.5 or percentage :
 print ("Pass")
elif percentage < 59.5: 
 print ("Merit1")
elif percentage < 69.5: 
 print ("Merit2")
else: 
 print ("Distinction")
