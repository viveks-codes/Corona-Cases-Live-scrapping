
import requests 
from lxml import html 
url = 'https://www.mohfw.gov.in/'

# path to particular element 
liveCase= '//*[@id="site-dashboard"]/div/div/div/div/ul/li[1]/strong'

r= requests.get(url) 

# get byte string 
htmlCode= r.content 

#filter
source_code = html.fromstring(htmlCode) 
# jump to preferred html element 
tree = source_code.xpath(path) 

# print texts in first element in list 
print(tree[0].text_content()) 
