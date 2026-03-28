import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    # URL of the site to scrape
    base_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    
    # Send an HTTP request
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Failed to retrieve the website")
        return

    # Parse the content
    soup = BeautifulSoup(response.content, 'html.parser')
    category_name = "Mystery" # Setting manually based on the URL
    
    books = []
    # Find all book articles
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        # Extract star rating (stored as a class name)
        rating = book.p['class'][1]
        price = book.find('p', class_='price_color').text
        # Availability check
        availability = book.find('p', class_='instock availability').text.strip()
        # Build the full link
        link = "http://books.toscrape.com/catalogue/" + book.h3.a['href'].replace('../../../', '')

        books.append([title, category_name, price, rating, availability, link])

    # Save to CSV as required by section 1 of your project [cite: 30]
    with open('books_raw.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header row
        writer.writerow(['Title', 'Category', 'Price', 'Rating', 'Availability', 'Link'])
        writer.writerows(books)

    print(f"Successfully scraped {len(books)} books and saved to books_raw.csv")

if __name__ == "__main__":
    scrape_books()