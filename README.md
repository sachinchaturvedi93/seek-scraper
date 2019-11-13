# Seek Review Scraper

# Installation
First, make sure that you're using Python 3.

1. Clone or download this repository.
2. Run `pip install -r requirements.txt`
3. Open your terminal and go to your root directory where you want to create the scraper folder.
4. Write `scrapy startproject seek in your terminal. This will create the seek folder. Enter `cd seek/seek/spiders` in terminal to go to the spiders directory.
5. Enter scrapy `genspider seek-spider "seek.com"`
6. Now if you go to the directory `/seek/seek/spiders` you will find seek_spider.py file. Change the content with my `seek_spider.py` file.
7. When you are in the directory /seek/seek/spiders write in your terminal : `scrapy crawl seek-spider -a start_url='https://www.seek.com.au/companies/commonwealth-bank-of-australia-432306/reviews' -o commonwealth.csv`
