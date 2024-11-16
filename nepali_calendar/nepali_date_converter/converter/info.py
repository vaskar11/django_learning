import csv
import os
''''this is for the csv part'''
# Function to load CSV into a dictionary like the one requested
def load_bs_years_data(file_path):
    bs_years_data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            year = int(row[0])  # The first column is the year
            months_data = [int(x) for x in row[1:]]  # The rest are the months' data
            bs_years_data[year] = months_data
            #It put in the dictanory as 1997:all the months
    return bs_years_data



# # Get the absolute path of the CSV file in the same directory as this script
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'calendar_bs.csv')

# Path to the CSV file
# file_path = 'converter/calendar_bs.csv'
# Load the CSV data into the desired dictionary format
bs_years_data = load_bs_years_data(file_path)
# print(bs_years_data)



