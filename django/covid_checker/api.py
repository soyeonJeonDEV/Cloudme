from tabnanny import check
from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xmltodict

serviceKey = "p7zGkmRh2x32vu%2BuvThZkvgWgBnug8qu2YB%2F3AQHyOERlV3SqETp1UPGubmd5La2plHZDURFlgotkT1ctC6b2g%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')
today = datetime.today().strftime("%Y%m%d")

def check_covid():
#    info = []
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
    numOfRows="1"
    pageNo="1"
    startCreateDt= today


    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('pageNo') : pageNo, quote_plus('numOfRows') : numOfRows, quote_plus('startCreateDt') : startCreateDt })
    res = requests.get(url + queryParams)
    xml = res.text
 #   soup = BeautifulSoup(xml, 'html.parser')
    xmlObject = xmltodict.parse(xml)
    allData = xmlObject['response']['body']['items']['item']

    return allData

url = 'http://ncov.mohw.go.kr/' # 사이트 링크

response = requests.get(url) 
html = response.text
soup = BeautifulSoup(html, 'html.parser')

def mail():
   mail_data = str(soup.select_one('#content > div > div > div > div.liveToggleOuter > div > div.live_left > div.occurrenceStatus > div.occur_graph > table > tbody > tr:nth-child(1)'))
   xmlObject = xmltodict.parse(mail_data)
   return xmlObject
