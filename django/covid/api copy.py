from tabnanny import check
from urllib.parse import urlencode, unquote, quote_plus
from xml.dom.pulldom import START_ELEMENT
import requests
from bs4 import BeautifulSoup
import bs4
from datetime import datetime, timedelta
import xmltodict

serviceKey = "OZ0AaA4R73jc3DCNYKWS0imRsCPAasq7HFpF4pKadbOVQ%2FzmJW2qUCQDQ7FUKpYdXtTKb53n%2B4XZtVWRp3eJMg%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')
yesterday = datetime.today() - timedelta(2)
day = yesterday.strftime("%Y%m%d")


#def check_covid():
    
url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson"
numOfRows="1"
pageNo="1"
startCreateDt= day
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('pageNo') : pageNo, quote_plus('numOfRows') : numOfRows, quote_plus('startCreateDt') : startCreateDt })
res = requests.get(url + queryParams)
xml = res.text
soup = bs4.BeautifulSoup(xml,'lxml')
items = soup.findAll('item')

areanm = []
natDeathCnt = []
natDefCnt = []
nationNm = []
nationNmEn = []

#대륙 딕셔너리
def covid_areanm():
    for item in items:
        areanm.append(item.find('areanm').get_text())

    return areanm

#누적사망자
def covid_natDeathCnt():
    for item in items:
        natDeathCnt.append(item.find('natdeathcnt').get_text())

    return natDeathCnt

#누적확진자
def covid_natDefCnt():
    for item in items:
        natDefCnt.append(item.find('natdefcnt').get_text())

    return natDefCnt

#국가명_한글

for item in items:
    nationNm.append(item.find('nationnm').get_text())



#국가명_영어
def covid_nationNmEn():
    for item in items:
        nationNmEn.append(item.find('nationnmen').get_text())

    return nationNmEn       


print(nationNm)


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




natDeathCnt = covid_natDeathCnt

print(natDeathCnt)