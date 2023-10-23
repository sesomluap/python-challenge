#import libraries
import os
import csv

#join path
PyBank = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(PyBank, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    #skip header
    print(f"Header: {csvheader}")

    #assign list variables
    profit = []
    months = []

    #read through each row of data below the header
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    #find the total months in the dataset
    total_months = len(months)

    #find revenue change
    revenue_change = []
    
    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))

    #calculate rounded average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average, 2)

    #find greatest revenue increase & decrease
    greatest_increase =  max(revenue_change)
    greatest_decrease = min(revenue_change)

    #Find the corresponding dates for the greatest increase and decrease
    date_greatest_increase = months[revenue_change.index(greatest_increase) + 1]
    date_greatest_decrease = months[revenue_change.index(greatest_decrease) + 1]


    #print the results
    print("Financial Analysis")

    print("----------------------------")

    print("Total Months: " + str(total_months))
    
    print("Total: " + "$" + str(sum(profit)))

    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + date_greatest_increase + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + date_greatest_decrease + " " + "$" + str(greatest_decrease))


    #output to a text file
    output = open("analysis/output.txt", "w")
    
    output.write("Financial Analysis\n")

    output.write("----------------------------\n")

    output.write("Total Months: " + str(total_months) + "\n")
    
    output.write("Total: " + "$" + str(sum(profit)) + "\n")

    output.write("Average Change: " + "$" + str(revenue_average) + "\n")

    output.write("Greatest Increase in Profits: " + date_greatest_increase + " " + "$" + str(greatest_increase) + "\n")

    output.write("Greatest Decrease in Profits: " + date_greatest_decrease + " " + "$" + str(greatest_decrease) + "\n")