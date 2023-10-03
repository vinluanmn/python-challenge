import os
import csv

poll_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(poll_csv) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csvHeader = next(csvReader)
    for row in csvReader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1

print("Election Results\n")
print("--------------------------------\n")
print(f"Total votes: {total_votes}\n")
print("--------------------------------\n")
analysis_output = ""
analysis_output += ("Election Results\n")
analysis_output += ("--------------------------------\n")
analysis_output += (f"Total votes: {total_votes}\n")
analysis_output += ("--------------------------------\n")

for candidate in candidates: 
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})\n")
    analysis_output += (f"{candidate}: {percentage:.3f}% ({votes})\n")
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate
print("--------------------------------\n")
print(f"Winner: {winning_candidate}\n")
print("--------------------------------\n")

analysis_output += ("--------------------------------\n")
analysis_output += (f"Winner: {winning_candidate}\n")
analysis_output += ("--------------------------------\n")

create_file = os.path.join("analysis", "analysis.txt")
with open(create_file, 'w') as file:
    file.write(analysis_output)

if os.path.exists(create_file):
    print(f"File has been successfully written as {create_file}")
else:
    print("Error: The file was not created or written.")