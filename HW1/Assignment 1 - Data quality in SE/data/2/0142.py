import urllib2
import csv
from bs4 import BeautifulSoup
url = {
   "Home ": 'https://www.moneycontrol.com/',
#    "Market": 'https://www.moneycontrol.com/stocksmarketsindia/',
#    "Mf Home": 'https://www.moneycontrol.com/mutualfundindia/'
}
def get_last_element_timestamp(url):
    conn = urllib2.urlopen(url)
    html = conn.read()
    soup = BeautifulSoup(html,"lxml")
    elements = soup.find_all('div')[-1]
    return elements.text

def historic_data(url):
    csv_data = urllib2.urlopen(url)
    csv_reader = list(csv.reader(csv_data, delimiter=','))
    return (csv_reader[-1])

for page,url_value in url.items():
   print (page,get_last_element_timestamp(url_value))
#    print page
##
bse_info_csv="http://www.moneycontrol.com/tech_charts/bse/his/it.csv"
nse_info_csv = "http://www.moneycontrol.com/tech_charts/nse/his/it.csv"
historic_sensex = "http://www.moneycontrol.com/tech_charts/bse/his/sensex.csv"
historic_nifty = "http://www.moneycontrol.com/tech_charts/nse/his/nifty.csv"
print("Historic csv infosys  => BSE")
print(historic_data(bse_info_csv))
print ("Historic csv of infosys => NSE")
print(historic_data(nse_info_csv))  
print ("Historic csv of sensex ")
print(historic_data(historic_sensex))
print ("Historic csv of nifty")
print (historic_data(historic_nifty))  




