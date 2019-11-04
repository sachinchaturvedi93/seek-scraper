# -*- coding: utf-8 -*-
import scrapy
import json
from pprint import pprint
import re


class SeekSpiderSpider(scrapy.Spider):
    name = 'seek-spider'
    
    allowed_domains = ['seek.com.au']

    def __init__(self, *args, **kwargs):
        super(SeekSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
    """start_urls = [
        'https://www.seek.com.au/companies/commonwealth-bank-of-australia-432306/reviews']"""
    
    
    def parse(self,response):
        href = response.xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div[1]/link/@href').extract()
        print(href)
        s = str(href)
        res = re.findall(r'\d+', s)
        res = str(res)
        string = (res[res.find("[")+1:res.find("]")])
        string_replaced = string.replace("'", "")
        print(string_replaced)
        next_urls = 'https://company-profiles-api.cloud.seek.com.au/v1/companies/'+string_replaced+'/reviews?page=1'
        print(next_urls)
        yield scrapy.Request(next_urls, callback=self.parse_detail)
  
    def parse_detail(self, response):
        result = json.loads(response.body)
        res = []
        for i in result['data']:
            detail = {}
            detail['ID'] = i['id']
            detail['Date'] = i['reviewCreatedAt']
            detail['JobTitle'] = i['jobTitle']
            detail['PostTitle'] = i['title']
            detail['Pros'] = i['pros']
            detail['Cons'] = i['cons']
            detail['EmploymentStatus'] = i['yearLeftEmploymentStatusText']
            detail['Location'] = i['workLocation']
            detail['OverallRating'] = i['ratingCompanyOverall']
            detail['BenefitsRating'] = i['ratingBenefitsAndPerks']
            detail['CareerOpportunityRating'] = i['ratingCareerOpportunity']
            detail['SeniorManagementRating'] = i['ratingExecutiveManagement']
            detail['WorkEnvironmentRating'] = i['ratingWorkEnvironment']
            detail['WorkLifeBalanceRating'] = i['ratingWorkLifeBalance']
            detail['DiversityRating'] = i['ratingDiversity']
            res.append(detail)
        return res

        
        
