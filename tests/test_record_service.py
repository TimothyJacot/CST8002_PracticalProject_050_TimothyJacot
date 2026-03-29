"""
Docstring for tests.test_record_service

Author: Timothy Jacot
Course: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Description: Tests add_record functionality of business layer.

"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from businesslayer.record_service import RecordService
from model.record import Record

print("Program by: Timothy Jacot")

class TestRecordService(unittest.TestCase):

    def test_add_record(self):
        """
        Test that a record is added to the in-memory list.

        """
        service = RecordService()

        record = Record(
            site_id="TestSite", 
            year=2025, 
            diver_id="D1", 
            transect="T1", 
            transect_distance=10.5, 
            species_code="SP01", 
            count=3
            )
        
        service.add_record(record)
        self.assertEqual(len(service.get_all_records()), 1)
        self.assertEqual(service.get_all_records()[0].get_site_id(), "TestSite")

if __name__ == '__main__':
    unittest.main()
