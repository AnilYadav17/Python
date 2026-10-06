'''A group of friends went to a restaurant. The restaurant adds GST and 
service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''


bill_amount,gst,service_charge,friends = map(float,input("Enter total bill Amount , GST , Service Charge ,and Number of Friends: ").split())
final_bill = bill_amount+bill_amount*gst/100+bill_amount*service_charge/100
print("Final Bill: ",final_bill,"\nEach Person Pays :",final_bill/friends)
