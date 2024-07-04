from bs4 import BeautifulSoup
import requests
import csv

# Initialize lists
Name = []
price_element = []
City = []
Model = []
Kilometers = []
Fuel = []
CC = []
Mode = []

# Loop through all pages
for page_number in range(1, 1827):  # Assuming you have 1828 pages to scrape
    url = f'https://www.pakwheels.com/used-cars/automatic/57336?page={page_number}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Extract titles only once and append them to the Name array
    car_links = soup.find_all('a', class_='car-name ad-detail-path')
    for car_link in car_links:
        title = car_link['title']
        if title is not None:
            Name.append(title)
        else:
            Name.append('None')
    class_name = f'well search-list clearfix ad-container page-{page_number}'

    # Loop through car listings
    for item in soup.find_all('div', class_=class_name):
        # Extract and process price
        price = item.find(class_='price-details generic-dark-grey')
        if price is not None:
            price_text = ''.join(price.get_text().split())  # Remove spaces
            price_value = price_text.replace('PKR', '').replace('lacs', '')  # Remove PKR and lacs
            price_element.append(price_value)
        else:
            price_element.append(0)

        # Extract and process City
        Cities = item.find(class_='list-unstyled search-vehicle-info fs13')
        if Cities is not None:
            City.append(Cities.text.strip())
        else:
            City.append('None')

    # Extract Model, Kilometers, Fuel, CC, and Mode
    for data in soup.find_all('ul', class_='list-unstyled search-vehicle-info-2 fs13'):
        all_li = data.find_all('li')
        Model.append(all_li[0].text if len(all_li) > 0 else 'None')
        Kilometers.append(all_li[1].text if len(all_li) > 1 else 0)
        Fuel.append(all_li[2].text if len(all_li) > 2 else 'None')
        CC.append(all_li[3].text if len(all_li) > 3 else 0)
        Mode.append(all_li[4].text if len(all_li) > 4 else 'None')

# Create a CSV file and write the data
with open('PakWheels2.csv', mode='a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Price', 'City', 'Model', 'Kilometers', 'Fuel', 'CC', 'Mode'])  # Write header
    for i in range(len(Name)):
        writer.writerow([Name[i], price_element[i], City[i], Model[i], Kilometers[i], Fuel[i], CC[i], Mode[i]])
        print(i)