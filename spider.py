import random 
import requests
import re

# craw the html page
def get_html(url,params):
    uapools=[
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14'      
        ]
    thisua=random.choice(uapools)
    headers={'User-Agent':thisua}
    r = requests.get(url,params=params,headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    r.encoding = 'utf-8'
    
    return r.text
 # pase the html page1
 
def parse_page(infolist, data):
     commentpat = '"content":"(.*?)"'
     lastpat = '"last":"(.*?)"'
     commentall = re.compile(commentpat,re.S).findall(data)  
     next_cid = re.compile(lastpat).findall(data)[0]  
     infolist.append(commentall)
     return next_cid  
 
 
 ## parse the html page2
def print_comment_list(infolist): 
    j=0
    for page in infolist:
        print('第' + str(j + 1) + '页\n')     
        commentall = page
        for i in range(0, len(commentall)):
            print(commentall[i]+'\n')
        j +=1
        
## save the content to a txt file
def save_to_txt(infolist,path):
    fw = open(path, 'w+', encoding='utf-8')
    j = 0
    for page in infolist:
        commentall = page
        for i in range(0, len(commentall)):
            fw.write(commentall[i]+'\n')
        j = j + 1
    fw.close()
# finally call the logic
# one funtion a indentation
def main ():
    infolist=[]
    vid="7579013546"
    cid='0'
    page_num=3000
    url='https://video.coral.qq.com/varticle/' + vid + '/comment/v2'
    # print(url)
    
    # one for loop one indention
    for i in range(page_num):
        params = {'orinum':'10', 'cursor':cid}
        # print(params)
        html= get_html(url,params)
        # print(html)
        cid = parse_page(infolist,html)
        # print(cid)
        
    print_comment_list(infolist)
   
    save_to_txt(infolist,'content.txt')
   
main()
    
    
    