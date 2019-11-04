#!/bin/bash
scrapy crawl seek-spider -a start_url='https://www.seek.com.au/companies/commonwealth-bank-of-australia-432306/reviews' -o commonwealth.csv
scrapy crawl seek-spider -a start_url='https://www.seek.com.au/companies/google-433216/reviews' -o google.csv

