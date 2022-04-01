import os
import csv



csvpath= os.path.join('..','Desktop','python-challenge','PyBank','Resources','budget_data.csv')

Date = []
P_or_L = []


Date_Total = int
PL_Changes = int
G_increase = int
G_decrease = int
GI = 0 
GD = 1
GI_Date = ''
GD_Date = ''

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Add date data and P/L
        Date.append(row[0])
        P_or_L.append(int(row[1]))

# gives total amount
for i in range(0, len(P_or_L)):
    Total_amount = sum(P_or_L)


#prints date total
Date_Total = len(Date)

#Gives the greatest Increase
for i in range(0, len(P_or_L)):
    if P_or_L[i] > GI:
        GI = P_or_L[i]
        GI_Date = Date[i]
    
#Gives the greatest Decrease
for i in range(0, len(P_or_L)):
    if P_or_L[i] < GD:
        GD = P_or_L[i]
        GD_Date = Date[i]


#output
print('Financial Analysis!')
print('______________________________________')

print(f'Total Months: {str(Date_Total)}')
print(f'Total ${int(Total_amount)}')
print(f'Average Change: ${Total_amount/len(P_or_L)}')
print(f'Greatest Increase in profits: {GI_Date} (${GI})')
print(f'Greatest Decrease in Profits: {GD_Date} (${GD})')

output_file = os.path.join('..','Desktop','python-challenge','PyBank','analysis.csv')

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow('Financial Analysis!')
    writer.writerow('______________________________________')
    writer.writerow(f'Total Months: {str(Date_Total)}')
    writer.writerow(f'Total ${int(Total_amount)}')
    writer.writerow(f'Average Change: ${Total_amount/len(P_or_L)}')
    writer.writerow(f'Greatest Increase in profits: {GI_Date} (${GI})')
    writer.writerow(f'Greatest Decrease in Profits: {GD_Date} (${GD})')