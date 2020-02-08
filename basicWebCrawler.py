import requests
from bs4 import BeautifulSoup

r = requests.get('https://theinternship.io/')
s = BeautifulSoup(r.text, 'lxml')
d = s.find('div', {'id':'__nuxt'})
a_tags = d.find_all('a')
span_tags = d.find_all('span')
a_tags = a_tags[:-3]
length_of_description = []
data = []
for i in range(len(a_tags)):
    length_of_description.append([a_tags[i].find('img')['src'], len(str(span_tags[i]))])
length_of_description.sort(key=lambda x: x[1])
for i in length_of_description:
    print(i[0])
    data.append(i[0])
main_api = 'http://maps.googleapis.com'