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
                    if len(row) < 7:
                        print(f"Skipping malformed row: {row}")
                        continue
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
                    except ValueError as ve:
                        continue
                        if len(records) >= 100:
                            break
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading records: {str(e)}")
        
        return records
    def save_records(self, records):
        """
        Docstring for save_records
        Saves provided list of Record objects to new CSV file.
        Filename is generated using UUID.
        Returns created file name.

        """
        unique_filename = f"{uuid.uuid4()}.csv"

        try:
            with open(unique_filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow([
                    "site_id", 
                    "year", 
                    "diver_id",
                    "transect",
                    "transect_distance",
                    "species_code",
                    "count"
                ])
                for record in records:
                    writer.writerow([
                        record.get_site_id(),
                        record.get_year(),
                        record.get_diver_id(),
                        record.get_transect(),
                        record.get_transect_distance(),
                        record.get_species_code(),
                        record.get_count()
                    ])
        except Exception as e:
            raise Exception(f"An error occurred while saving records: {str(e)}")
        
        return unique_filename
                          

