import requests
from bs4 import BeautifulSoup


def check_covid():
    data = []
    url = "http://ncov.mohw.go.kr/"
    res = requests.get(url)
    xml = res.text

    soup = BeautifulSoup(xml, 'html.parser')
    date = soup.find('span', class_='livedate').text
    #datalist = soup.find('div', class_='occur_num').findAll('div')
    #for i in datalist:
    #    data.append(i.find('span', class_='data').text)
    #accumulated = soup.find('ul', class_="liveNum")
    #datalist = accumulated.findAll('span', class_='num')
    #for i in datalist:
    #   data.append(i.text)

    return date, data
