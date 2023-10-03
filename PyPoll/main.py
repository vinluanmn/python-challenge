import os
import csv

#find and load the csv file
poll_csv = os.path.join("Resources","election_data.csv")

#assign total votes variable
total_votes = 0
#create candidates list
candidates = []
#create candidates and votes dictionary
candidate_votes = {}
# assign variable for winning_candidate and initiate vote count
winning_candidate = ""
winning_count = 0

#create reader to read the csv
with open(poll_csv) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #use next to bypass header
    csvHeader = next(csvReader)
    #loop through rows of the csv
    for row in csvReader:
        #each row is a vote. add 1 to total_vote as reader continues through each row
        total_votes += 1
        #assign candidate to index 2
        candidate = row[2]

        #create loop to .append canditate to candidate list
        if candidate not in candidates:
            candidates.append(candidate)
            #initiate candidate vote count for each candidate in list
            candidate_votes[candidate] = 0
        #for each candidate in list, and 1 to each iteration in csv
        candidate_votes[candidate] += 1

#print election total_vote results
print("Election Results\n")
print("--------------------------------\n")
print(f"Total votes: {total_votes}\n")
print("--------------------------------\n")

#create output to write in created text file
analysis_output = ""
analysis_output += ("Election Results\n")
analysis_output += ("--------------------------------\n")
analysis_output += (f"Total votes: {total_votes}\n")
analysis_output += ("--------------------------------\n")

#create a loop to determine percentage of votes for each candidate
for candidate in candidates: 
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    #print candidate their percentage and total number of votes
    print(f"{candidate}: {percentage:.3f}% ({votes})\n")
    #create an output to write as part of the text file
    analysis_output += (f"{candidate}: {percentage:.3f}% ({votes})\n")
    #create conditional if votes is greater than winning_count to
    #determin the candiate from the list with the most votes
    #assign winning_candidate
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate
#print winning results
print("--------------------------------\n")
print(f"Winner: {winning_candidate}\n")
print("--------------------------------\n")
#create output to print in text file
analysis_output += ("--------------------------------\n")
analysis_output += (f"Winner: {winning_candidate}\n")
analysis_output += ("--------------------------------\n")

#create path for text file
create_file = os.path.join("analysis", "analysis.txt")
#write text file upon open
with open(create_file, 'w') as file:
    file.write(analysis_output)

#create conditional statement to verify file was created
if os.path.exists(create_file):
    print(f"File has been successfully written as {create_file}")
else:
    print("Error: The file was not created or written.")