import requests
from lxml import etree as et
response = requests.get('https://news.google.com/rss?x=1571747254.2933&hl=en-US&gl=US&ceid=US:en')
print(type(response.content))
# tree = et.parse('response.content')
# root = tree.getroot()
# print(root)
