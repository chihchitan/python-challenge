import os
import csv

csvpath = os.path.join('election_data.csv')

candidate_votes = {"Correy": 0, "Khan": 0, "Li":0, "O'Tooley": 0}
total_votes = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None) 
    for row in csvreader:
        vote = row[2]
        candidate_votes[vote] +=1
    total_votes = sum(candidate_votes.values())
        
    max_votes = 0
    winner = ""
    for candidate_name, votes in candidate_votes.items():
        if max_votes < votes:
            max_votes = votes
            winner = candidate_name

#summary
print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------------")
for candidate_name, votes in candidate_votes.items():
    percent = (votes / total_votes) * 100
    print("{}: {:.3f}%, ({})".format(candidate_name, percent, votes))
print("-----------------------------------")
print(f"Winner: {winner}")

#output txt
outputfile = "election_results.txt"
with open(outputfile, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-----------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("-----------------------------------")
    txt_file.write("\n")
    for candidate_name, votes in candidate_votes.items():
        percent = (votes / total_votes) * 100
        txt_file.write("{}: {:.3f}%, ({})".format(candidate_name, percent, votes))
        txt_file.write("\n")
    txt_file.write("-----------------------------------")
    txt_file.write("\n")
    txt_file.write(f"Winner: {winner}")