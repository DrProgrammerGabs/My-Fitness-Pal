import time
print ("Body Mass Index (BMI Calculator) Version 1.0")
import time
time.sleep(2)
print ("Created by Dr. Marie Gabrielle Laguna-Bedia of SCRIPTUS WEB DEVELOPMENT AND CONSULTING, Iloilo, Philippines")
import time
time.sleep(2)
print ("Copyright 2016. ALL RIGHTS RESERVED")
import time
time.sleep(2)
print ("Hello! This is a BODY MASS INDEX (BMI) calculator. This tool will tell you whether you need to gain weight, lose weight or maintain your current weight.")
import time
time.sleep(2)
print ("Please fill up the required information")                   #greetings
name = input ("Name: ")                                    #where the user inputs the name                                                 
age = input ("Age: ")                                      #where the user inputs the age
print ("What is your height in meters? To get your height in meters, multiply your height inches with 0.0254")                   #question
height = float (input ("Height: "))                                #where the user inputs the height
print ("What is your weight in kilograms?")                #question
weight = int (input ("Weight: "))                                #where the user inputs the weight
print("I will now solve for your body mass index for you to find out if you are underweight, of normal weight, overweight or obese. Please wait....") #remarks
import time
time.sleep(3)                                              # delays for 5 seconds
print ("Here is your BMI result")                          #here is your BMI result, says
import time                                                 
time.sleep(2)                                              #delays for 5 seconds
BMI = weight/(height*height)
print ("Here is my interpretation:")                       # says interpretation

if BMI <= 18.5:
    print ("You are underweight. You should eat more to gain weight") #underweight    
elif BMI == 18.5-24.9:
    print ("You are of normal weight. Maintain your current weight")  #normal    
elif BMI == 25-29.9:
    print ("You are overweight. You should lose some weight through proper diet and exercise")  #overweight    
else:
    BMI >= 30
    print ("You are obese. See your doctor on how to lose weight effectively")  #obese
    
import time
time.sleep(5)                                               #delays for 5 seconds
print ("Thanks for using this app! Always strive to be healthy!")    #thank you
import sys
sys.exit()                                                 #exit file



    
