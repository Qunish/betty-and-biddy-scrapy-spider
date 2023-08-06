# Betty and Biddy Summer Sale Spider

This repository contains two Scrapy spiders designed to scrape product information from the Betty and Biddy Summer Sale website. The spiders navigate through the sale pages, extract details of products listed on each page, and store the scraped data in a MongoDB database for later analysis or use.

## Requirements

- Python 3.x
- Scrapy
- pymongo

## Usage

1. Install the required dependencies:

   ```bash
   pip install scrapy pymongo
   ```

2. Make sure you have a running instance of MongoDB on your local machine or modify the MongoDB connection parameters in the spiders accordingly if using a remote database.

3. Choose one of the spiders to run:

   - `bettyandbiddy_spider.py`: This spider extracts product information and stores it in the MongoDB collection `summer_sale_lv`.
   - `bettyandbiddy_spider_pv.py`: This spider extracts more detailed product information and stores it in the MongoDB collection `summer_sale`.

4. Run the chosen spider using the following command:

   ```bash
   scrapy runspider your_chosen_spider.py
   ```

   Replace `your_chosen_spider.py` with the filename of the selected spider.

5. The spider will start scraping the product information from the Betty and Biddy Summer Sale website and store it in the corresponding MongoDB collection.

## Spider Details

### `bettyandbiddy_spider.py`

- **Name**: `summer_sale_lv`
- **Start URLs**: The spider starts crawling from the initial page of the summer sale: `"https://bettyandbiddy.com/collections/summer-sale?page=1"`
- **Pagination**: The spider will follow the pagination links on the website to access subsequent pages of the summer sale.

### `bettyandbiddy_spider_pv.py`

- **Name**: `summer_sale_pv`

## Data Scraped

### `bettyandbiddy_spider.py`

The spider extracts the following information from each product listed on the summer sale pages:

- Product Name
- Original Price (before discount)
- Sale Price (discounted price)
- Product Link

### `bettyandbiddy_spider_pv.py`

The spider extracts the following detailed information from each product page:

- Product Description
- Product Material
- Product Size
- Image Link

Please note that the CSS selectors used to extract the information might need to be adjusted based on the current structure of the website if any changes have occurred since the code was written.

## MongoDB Storage

The scraped product data is stored in a MongoDB database named `bettyandbiddy_db` within the `summer_sale` collection. The MongoDB connection parameters are set to connect to a local MongoDB server (`localhost:27017`). If you are using a remote MongoDB server, make sure to modify the connection parameters in the respective spiders' `__init__` method.

The spiders fetch the product links or details from the corresponding MongoDB collection and update or insert the data into the MongoDB collections `summer_sale_lv` and `summer_sale`. The `upsert=True` parameter ensures that if a product URL is not found in the collection, a new document will be inserted, and if it exists, the existing document will be updated.

Please ensure that you are aware of and adhere to the website's terms of service and scraping policies while using these spiders. Unauthorized scraping or excessive requests may result in IP blocking or other restrictions by the website.