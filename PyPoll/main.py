import os
import csv


csvpath= os.path.join('..','Desktop','python-challenge','PyPoll','Resources','election_data.csv')


ch_total = 0
ch_per = 0
di_total = 0
di_per = 0
ra_total = 0
ra_per = 0
total_votes = 0
winner = ''

Voter_ID = []
County = []
Candidate = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Add data to arrays
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

for i in range(0, len(Voter_ID)):
    if Candidate[i] == "Charles Casper Stockham":
        ch_total = ch_total + 1
    elif Candidate[i] == "Diana DeGette":
        di_total = di_total +1
    elif Candidate[i] == "Raymon Anthony Doane":
        ra_total = ra_total + 1

total_votes = ch_total + di_total + ra_total

ch_per = round((ch_total/total_votes)*100,2)
di_per = round((di_total/total_votes)*100, 2)
ra_per = round((ra_total/total_votes)*100,2)

if ch_total > di_total and ra_total:
    winner = 'Charles Casper Stockham'
elif di_total > ch_total and ra_total:
    winner = 'Diana DeGette'
elif ra_total > di_total and ch_total:
    winner = 'Raymon Anthony Doane'


print('Election Results!')
print('______________________________')
print(f'Total Votes: {total_votes}')
print('______________________________')
print(f'Charles Casper Stockham: {ch_per}% ({ch_total})')
print(f'Diana DeGette: {di_per}% ({di_total})')
print(f'Raymon Anthony Doane: {ra_per}% ({ra_total})')
print('_______________________________')
print(f'Winner: {winner}')
print('_______________________________')