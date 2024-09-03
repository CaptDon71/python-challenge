#!/usr/bin/env python
# coding: utf-8

# In[9]:


# PyPoll Challenge
import os
import csv


# In[11]:


# Determine files to read and write 
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_write = os.path.join("analysis", "election_analysis.txt")


# In[13]:


# Declare variables
candidates = {}
total_votes = 0
winner = ""


# In[15]:


# Read csv and convert into lists of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read header
    header = next(reader)
    # With remaining rows, create a dictionary list 
    # Parse rows and count votes
    for row in reader:
        candidate_name = row[2]  # Get the candidate's name from each row
        if candidate_name in candidates:
            candidates[candidate_name] += 1  # Increment vote count if the candidate is already in dictionary
        else:
            candidates[candidate_name] = 1   # Initialize vote count if the candidate is not in dictionary

# Calculate total votes
total_votes = sum(candidates.values())

# Determine the winner
winner = max(candidates, key=candidates.get)


# In[17]:


# Create a reuseable multiline string variable
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Calculate and add each candidate's percentage and vote count
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"

results += "-------------------------\n"
results += f"Winner: {winner}\n"
results += "-------------------------\n"

# Print the results to the terminal
print(results)

# Export the results to a text file
with open(file_to_write, "w") as file:
    file.write(results)


# In[ ]:




