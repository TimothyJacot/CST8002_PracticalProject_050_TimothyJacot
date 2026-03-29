"""
Docstring for presentationlayer.main

Author: Timothy Jacot
Course: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Description: Presentation layer handling user interaction

"""

from businesslayer.record_service import RecordService
from model.record import Record
def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nProgram by Timothy Jacot")
    print("Menu:")
    print("1. Load data from CSV")
    print("2. View all records")
    print("3. View specific record")
    print("4. Add new record")
    print("5. Update existing record")
    print("6. Delete record")
    print("7. Save records to CSV")
    print("8. Exit")
def main():
    """
    Main function to run the program, handling user input
    and coordinating with RecordService.
    """
    service = RecordService()
    file_path = "data/data/pacific_rim_npr_coastalmarine_kelp_density_2013-2016_data.csv"
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            service.load_data(file_path)
            print("Data loaded successfully.")

        elif choice == '2':
            records = service.get_all_records()
            for  i, record in enumerate(records):
                print(f"{i}: {record}")
        
        elif choice == '3':
            index = int(input("Enter record index: "))
            try:
                record = service.get_record(index)
                print(record)
            except IndexError:
                print("Invalid record index.")

        elif choice == '4':
            try:
                site_id = input("Enter site ID: ")
                year = int(input("Enter year: "))
                diver_id = input("Enter diver ID: ")
                transect = input("Enter transect: ")
                transect_distance = float(input("Enter transect distance: "))
                species_code = input("Enter species code: ")
                count = int(input("Enter count: "))

                new_record = Record(
                    site_id, 
                    year, 
                    diver_id, 
                    transect, 
                    transect_distance, 
                    species_code, 
                    count)
                service.add_record(new_record)
                print("Record added successfully.")
            except ValueError:
                print("Invalid input. Please enter correct data types.")

        elif choice == '5':
            try:
                index = int(input("Enter record index to update: "))
                
                site_id = input("Enter new site ID: ")
                year = int(input("Enter new year: "))
                diver_id = input("Enter new diver ID: ")
                transect = input("Enter new transect: ")
                transect_distance = float(input("Enter new transect distance: "))
                species_code = input("Enter new species code: ")
                count = int(input("Enter new count: "))

                updated_record = Record(
                    site_id, 
                    year, 
                    diver_id, 
                    transect, 
                    transect_distance, 
                    species_code, 
                    count)
                service.update_record(index, updated_record)
                print("Record updated successfully.")

            except (ValueError, IndexError):
                print("Invalid input or record index. Please try again.")
        
        elif choice == '6':
            try:
                index = int(input("Enter record index to delete: "))
                service.delete_record(index)
                print("Record deleted successfully.")
            except IndexError:
                print("Invalid record index. Please try again.")
        
        elif choice == '7':
                filename = service.save_data()
                print(f"Records saved to {filename}")
        
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


            


