from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = "p7zGkmRh2x32vu%2BuvThZkvgWgBnug8qu2YB%2F3AQHyOERlV3SqETp1UPGubmd5La2plHZDURFlgotkT1ctC6b2g%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air():
    station = []
    pm10 = []
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson"
    returnType="xml"
    numOfRows="1"
    pageNo="1"
    startCreateDt="20200310"
    endCreateDt="20200320"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('pageNo') : pageNo, quote_plus('numOfRows') : numOfRows, quote_plus('startCreateDt') : startCreateDt, quote_plus('endCreateDt') : endCreateDt })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('areaNm'):
        station.append(tag.text)

    return xml
