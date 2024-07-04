# sorting_algorithms.py
def bubble_sort(data, key):
    data_copy = data.copy()
    n = len(data_copy)
    for i in range(n):
        for j in range(0, n-i-1):
            if data_copy[j][key] > data_copy[j+1][key]:
                data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]
    return data_copy

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x[key] < pivot[key]]
    middle = [x for x in data if x[key] == pivot[key]]
    right = [x for x in data if x[key] > pivot[key]]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# searching_algorithms.py
def search_by_attribute(data, query):
    query_lower = query.lower()
    return [item for item in data if query_lower in str(item).lower()]

# main.py
import sys
from algorithms.sorting_algorithms import bubble_sort, quick_sort
from algorithms.searching_algorithms import search_by_attribute

# Sample data
cars_data = [
    {"Name": "Toyota Corolla 2021 Altis Grande X CVT-i 1.8 Black Interior", "Price": "67.5", "City": "Karachi", "Model": "2021", "Kilometers": "18,939 km", "Fuel": "Petrol", "CC": "1800 cc", "Mode": "Automatic"},
    {"Name": "MG ZS 2022 1.5L", "Price": "56.9", "City": "Multan", "Model": "2022", "Kilometers": "5,996 km", "Fuel": "Petrol", "CC": "1490 cc", "Mode": "Automatic"},
    {"Name": "DFSK Glory 580 2021 Pro", "Price": "54.75", "City": "Lahore", "Model": "2021", "Kilometers": "25,800 km", "Fuel": "Petrol", "CC": "1498 cc", "Mode": "Automatic"},
    {"Name": "Toyota Hiace 2007 DX", "Price": "27.5", "City": "Mardan", "Model": "2007", "Kilometers": "150,000 km", "Fuel": "Petrol", "CC": "2700 cc", "Mode": "Automatic"},
    {"Name": "Honda City 2005 i-DSI Vario", "Price": "14", "City": "Lahore", "Model": "2005", "Kilometers": "275,000 km", "Fuel": "Petrol", "CC": "1300 cc", "Mode": "Automatic"},
    {"Name": "Toyota Vitz 2018 F 1.0", "Price": "39.3", "City": "Lahore", "Model": "2018", "Kilometers": "70,000 km", "Fuel": "Petrol", "CC": "1000 cc", "Mode": "Automatic"},
    {"Name": "Daihatsu Hijet 2014 Deluxe", "Price": "17.75", "City": "Karachi", "Model": "2014", "Kilometers": "140,000 km", "Fuel": "Petrol", "CC": "660 cc", "Mode": "Automatic"},
    {"Name": "Honda City 5th Generation 2021 1.3 i-VTEC Prosmatec", "Price": "42.45", "City": "Rawalpindi", "Model": "2021", "Kilometers": "41,000 km", "Fuel": "Petrol", "CC": "1300 cc", "Mode": "Automatic"},
    {"Name": "Toyota Corolla 2015 GLi Automatic 1.3 VVTi", "Price": "36.9", "City": "Lahore", "Model": "2015", "Kilometers": "136,000 km", "Fuel": "Petrol", "CC": "1300 cc", "Mode": "Automatic"},
    {"Name": "Toyota Corolla 2020 GLi Automatic 1.3 VVTi", "Price": "47", "City": "Jhelum", "Model": "2020", "Kilometers": "39,000 km", "Fuel": "Petrol", "CC": "1300 cc", "Mode": "Automatic"},
    {"Name": "Toyota Hilux 2012 Vigo Champ G", "Price": "60", "City": "Rawalpindi", "Model": "2012", "Kilometers": "140,000 km", "Fuel": "Diesel", "CC": "2500 cc", "Mode": "Automatic"},
    {"Name": "Toyota Passo 2006 G 1.0", "Price": "18.75", "City": "Islamabad", "Model": "2006", "Kilometers": "135,000 km", "Fuel": "Petrol", "CC": "1000 cc", "Mode": "Automatic"},
    {"Name": "Toyota Yaris 2003", "Price": "1.5", "City": "Lahore", "Model": "2003", "Kilometers": "150,000 km", "Fuel": "Petrol", "CC": "1000 cc", "Mode": "Automatic"},
    {"Name": "Nissan Dayz 2014 Highway star X", "Price": "22.8", "City": "Lahore", "Model": "2014", "Kilometers": "122,000 km", "Fuel": "Petrol", "CC": "660 cc", "Mode": "Automatic"},
    {"Name": "Toyota Vitz 2002 F 1.0", "Price": "19", "City": "Lahore", "Model": "2002", "Kilometers": "302,000 km", "Fuel": "Petrol", "CC": "1000 cc", "Mode": "Automatic"},
]

def display_menu():
    print("\nWelcome to Wheels Probe")
    print("1. View Information")
    print("2. Sort Data")
    print("3. Search Data")
    print("4. Exit")

def display_info():
    print("\nInformation about Wheels Probe")
    print("This application helps you to sort and search car data.")

def display_cars_data(data):
    headers = ["Name", "Price", "City", "Model", "Kilometers", "Fuel", "CC", "Mode"]
    for car in data:
        print("\n".join([f"{header}: {car[header]}" for header in headers]))
        print("")

def sort_data():
    global cars_data
    print("\nSelect Sorting Algorithm")
    print("1. Bubble Sort")
    print("2. Quick Sort")
    algo_choice = input("Enter choice: ")

    print("\nSelect Attribute to Sort By")
    print("1. Name")
    print("2. Price")
    print("3. City")
    print("4. Model")
    print("5. Kilometers")
    print("6. Fuel")
    print("7. CC")
    print("8. Mode")
    attr_choice = input("Enter choice: ")

    algo_dict = {"1": "Bubble Sort", "2": "Quick Sort"}
    attr_dict = {
        "1": "Name",
        "2": "Price",
        "3": "City",
        "4": "Model",
        "5": "Kilometers",
        "6": "Fuel",
        "7": "CC",
        "8": "Mode",
    }

    algo = algo_dict.get(algo_choice, "Bubble Sort")
    attribute = attr_dict.get(attr_choice, "Name")

    if algo == "Bubble Sort":
        cars_data = bubble_sort(cars_data, attribute)
    elif algo == "Quick Sort":
        cars_data = quick_sort(cars_data, attribute)

    print(f"\nData sorted by {attribute} using {algo}")
    display_cars_data(cars_data)

def search_data():
    query = input("\nEnter search query: ")
    results = search_by_attribute(cars_data, query)
    if results:
        print(f"\nSearch results for '{query}':")
        display_cars_data(results)
    else:
        print(f"\nNo results found for '{query}'")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_info()
        elif choice == "2":
            sort_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            print("\nExiting the application. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
