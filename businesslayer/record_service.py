"""
Docstring for businesslayer.record_service

Author: Timothy Jacot
Course: CST8002
Professor: Tyler DeLay
Description: record_service.py handles business logic and memory management.

"""

from persistencelayer.record_repo import RecordRepository

class RecordService:
    """
   Manages Record objects in memory and coordinates with persistence layer.
    
    """
    def __init__(self):
        """
        Initializes RecordServices with empty list of records
        and RecordRepo instance
        """
        self.record = []
        self.repo = RecordRepository()

        def load_data(self, file_path):
            """
            Loads records from CSV file into memory using RecordRepository.
            
            """
            self.records = self.repo.load_records(file_path)
        def reload_data(self, file_path):
            """
            Reloads data from dataset, replacing memory records

            """
            self.load_data(file_path)

        def get_all_records(self):
            """
            Returns all in-memory records.
            
            """
            return self.records
        def get_record(self, index):
            """
            Retrieves a specific record by index.
            
            """
            return self.records[index]
        def add_record(self, record):
            """
            Adds a new record to memory.
            
            """
            self.records.append(record)

        def update_record(self, index, updated_record):
            """
            Updates an existing record at specified index.
            
            """
            self.records[index] = updated_record

        def delete_record(self, index):
            """
            Deletes a record from memory at specified index.
            
            """
            del self.records[index]

        def save_data(self):
            """
            Saves current in-memory records to new CSV file using RecordRepository.
            
            """
            self.repo.save_records(self.records)
        
