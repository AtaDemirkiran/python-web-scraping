import requests
from bs4 import BeautifulSoup


httpRequest=requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm')

html = httpRequest.content

parsedHtml=BeautifulSoup(html,"html.parser")
# kodları parse ediyoruz
salaries=parsedHtml.find_all("div",{"data-test":"median-base-salary"})

for salary in salaries:
    print(salary.text)