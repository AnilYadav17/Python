'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:
* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.
Input:
Enter temperature: 38

Output:
Weather Condition: Hot'''

temp = int(input("Enter Temperature:"))

if temp>0:
    if temp>=21:
        if temp>30:
            print("Temperature Status : HOT")
        else:
            print("Temperature Status : WARM")
    else:
        print("Temperature Status : COLD")
else:
    print("Temperature Status : FREEZING")
