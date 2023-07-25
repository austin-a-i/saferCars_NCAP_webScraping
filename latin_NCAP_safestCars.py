# This is a sample Python script.


# pip install requests --upgrade --quiet'
import requests
# pip install pandas --quiet
import pandas as pd
# pip install beautifulsoup4 --upgrade --quiet
from bs4 import BeautifulSoup

# Importing html data from website
latin_ncap_url = "https://www.latinncap.com/en/results"
response = requests.get(latin_ncap_url)
print(response)
page_contents = response.text

# print(page_contents)

# Parsing data using BeautifulSoup lib
doc = BeautifulSoup(response.content, 'html.parser')
# print(doc.prettify())
# print(doc.title)

# # Getting the name of the tag
# print(doc.title.name)

# # Getting the name of parent tag
# print(doc.title.parent.name)

# Extract brand names data and append to list
selection_class = "tit-marca"
brand_tags = doc.find_all('span', {'class': selection_class})
print(len(brand_tags))

brand_names = []
for brand in brand_tags:
    brand_name = brand.text
    if brand_name not in brand_names:
        brand_names.append(brand_name)
print(brand_names)
print(len(brand_names))

# Extract vehicle-model data and append to list
vehicle_models = []
model_manufacturer = []
vehicle_model_tags = doc.find_all('h3', class_=False, id=False)
for tag in vehicle_model_tags:
    vehicle_models.append(tag.text)
    for model in brand_names:
        if model in tag.text:
            model_manufacturer.append(model)
len(model_manufacturer)

# Extract publication_date data | removing unnecessary line-breaks,white-spaces
#            before appending to list
date_class = "colum colum-fecha"
date_tags = doc.find_all('div', {'class': date_class})

date_titles = []
for tag in date_tags:
    date_titles.append(tag.text)

published_year = []
char = ['\n\t', '\t']
for element in date_titles:
    for char in element:
        element.replace(char, "")
    published_year.append(element.strip())

# Extract adult safety rating data and append to list
adult_class = "porcentaje adulto"
adult_tags = doc.find_all('div', {'class': adult_class})

adult_safety = []
for tag in adult_tags:
    adult_safety.append(tag.text)
len(adult_safety)

# Extract child safety rating and append to list
child_class = "porcentaje nino"
child_tags = doc.find_all('div', {'class': child_class})

child_safety = []
for tag in child_tags:
    child_safety.append(tag.text)
len(child_safety)

# Extract pedestrian safety rating and append to list
pedestrian_class = "porcentaje usuarios"
pedestrian_tags = doc.find_all('div', {'class': pedestrian_class})

pedestrian_safety = []
for tag in pedestrian_tags:
    pedestrian_safety.append(tag.text)
len(pedestrian_safety)

# Extract overall safety star rating and append to list
star_class = "colum colum-estrellas"
star_tags = doc.find_all('div', {'class': star_class})

star_rating = []
star_rating_class = "estrella-act"
for stars in star_tags:
    star_text = str(stars)
    star_count = star_text.count(star_rating_class)
    star_rating.append(star_count)

# Extract overall safety measures rating and append to list
safety_class = "porcentaje asistentes"
safety_tags = doc.find_all('div', {'class': safety_class})

safety_titles = []
for tag in safety_tags:
    safety_titles.append(tag.text)
len(safety_titles)

# Print the extracted data and length
print("Manufacturer", len(model_manufacturer), model_manufacturer)
print("Models:", len(vehicle_model_tags), vehicle_models)
print("Star rating", len(star_rating), star_rating)
print("Years of publication:", len(published_year), published_year)
print("Adult Safety", len(adult_safety), adult_safety)
print("Child Safety", len(child_safety), child_safety)
print("Safety:", len(safety_titles), safety_titles)

# Initializing Dictionary K-V pair and creating DataFrame
ncap_dict = {
    'Manufacturer': model_manufacturer[:29],
    'Model': vehicle_models[:29],
    "Star rating": star_rating,
    'Published Date': published_year[:29],
    'Adult Safety': adult_safety[:29],
    'Child': child_safety[:29],
    'Pedestrian': pedestrian_safety[:29],
    'Safety': safety_titles[:29]
}

ncap_df = pd.DataFrame(ncap_dict)
#print(ncap_df)

'''
# Write the DataFrame to the CSV file
csv_file = "SafetyCarData_From2020.csv"
ncap_df.to_csv(csv_file, index=False)
print("DataFrame has been successfully written to", csv_file)
'''

driver_class = "colum colum-240 adulto"
adult_occupant = doc.find_all('div', {'class': driver_class})
len(adult_occupant)

driver_safety_titles = []
for tag in adult_occupant:
    driver_safety_titles.append(tag.text)
len(driver_safety_titles)

char = '\n'
driver_safety_stars = [ele.replace(char, '') for ele in driver_safety_titles]
driver_safety_stars[0]

back_class = "colum colum-240 nino"
child_occupant = doc.find_all('div', {'class': back_class})
child_occupant[0].text

child_safety_titles = []
for tag in child_occupant:
    child_safety_titles.append(tag.text)
len(child_safety_titles)

char = '\n'
child_safety_stars = [ele.replace(char, '') for ele in child_safety_titles]
child_safety_stars[0]

print("Manufacturer", len(model_manufacturer))
print('Model', len(vehicle_model_tags))
print('Adult', len(driver_safety_stars))
print('Child', len(child_safety_stars))

ncap1_dict = {
    'Manufacturer': model_manufacturer[30:],
    'Model': vehicle_models[31:],
    'Adult Occupant': driver_safety_stars,
    'Child Occupant': child_safety_stars,
}

ncap1_df = pd.DataFrame(ncap1_dict)
print(ncap1_df)

'''
# Write the DataFrame to the CSV file
csv_file1 = "SafetyCarData_Before2020.csv"
ncap1_df.to_csv(csv_file1, index=False)
print("DataFrame has been successfully written to", csv_file1)
'''
