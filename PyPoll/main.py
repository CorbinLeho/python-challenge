import os
import csv

File = ('PyPoll.csv')

Poll = {}

TotalVotes = 0

#gets data File
with open(File, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader)

    for row in csv_reader:
        TotalVotes += 1
        if row[2] in Poll.keys():
            Poll[row[2]] = Poll[row[2]] + 1
        else:
            Poll[row[2]] = 1

Candidates = []
Num_votes = []

for key, value in Poll.items():
    Candidates.append(key)
    Num_votes.append(value)

vote_percent = []
for n in Num_votes:
    vote_percent.append(round(n/TotalVotes*100, 1))

# zips Candidtes, Num_votes, vote_percent into tuples
clean_data = list(zip(Candidates, Num_votes, vote_percent))

winner_list = []

for name in clean_data:
    if max(Num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

output_file = os.path.join('PyPollSolved.txt')

with open(output_file, 'w') as f:
    f.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(TotalVotes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        f.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    f.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output_file, 'r') as readfile:
    print(readfile.read())