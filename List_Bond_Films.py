from urllib.request import urlopen
from bs4 import BeautifulSoup
import fileinput
import sys

url = "https://www.pocket-lint.com/tv/news/148096-james-bond-007-best-movie-viewing-order-chronological-release"
html = urlopen(url)
soup = BeautifulSoup(html, 'html')
# soup.contents
Bond_Film_Quick_List = soup.find("p", string="This is the same list as above, only spoiler-free and much quicker to read:")
Bond_Film_Date_List=Bond_Film_Quick_List.next_sibling.text
print (Bond_Film_Date_List)
exit()
