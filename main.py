import pandas as pd
import requests as req
import bs4
import lxml

def Main():
    result = req.get('https://www.worldometers.info/coronavirus/country/india/')
    soup = bs4.BeautifulSoup(result.text,'lxml')
    cases = soup.find_all('div',class_='maincounter-number')
    # print(cases) -> No of active cases
    data = []
    for i in cases:
        span = i.find('span')
        data.append(span.string)
    # print(data)
    df = pd.DataFrame({'covid_data':data})
    df.index = ['Total Cases','Deaths','Recovered']
    print(df)
    df.to_csv('Covid-19_Data.csv')


if __name__ == '__main__' : Main()
