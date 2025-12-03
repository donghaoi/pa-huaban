import time
import urllib3
import requests
import json
import re
import os
# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class HuaBan(object):

    def __init__(self):
        self.url = "https://huaban.com/v3/search/file?"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'Referer': 'https://huaban.com/',
            'Cookie': 'user_device_id=c55d5c38b0c44e96baa059ad25d56d24; fd_id=e18f34fa4f53e18c9e32e13fe432adbc; fd_id_timestamp=1752054586031; canary_uuid=bc9c3e4570125bd78501dd4eb0cc4a90; canary=.?base; huaban-page-setting={%22cols%22:9%2C%22columnSize%22:240}; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1763516607,1764668270; HMACCOUNT=EE50C3B70B3CC054; _clck=1eivfn6%5E2%5Eg1i%5E0%5E2128; locale=zh-cn; token.prod=eyJ1c2VyX2lkIjozMDE1MTkwNTUsImh1YWJhbl9pZCI6MzgzMzIyNTcsInVzZXIiOjMwMTUxOTA1NSwiYWNjZXNzX3Rva2VuIjoiZXlKMGVYQWlPaUpxZDNRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SnBjM01pT2lKMWJYTWlMQ0p6ZFdJaU9qTXdNVFV4T1RBMU5Td2lZWFZrSWpvaWFIVmhZbUZ1SWl3aVpYaHdJam94TnpZME9USTNOalF6TENKMVkybGtJam9pT1RBek1UVXhOVEF6TURVME1ETTJPVGt6T1NJc0ltcDBhU0k2SWpGeGFuWnhlWGRwWlc4aUxDSm9ZbDlwWkNJNklqTTRNek15TWpVM0luMC5JT1Z5LXk4V0lvOWdGN00tYS1xU2tHdkh4eW05WU5wQjJYb0RMM3JsazRBIiwicmVmcmVzaF90b2tlbiI6Ik56d1U1aXI5Uk1Lb1R2UUEwd0ZnREEiLCJhY2Nlc3NfdG9rZW5fZXhwaXJlc19hdCI6IjIwMjUtMTItMDVUMDk6NDA6NDMuMDAwWiIsInJlZnJlc2hfdG9rZW5fZXhwaXJlc19hdCI6IjIwMjYtMDEtMDFUMDk6NDA6NDMuNzY4WiIsImFjY2Vzc190b2tlbl9saWZlX3RpbWUiOjI1OTIwMCwicmVmcmVzaF90b2tlbl9saWZlX3RpbWUiOjI1OTIwMDAsInRpbWVzdGFtcCI6MTc2NDY2ODQ0Mzg1MywibWVyZ2VkIjp0cnVlfQ==; token.prod.sig=KbR-4FaJBFbrxkRpZpows4WXSWJR_cVBA50rAdhQYkI; referer=https%3A%2F%2Fwww.gaoding.art%2F; sid=s%3Aikm4IH2k6uD83u2uwVMyc6FBrIgFwOHM.q10l6zu3VE%2BSIzCWXMwRMDAh4l8C%2FpX%2FCvUokUDE0Z4; uid=38332257; gd_id=2026463727255459901; token.org_id.prod=8031514056138794062; ab_test_id=40e5e42da030d25e9ecc52cddccf1e5b; feature_page=%257B%2522all%2522%253A5%257D; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1764668454; _clsk=10eoxhy%5E1764668594776%5E14%5E0%5En.clarity.ms%2Fcollect',
            'guest-token': 'c55d5c38b0c44e96baa059ad25d56d24',
            'Accept': 'application/json, text/plain, */*',  # 修正为大写
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Csrf-Token': '0fab09599529e9c612ecb2a51efc',
            'Origin': 'https://huaban.com'
        }
        self.session = requests.session()


    def params_one(self, img_type,page_num,page):
        params = {
            "text": img_type, # 关键字
            "sort": "all",
            "limit": page_num,  # 每页显示图片个数
            "page": page, # 爬取第几页
            "position": "search_pin",
            "fields": "pins:PIN|total,facets,split_words,relations,rec_topic_material,topics",
        }
        return params

    def index_spider(self, params_ret):
        response = self.session.get(url=self.url,params=params_ret, headers=self.headers,timeout=15,verify=False).text
        data = json.loads(response)
        data_list = data["pins"]
        img_list= []
        for i in data_list:
            if 'file' in i:
                url = "https://gd-hbimg.huaban.com/" + i['file']['key'] + "_fw480webp"
            img_list.append(url)
        return img_list



    def save_data(self, img_urls):
        try:
            b = 0
            for i in img_urls:
                b += 1
                xiazai = requests.get(url=i, headers=self.headers,timeout=15,verify=False)
                img_name = str(img_urls[0]).split("/")[-1].replace("webp", ".webp", 1).replace("fw480","_fw480" + str(b))
                print(img_name)
                with open("图片爬取存储位置/" + img_name ,"wb") as a:
                    a.write(xiazai.content)
                    print("第" + str(b) + "张图片下载完成")
        except Exception as e:
            print('图片下载失败，错误：' + str(e))

    def main(self):
        img_type = input("请输入抓取图类型：")
        page_num = input("请输入每页爬取的个数：")
        page = input("请输入爬取第几页：")
        if not os.path.exists("图片爬取存储位置"):
            print("正在创建文件夹...")
            os.makedirs("图片爬取存储位置")
            time.sleep(2)
        params_ret = self.params_one(img_type,page_num,page)
        img_urls = self.index_spider(params_ret)
        self.save_data(img_urls)
        time.sleep(2)


if __name__ == '__main__':
    huaban = HuaBan()
    huaban.main()


