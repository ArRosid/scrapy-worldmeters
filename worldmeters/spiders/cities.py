# -*- coding: utf-8 -*-
import scrapy


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//tr/td/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_country, meta={"country_name": name})
    
    def parse_country(self, response):
        data = []
        country_name = response.request.meta["country_name"]

        cities = response.xpath('//table[@class="table table-hover table-condensed table-list"]/tbody/tr')

        for city in cities:
            city_name = city.xpath(".//td[2]/text()").get()
            population = city.xpath(".//td[3]/text()").get()

            data.append({
                "city_name": city_name,
                "population": population
            })

        yield {
            "country_name": country_name,
            "data": data
        }
