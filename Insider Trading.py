# Import requirements
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import urllib.request

# Function to download given file 
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

# inurl is a set that contains 3 strings. 
inurl = ["insider trading policy", "upsi", "unpublished price sensitive information"]
downloaded = 0
query = ""

# The only parameter we need to change is the company name. 
# Forming a query with company name + x (eg. AIA ENGINEERING LTD INSIDER TRADING POLICY)
for x in inurl:
    a = "20 MICRONS LTD."
    a = a.replace(".","")
    query = a + x

# Finding the first three results on searching query on google 
    for j in search(query, tld="co.in", num=3, stop=3, pause=5):
        url = j
        if url.lower().find('.pdf') != -1: # If link is pdf, download it. 
            download_file(url, a)
            downloaded = 1
            break
# If obtained link is not a pdf,parse the page. 
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
# Find the links with extention .pdf. 
        anchors = soup.select("a[href$='.pdf']")
        for link in anchors:
            pdflink = link.get('href')
# Finding the keywords, inside, insider, trading policy in the pdf, if found download it. 
            if pdflink.lower().find('inside') != -1:
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
            elif pdflink.lower().find('insider') != -1:
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
            elif pdflink.lower().find('tradingpolicy') != -1:
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
    if downloaded == 1 :
        print("pdf downloaded")
        downloaded = 0
        break