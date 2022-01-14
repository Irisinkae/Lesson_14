import requests
import time
import aiohttp
import asyncio
#нет комментариев и фото в альбомах

async def main():
    before= time.time()
    url="https://jsonplaceholder.typicode.com/users"
    u=requests.get(url)
    users=u.json()
    for i in range(len(users)):  #len(users)
        await user_hist(i+1)
    print(time.time()-before)

async def user_hist(k):
    
    url=f"https://jsonplaceholder.typicode.com/users/{k}"
    url_p=f"https://jsonplaceholder.typicode.com/users/{k}/posts"
    url_a=f"https://jsonplaceholder.typicode.com/users/{k}/albums"
    url_t=f"https://jsonplaceholder.typicode.com/users/{k}/todos"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status==200:
                _r=await resp.json()
                print(_r)

        async with session.get(url_p) as p:
            if p.status==200:
                _p= await p.json()
                print(_p)

        async with session.get(url_a) as a:
            if a.status==200:
                _a= await a.json()
                print(_a)    

        async with session.get(url_t) as t:
            if a.status==200:
                _t= await t.json()
                print(_t)           
        
   


loop = asyncio.get_event_loop()
loop.run_until_complete(main())