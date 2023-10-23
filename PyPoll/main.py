#import libraries
import os
import csv

#join path
PyPoll = os.path.join("Resources", "election_data.csv")
                      
#open and read csv
with open(PyPoll, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    #skip  header
    print(f"Header: {csvheader}")

    #assign list variables
    candidates = []
    num_votes = []
    percent_votes = []

    #set vote counter to 0
    total_votes = 0

    #make our vote counting loop
    for row in csvreader:
        #count total votes
        total_votes += 1

        #identify new candidates and add them to the list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        #tally candidate vote counts
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    #convert vote counts into rounded percentages
    for votes in num_votes:
        percentage = (votes/total_votes)*100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    #identify the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#display election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

#output election results to txt
output = open("analysis/output.txt", "w")
output.write("Election Results" + "\n")
output.write("-------------------------" + "\n")
output.write(f"Total Votes: {str(total_votes)}" + "\n")
output.write("-------------------------" + "\n")
for i in range(len(candidates)):
    output.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})" + "\n")
output.write("-------------------------" + "\n")
output.write(f"Winner: {winning_candidate}" + "\n")
output.write("-------------------------" + "\n")