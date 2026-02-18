"""
Docstring for persistencelayer.record_repo

Author: Timothy Jacot
Course: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Description: Handling all file I/O operations for Record objects.

"""


import csv
import uuid
from model.record import Record

class RecordRepository:
    """
    Docstring for RecordRepository
    Class RecordRepository handles loading and saving Record objects.
    """
    def load_records(self, file_path):
        """
        Docstring for load_records
        
        :param self: Description
        :param file_path: Description
        """
        records = []
        try:
            with open(file_path, mode='r', newline='', encoding='cp1252') as csvfile:
                reader = csv.reader(csvfile)
                next(reader) #skipping header row
                for row in reader:
                    if len(row) != 7:
                        print(f"Skipping malformed row: {row}")
                        continue
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
                        
                        if len(records) >= 100:
                            break
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading records: {str(e)}")
        
        return records
                  

