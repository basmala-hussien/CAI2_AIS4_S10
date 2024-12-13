#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup
import csv
import json

# Fetch and parse HTML content
# Define the website URL to scrape and send an HTTP GET request
website  = "https://www.baraasallout.com/test.html"
response = requests.get(website)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Utility function to write data to CSV
# Saves extracted data into a CSV file with specified headers and rows
def write_csv(filename, headers, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

# Utility function to write data to JSON
# Saves extracted data into a JSON file with formatted output
def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# 1. Extract Text Data
# Extracts headings (h1, h2), paragraphs (p), and list items (li) from the HTML
# Saves the extracted data into a CSV file
def extract_text_data():
    headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2'])]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
    list_items = [li.get_text(strip=True) for li in soup.find_all('li')]
    write_csv("Extract_Text_Data.csv", ["Headings", "Paragraphs", "List Items"],
              [[", ".join(headings), ", ".join(paragraphs), ", ".join(list_items)]])

# 2. Extract Table Data
# Extracts rows and columns from an HTML table and saves them into a CSV file
def extract_table_data():
    table = soup.find('table')
    if not table:  # If no table is found, exit the function
        return
    rows = [[cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])] for row in table.find_all('tr')]
    write_csv("Extract_Table_Data.csv", rows[0], rows[1:])

# 3. Extract Product Information
# Extracts product details from cards with a specific class and saves them into a JSON file
def extract_product_information():
    cards = soup.find_all(class_="book-card")
    products = []
    for card in cards:
        products.append({
            "Book Title": card.find(class_="book-title").get_text(strip=True) if card.find(class_="book-title") else "",
            "Price": card.find(class_="price").get_text(strip=True) if card.find(class_="price") else "",
            "Stock Availability": card.find(class_="stock-status").get_text(strip=True) if card.find(class_="stock-status") else "",
            "Button Text": card.find('button').get_text(strip=True) if card.find('button') else ""
        })
    write_json("Product_Information.json", products)

# 4. Extract Form Details
# Extracts details of form inputs (name, type, and default value) and saves them into a JSON file
def extract_form_details():
    form = soup.find('form')
    if not form:  # If no form is found, exit the function
        return
    inputs = form.find_all('input')
    form_data = [{"Field Name": inp.get('name', ""), "Input Type": inp.get('type', ""), "Default Value": inp.get('value', "")} for inp in inputs]
    write_json("Form_Details.json", form_data)

# 5. Extract Links and Multimedia
# Extracts all links and the video URL (if available) and saves them into a JSON file
def extract_links_and_multimedia():
    links = [{"Text": a.get_text(strip=True), "Href": a.get('href', "")} for a in soup.find_all('a')]
    video_link = soup.find('iframe').get('src') if soup.find('iframe') else ""
    write_json("Links_and_Multimedia.json", {"Links": links, "Video Link": video_link})

# 6. Extract Featured Products
# Extracts featured product details (id, name, price, colors) and saves them into a JSON file
def extract_featured_products():
    featured_products = soup.find_all(class_="featured-product")
    products = []
    for product in featured_products:
        products.append({
            "id": product.get('data-id', ""),
            "name": product.find('span', class_="name").get_text(strip=True) if product.find('span', class_="name") else "",
            "price": product.find('span', class_="price").get_text(strip=True) if product.find('span', class_="price") else "N/A",
            "colors": product.find('span', class_="colors").get_text(strip=True) if product.find('span', class_="colors") else "N/A"
        })
    write_json("Featured_Products.json", products)

# Execute all tasks
# Calls all the above functions to perform various scraping tasks
extract_text_data()
extract_table_data()
extract_product_information()
extract_form_details()
extract_links_and_multimedia()
extract_featured_products()

# Prints a success message when all tasks are complete
print("Web scraped successfully")


# In[ ]:




