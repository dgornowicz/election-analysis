# 0. The data we need to retrieve
# 0.1 Add dependencies
import csv
import os

# 0.2 Assign variable to load a file from path
file_to_load = os.path.join('Resources','election_results.csv')

# 0.3 Assign variable to save the file to path
file_to_save = os.path.join('Analysis','election_analysis.txt')

# 0.4 Open election results and read file
with open(file_to_load) as election_data:

    # 0.4.1 Read file object with reader function
    file_reader = csv.reader(election_data)

    # 0.4.2 Read and print header row
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast

# 2. A complete list of conadidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote
