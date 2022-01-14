import requests
import time
#нет комментариев и фотографий


def main():
    before= time.time()
    url="https://jsonplaceholder.typicode.com/users"
    u=requests.get(url)
    users=u.json()
    for i in range(len(users)):
        user_hist(i+1)
       
    print(time.time()-before)

def user_hist(k):
    
    url=f"https://jsonplaceholder.typicode.com/users/{k}"
    r=requests.get(url)
    if r.status_code==200:
        _r=r.json()
        print(_r)
   
    url_p=f"https://jsonplaceholder.typicode.com/users/{k}/posts"
    p=requests.get(url_p)
    if p.status_code==200:
        _p=p.json()
        print(_p)
            
           

    url_a=f"https://jsonplaceholder.typicode.com/users/{k}/albums"
    a=requests.get(url_a)
    if a.status_code==200:
        _a=a.json()
        print(_a)   
    
    url_t=f"https://jsonplaceholder.typicode.com/users/{k}/todos"
    t=requests.get(url_t)
    if t.status_code==200:
        _t=t.json()
        print(_t) 
              

main()