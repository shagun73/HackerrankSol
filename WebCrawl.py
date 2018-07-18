from bs4 import BeautifulSoup as bsoup   
import requests as rq
import re
import os

# performing the webcrawling using BeautifulSoup and storing the required values in the form of a dictionary.
def website_crawler():
    dictval = {}
    req = rq.get('http://apps.leg.wa.gov/wac/default.aspx?cite=296-17A&full=true')
    soup = bsoup(req.content,from_encoding="latin-1")
    link = soup.find(id="ctl00_ContentPlaceHolder1_dlSectionContent")
    spanlinks = link.find_all('span')
    
    for sl in spanlinks:
        for reqtext in sl.find_all('span',text=re.compile("^[0-9]{4}-[0-9]{2} ")):
            spanText =(reqtext.text).encode('utf-8')
            key,value = spanText.split(' ', 1 )
            dictval[key] = value
    return dictval

# to store the results from webcrawling into the file located at the given filepath from the user.
def storing_result(dictval,filepath):
    try:
        with open(filepath,"+") as f:
            f.write(dictval)
    except (Exception,e):
        print("Error occured: %s",e)
        return False
    return True

if __name__ == '__main__':
    path = raw_input("Please provide location to store the output file: ")
    if not os.path.exists(path):
        print("Incorrect path.")
    else:
        path = os.path.join(path,"wa_gov.txt")  # wa_gov.txt is the file having the required values.
        dictionaryval = website_crawler()
        success = storing_result(str(dictionaryval),path)
        if success:
            print("Successfully stored.")
        else:
            print("Failure.")
    