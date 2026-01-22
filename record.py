"""
Docstring for CST8002-PracticalProject01.record

Author: Timothy Jacot
Course code: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Due Date: January 23rd 2026


"""
#Entity object Record
class Record:
    def __init__(self, site_id, year, diver_id, transect, transect_distance, species_code, count):
        self.site_id = site_id
        self.year = year
        self.diver_id = diver_id
        self.transect = transect
        self.transect_distance = transect_distance
        self.species_code = species_code
        self.count = count

    # Getters for each column
    def get_site_id(self):
        return self.site_id

    def get_year(self):
        return self.year

    def get_diver_id(self):
        return self.diver_id

    def get_transect(self):
        return self.transect

    def get_transect_distance(self):
        return self.transect_distance

    def get_species_code(self):
        return self.species_code

    def get_count(self):
        return self.count
    
    # Setters for each column

    def set_site_id(self, value):
        self.site_id = value

    def set_year(self, value):
        self.year = value

    def set_diver_id(self, value):
        self.diver_id = value

    def set_transect(self, value):
        self.transect = value

    def set_transect_distance(self, value):
        self.transect_distance = value

    def set_species_code(self, value):
        self.species_code = value

    def set_count(self, value):
        self.count = value
    
    #Displaying record
    def __str__(self):
        return f"Record(Site ID: {self.site_id}, Year: {self.year}, Diver ID: {self.diver_id}, Transect: {self.transect}, Transect Distance: {self.transect_distance}, Species Code: {self.species_code}, Count: {self.count})"