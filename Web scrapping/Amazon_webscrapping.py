import requests
from bs4 import BeautifulSoup

#amazaon website url
url = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

#Amazon product smart home
url_1 = "https://www.amazon.com/s?k=smart+home&ref=nav_bb_sb"

#sending request to get text of the amazon front page 
response_frontpage = requests.get(url)
print(response_frontpage.text)

response_smarthome = requests.get(url_1)
print(response_smarthome)

