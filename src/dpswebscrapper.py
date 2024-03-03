# import click
import requests
from bs4 import BeautifulSoup

def coliint():
    #  Scraping the crime pdf from DPS website
    link = "https://dps.usc.edu/alerts/log/"
    getreq = requests.get(link)
    assert getreq.ok

    # Scraping out the PDF links from the web response
    linksoup = BeautifulSoup(getreq.content, "html.parser") 
    pdflist = [a for a in linksoup.find_all('a') if a['href'].endswith(".pdf")]
    historical_crime_historylist = [a for a in pdflist if "current" in a.text.lower()][0]["href"]


    print(historical_crime_historylist)

    


if __name__ == "__main__":
    coliint()
