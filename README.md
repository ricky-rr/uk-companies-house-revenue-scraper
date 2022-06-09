
# Bulk Data Scraper for UK Companies 

Scrapes the following data:
['Total Assets', 'Total Liabilites', 'Net Assets', 'Cash In Bank', 'Employees', 'Turnover', 'Debt Ratio', 'No of Directors'


## Usage/Examples

Use excel (xlsx) to provide an import file which contains a list of company numbers on column A

```PYTHON
read_file = "/Users/FileLocation"
```

Then change the letter 'x' depending on how much companies there are to scrape.
Typically 1000 companies take around 3 mins.

```PYTHON
for i in range(1, x):
```
