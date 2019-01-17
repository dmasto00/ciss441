import csv
import json

"""
who: daaron maston
when: 1.16.2019
what: demo of a1 assignment
"""

nfl_data = []      # this is to collect data for printing at the very end. 
nfl_total_count = 0    # for counting the rows of data
with open('nfl_stadiums.csv', 'r') as csvfile:

    # parse csv file pointer into nfl_stream
    nfl_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    # interate over nfl_stream to process. 
    for nfl_data_row in nfl_stream:
        nfl_total_count += 1

        nfl_stadium_name = nfl_data_row['stadium_name']
        nfl_stadium_location = nfl_data_row['stadium_location']
        nfl_stadium_open = nfl_data_row['stadium_open']

        # only show the first 20 rows. 
        if nfl_total_count <= 20:
            print(nfl_total_count, nfl_stadium_name ,nfl_stadium_location, nfl_stadium_open)
            nfl_data.append({nfl_total_count: [nfl_stadium_name ,nfl_stadium_location, nfl_stadium_open]
                })

            
print("I found " + str(nfl_total_count) + " nfls.")
print("I am all done processing data!!!")

print(json.dumps(nfl_data))
