"""
Docstring for CST8002-PracticalProject01.main

Author: Timothy Jacot
Course code: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Due Date: January 23rd 2026

"""

#Main class main.py

import csv
from record import Record

def main():
    print("Full Name: Timothy Jacot\n")


    records = []    # Read the CSV file and create Record objects
    file_path = "CST8002-PracticalProject01/pacific_rim_npr_coastalmarine_kelp_density_2013-2016_data.csv"
    
    try:

        with open(file_path, mode ='r', newline='', encoding='cp1252')as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip header row

            #reading all records in csv file dynamically    
            for row in csv_reader:
                if len(row) < 7:    
                    continue  # Skip rows that don't have enough columns
                try:
                    record = Record(
                        site_id=row[0],
                        year=int(row[1]),
                        diver_id=row[2],
                        transect=row[3],
                        transect_distance=float(row[4]),
                        species_code=row[5],
                        count=int(row[6])
                    )
                    records.append(record)
                    if len(records) >= 5:
                        break
                # Limit to first 5 records for performance
                except ValueError as ve:
                    # Skip rows with bad numeric data
                    if 'Année' not in str(row):
                        print(f"Skipping row due to conversion error: {row} -> {ve}")
                    continue
    except FileNotFoundError:
        print(f"Error: The file '{csvfile}' was not found.")
        return
    except Exception as e:
        print(f"Error occured. Details: {e}")
        return

    # Looping through the list to display each record
    print("Records Loaded:")
    for rec in records:
        print(rec) 

    print(f"\nTotal Records Loaded: {len(records)}")

if __name__ == "__main__":
    main()