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
def covid_nationNm():
    for item in items:
        nationNm.append(item.find('nationnm').get_text())

    return nationNm

#국가명_영어
def covid_nationNmEn():
    for item in items:
        nationNmEn.append(item.find('nationnmen').get_text())

    return nationNmEn       

