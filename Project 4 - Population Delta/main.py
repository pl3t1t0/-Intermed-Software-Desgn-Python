import csv
import os
from collections import OrderedDict

class Population:
    def __init__(self):
        self.file_import = []  # Store file contents as a list of dictionaries
        self.annual = OrderedDict()  # Store annual population estimates
        self.biannual = OrderedDict()  # Store biannual changes

    def import_csv(self, filename):
        """Imports CSV data and stores it in file_import as a list of rows."""
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.file_import = list(reader)  # Store file content as a list
                
                for row in self.file_import:
                    city = row['Geographic_Area'].strip()
                    self.annual[city] = {
                        'Apr_2020': int(row['Pop_Est_ Apr_2020 '].strip()),
                        'Jul_2020': int(row['Pop_Est_Jul_2020'].strip()),
                        'Jul_2021': int(row['Pop_Est_Jul_2021'].strip())
                    }
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"Error: {e}")

    def biannual_delta(self):
        """Calculates the population change over two years and returns the count."""
        if not self.file_import:
            print("Error: No data imported.")
            return 0

        positive_count = 0
        for city, data in self.annual.items():
            delta = data['Jul_2021'] - data['Apr_2020']
            self.biannual[city] = delta
            if delta > 0:
                positive_count += 1
        
        return positive_count

    def annual_delta(self):
        """Calculates the annual population change and returns the count."""
        if not self.file_import:
            print("Error: No data imported.")
            return 0
        
        positive_count = 0
        temp_annual = OrderedDict()  # Temporary dictionary to store annual deltas
        for city, data in self.annual.items():
            delta = data['Jul_2021'] - data['Jul_2020']
            temp_annual[city] = delta
            if delta > 0:
                positive_count += 1
        
        self.annual = temp_annual  # Replace with correctly formatted annual dictionary
        return positive_count

    def search_by_loc(self, city):
        """Searches for city data in both annual and biannual dictionaries."""
        found = {}
        if city in self.annual:
            found['Annual Delta'] = self.annual.get(city, 0)
            found['Biannual Delta'] = self.biannual.get(city, 0)
        else:
            found = {'Annual Delta': 0, 'Biannual Delta': 0}
        return found

    def export_csv(self, filename):
        """Exports processed data to a new CSV file with a specific format."""
        if not self.file_import:
            print("Error: No data to export.")
            return
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Geographic Area', 'Bi-Annual Delta', 'Annual Delta'])
            
            for city in self.annual:
                biannual_delta = self.biannual.get(city, 0)
                annual_delta = self.annual.get(city, 0)
                writer.writerow([city, biannual_delta, annual_delta])

# Example Usage:
pop = Population()
pop.import_csv("./Project 4 - Population Delta/census_population.csv")
positive_biannual = pop.biannual_delta()
positive_annual = pop.annual_delta()
print(f"Number of cities with positive biannual growth: {positive_biannual}")
print(f"Number of cities with positive annual growth: {positive_annual}")
print(pop.search_by_loc('New York city, New York'))
pop.export_csv("./Project 4 - Population Delta/output_population.csv")
