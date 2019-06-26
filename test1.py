# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")

    # database connection
    db = conn.stocks
    company = input("Enter the company name")  # Enter which company's data you want to know
    print(company)
    data1 = db.day1.find({'SYMBOL': company})
    for d1 in data1:
        print(d1)  # displays the day1's data in the form of list
    data2 = db.day2.find({'SYMBOL': company})
    for d2 in data2:
        print(d2)     # displays the day2's data in the form of list
    data3 = db.day3.find({'SYMBOL': company})
    for d3 in data3:
        print(d3)    # displays the day3's data in the form of list
    data4 = db.day4.find({"SYMBOL": company})
    for d4 in data4:
        print(d4)   # displays the day4's data in the form of list
    data5 = db.day5.find({"SYMBOL": company})
    for d5 in data5:
        print(d5)  # displays the day5's data in the form of list
except:
    print("Could not connect to MongoDB")





