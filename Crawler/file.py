from bs4 import BeautifulSoup
import requests
from string import punctuation

doclist=['doc1.txt','doc2.txt','doc3.txt','doc4.txt','doc5.txt','doc6.txt','doc7.txt','doc8.txt','doc9.txt','doc10.txt','doc11.txt','doc12.txt']
links=['https://www.zigwheels.com/newcars/Tesla',' https://www.financialexpress.com/auto/car-news/mahindra-to-launch-indias-first-electric-suv-in-2019-all-new-e-verito-sedan-on-cards/1266853/',
       ' https://en.wikipedia.org/wiki/Toyota_Prius','https://economictimes.indiatimes.com/industry/auto/auto-news/government-plans-new-policy-to-promote-electric-vehicles/articleshow/65237123.cms',
       ' https://indianexpress.com/article/india/india-news-india/demonetisation-hits-electric-vehicles-industry-society-of-manufacturers-of-electric-vehicles-4395104/',
       ' https://www.livemint.com/Politics/ySbMKTIC4MINsz1btccBJO/How-demonetisation-affected-the-Indian-economy-in-10-charts.html',' https://www.hrblock.in/blog/impact-gst-automobile-industry-2/',
       ' https://inc42.com/buzz/electric-vehicles-this-week-centre-reduces-gst-on-lithium-ion-batteries-hyundai-to-launch-electric-suv-in-india-and-more/',
       'https://www.youthkiawaaz.com/2017/12/impact-of-demonetisation-on-the-indian-economy/','https://indianexpress.com/article/india/demonetisation-effects-cash-crisis-mobile-wallets-internet-banking-4406005/',
       ' https://www.news18.com/news/business/how-gst-will-curb-tax-evasion-1446035.html','https://economictimes.indiatimes.com/small-biz/policy-trends/is-gst-helping-the-indian-economy-for-the-better/articleshow/65319874.cms']
for i in range(len(doclist)):
    page=requests.get(links[i])
    soup=BeautifulSoup(page.text,'html.parser')
    p_tags=soup.find_all('p')
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    f=open(doclist[i],'w')
#f.write("abc")
    gen=[str(y.lower()) for y in text ]
    count=0
    print(len(gen))
    for t in gen:
        f.write(t)
        count=count+1
        if count>=500:
            break
    print(type(text))
    f.close()
