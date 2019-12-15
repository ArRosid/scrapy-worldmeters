# scrapy-worldmeters
Scrapy Project to scrape worldmeters.info website

To run this project, make sure you have scrapy installed. You can use this command to install scrapy<br>
<i>pip install scrapy</i>

If you have scrapy installed, you can run this command by this command<br>
<i>scrapy crawl countries -o result.json</i>

You can also scrape the countries forecast population using this command<br>
<i>scrapy crawl countries_forecast -o result_forecast.json</i>

You can also scrape the past & future populations of countries in just one time by using this command<br>
<i>scrapy crawl countries_past_future -o result_past_future.json</i>

You can also scrape Main cities by population in each countries by using this command<br>
<i>scrapy crawl cities -o result_cities.json</i>
