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
        Initializes RecordService with empty list of records
        and RecordRepository instance.
        """
        self.records = [] 
        self.repo = RecordRepository()

    def load_data(self, file_path):
        """
        Loads records from CSV file into memory using RecordRepository.
        """
        all_records = self.repo.load_records(file_path)
        print(f"Loaded {len(all_records)} records from file.")
        self.records = all_records

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
    
    def sort_by_year(self):
        """
        Sorts in-memory records by year.
        """
        self.records.sort(key=lambda record: record.get_year())
        print("Records: Sorted by year.")
    
    def sort_by_site_id(self):
        """
        Sorts in-memory records by site ID.
        """
        self.records.sort(key=lambda record: record.get_site_id())
        print("Records: Sorted by site ID.")
    
    def sort_by_count(self):
        """
        Sorts in-memory records by count.
        """
        self.records.sort(key=lambda record: record.get_count())
        print("Records: Sorted by count.")

    def filter_records (self, year=None, site_id=None, min_count=None):
        """
        Filters records based on year, site ID, and minimum count.
        
        """

        filtered = self.records
        if year is not None:
            filtered = [record for record in filtered if record.get_year() == year]
        if site_id is not None:
            filtered = [record for record in filtered if record.get_site_id().strip().lower() == site_id.strip().lower()]
        if min_count is not None:
            filtered = [record for record in filtered if record.get_count() >= min_count]
        return filtered
        