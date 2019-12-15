# -*- coding: utf-8 -*-
import scrapy


class CountriesPastFutureSpider(scrapy.Spider):
    name = 'countries_past_future'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_country, meta={"country_name": name})

    def parse_country(self, response):
        name = response.request.meta["country_name"]
        rows_past = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        rows_future = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[2]/tbody/tr')

        result = {}
        result["past"] = []
        result["future"] = []

        for row in rows_past:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            result["past"].append({
                "year": year,
                "population":population
            })

        for row in rows_future:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            result["future"].append({
                "year": year,
                "population":population
            })

        yield {
            "country_name": name,
            "data": result
        }