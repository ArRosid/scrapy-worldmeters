# -*- coding: utf-8 -*-
import scrapy


class CountriesForecastSpider(scrapy.Spider):
    name = 'countries_forecast'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//tr/td/a")
        for country in countries:
            link = country.xpath(".//@href").get()
            name = country.xpath(".//text()").get()

            yield response.follow(url=link, callback=self.parse_country, meta={"country_name":name})

    def parse_country(self, response):
        country_name = response.request.meta["country_name"]
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[2]/tbody/tr')

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                "country_name": country_name,
                "year": year,
                "population": population
            }
