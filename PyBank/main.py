import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    budgetdatafile = csv.reader(csvfile, delimiter=',')

     # skip the header

    next(budgetdatafile)
#in order to find the average difference for each month, previous value needs to start with a value. So 
#total months and sumprofitlosses need to have starting values which is one.
    totalmonths = 1
    sumprofitlosses = 0
    greatestincrease = 0
    greatestdecrease = 0
    monthlychange = []
    row = next(budgetdatafile)
    previousvalue = int(row[1])
    sumprofitlosses = sumprofitlosses  + int(row[1])

    for row in budgetdatafile:
        totalmonths = totalmonths + 1
        # converting the value of row 1 to a number
        sumprofitlosses = sumprofitlosses  + int(row[1])

        #to find the average of the change in the profit/losses column we need to subtract the value of the current profit loss
        #from the previous value and store it.  To store it we have to create a variable to hold it in memory
        changeinprofitloss = int(row[1]) - previousvalue
        monthlychange.append(changeinprofitloss)
        previousvalue = int(row[1])


        if int(row[1]) > greatestincrease:
            greatestincreasemonth = row[0]
            greatestincrease = int(row[1])
        
        if int(row[1]) < greatestdecrease:
            greatestdecreasemonth = row[0]
            greatestdecrease = int(row[1])
    averagechange = sum(monthlychange) / len(monthlychange)
    
    #find max value in monthlychange
    greatestchange = max(monthlychange)
    smallestchange = min(monthlychange)    

    #print to screen

    print(f"Financial Analysis")
    print(f" -------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${sumprofitlosses}")
    print(f"Average Change: ${averagechange:.2f}")
    print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestchange})")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${smallestchange})")

  # Write results to a file
    resultsfile = os.path.join("analysis", "pollingresults.txt")
    with open(resultsfile, "w",) as textfile:
        textfile.write(f"Financial Analysis\n")
        textfile.write(f" -------------------------\n")
        textfile.write(f"Total Months: {totalmonths}\n")
        textfile.write(f"Total: ${sumprofitlosses}\n")
        textfile.write(f"Average Change: ${averagechange:.2f}\n")
        textfile.write(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestchange})\n")
        textfile.write(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${smallestchange})\n")