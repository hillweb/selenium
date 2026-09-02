# 读取accounts.json文件
import json
from datetime import datetime
#import asyncio

def read_accounts():
    json_data=json.load(open('accounts.json'))
    results=[]
    for email in json_data:
        for domain in json_data[email]:
            expire_dates=json_data[email][domain]
            results.append({'email':email,'domain':domain,'expire_dates':expire_dates})
    # 排序
    results.sort(key=lambda x: x['expire_dates'])
    return results
#json 转csv
def json_to_csv(results):
    import csv
    with open('accounts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['email', 'domain', 'expire_dates'])
        for account in results:
            writer.writerow([account['email'], account['domain'], account['expire_dates']])
# 打印结果
def get_expire_accounts(results):
    """
    获取过期账号:返回结果格式为
    {
        "lookchary@outlook.com": [
            "papers.dpdns.org",
            "rtian.qzz.io"
        ],
        "manuel@eduppp.cn": [
            "zea.qzz.io"
        ]
    }
    """
    expire_accounts={}
    for account in results:
        email=account['email']
        domain=account['domain']
        expire_dates=account['expire_dates']
        expire_dates=datetime.strptime(expire_dates, '%Y-%m-%d')
        today=datetime.now()
        delta=(expire_dates-today).days
        if delta<120:
            print(f"{email} {domain} 续期已过{120-delta}天")
            if email not in expire_accounts:
                expire_accounts[email]=[domain]
            else:
                expire_accounts[email].append(domain)
    return expire_accounts
if __name__ == '__main__':
    json_data=read_accounts()
    expire_accounts=get_expire_accounts(json_data)
    expire_keys=expire_accounts.keys()
    print(f"共{len(expire_keys)}个账号过期")
    if len(expire_keys)>0:
        print(json.dumps(expire_accounts, ensure_ascii=False, indent=4))
        # results={}
        # for email in expire_keys:
        #     results[email]={}
        #     domainlist=expire_accounts[email]
        #     print(f"{email} {domainlist} ")
        #     # continue
        #     # 执行程序domains.py
        #     _result=asyncio.get_event_loop().run_until_complete(domains.login(email,domainlist))
        #     results[email].update(_result[email])
        #         # 更新accounts.json
        # domains.update_accounts(results)


