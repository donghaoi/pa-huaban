import time
import requests
import json
import re
import os


class HuaBan(object):

    def __init__(self):
        self.url = "https://huaban.com/search/?"
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Referer': 'https://huaban.com/search/?q=%E5%8F%A4%E8%A3%85',
        'Cookie': 'flowerCount=1; referer=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0770Pt_gXKcIqPK3zApC5XVkzU41scgLRkc7QWGhINC%26wd%3D%26eqid%3D8805a1c1000011e00000000360a1de37; sid=s%3Aan7d3r566BUGHCOfNX-eh3-jyZNDt1hK.X1ABiqbWnjrLud4QVRlk90YoXgStX25lJsuMyRmmW4I; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAACuUlEQVRYR%2B2WT0gUURzHP287FCpKhyQINZIOmUGQk0jBjBERGd3yICQFSXQITYKsQwcvegjapVvboQw8FBFEWUS1sxCIrh2CtCCMTAjJCoJYpNAXv9lZWNfdcdRZSWhOD9533vt%2Bfv9mFFprvB6llOf%2BKm2Gf4Q9fSoBKUomiba1OZbaIxEi7e3Oui0aJVlc7AmioQiIAjcUxAvF5QtELjfjKQ9x05y3xkdGNOwAhHjknwPZMDNDa18fLf39FjAK3AYuABNuBlqAfkkcUAU0AFeAKeAokMyhk%2F1S4Ehap%2BCbH%2FglZcS2xHPqsWybr%2BXljNXUGBJpDceBt0C57EsZ6ZShYWATcM4FNTKNeeia5DwF7wIHyS6tPCDTwCOgHhhyoy8gTmm5ZVYLxPLoahXcSwdmNUGa3YsvAw8AMSmZkRKTUrnqZiRt0HQjLJnz0jkZDhQkc2pd6unhbnMz49XVdPX28rmyUqIu0X8KvAGeALYLMgCUAd3AKeBiRt9IiWXrpH%2F2ASeBW7KvoCvQ0sp7mI%2Bp5cfISjW%2Bm%2F0%2FyEpD7fP9gmREx4cOoFWf40HpVvS66zBXJmtl1r%2FM9qbtkVHQNaDGlFW3M593L102iPllGx9LvzNZ8jNlY7n%2FWtoe7ga1W1nGMW0nzjuHWca1hRCOrklZxh5tJ16DfqysvTLt5j3ueXl1aZCKX2UcmtzuvPus4kMQIIkTKM4o09ivYyNhQrMPc2YjnnjOHJ9Uo3FaxxI3CbFVmcbBBSCL6DIzIjANU1UMbp5YOYgY0fHEKzT30apKNdZ15CoZvSZAJMLK%2Bc8ayFVWLuwayEiqT84Cncoy7uTMSEoTWI%2FIHQUoLZleoQ5peK8pmj2NnF5R%2BnD2lPPSRXYNvkhDSLOX%2FFnP79AssS3jvN84vfyp5XP8ByYryHckMHdLOGgxkL8g0%2BMoiUoFIQAAAABJRU5ErkJggg%3D%3D%2CWin32.1920.1080.24; _uab_collina=162122092106443335994661; UM_distinctid=179784c0f3246b-0c8a5ebb168302-2363163-1fa400-179784c0f33916; CNZZDATA1256903590=1392307910-1621216776-https%253A%252F%252Fwww.baidu.com%252F%7C1621216776; __asc=d8fba831179784c12b51c588f6d; __auc=d8fba831179784c12b51c588f6d; __gads=ID=309f5f92dbe484cb:T=1621220926:S=ALNI_MaqK6qgKTDxsF9_Wwtyi1cM7sZGdg; CNZZDATA1279796125=1037052495-1621219298-https%253A%252F%252Fhuaban.com%252F%7C1621219298; _ga=GA1.2.870236201.1621220934; _gid=GA1.2.1392806091.1621220934; BAIDU_SSP_lcr=https://www.baidu.com/link?url=YcrkUOs6trKqtX6ITCck5NOr8kwDSKIljxjF5-hYI-K&wd=&eqid=91f79901000018a60000000360a1dee6; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1621220921,1621220974,1621221095; uid=30893018; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1621221159253%26urlname%7Cy3qkysnq5z%7C1621221159253; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1621221158'
        }
        self.session = requests.session()


    def params_one(self, page):
        params = {
            "q": self.c,
            "ki4kgpwa": "",
            "page": page,
            "per_page": "20",
            "wfl": "1",
        }
        return params

    def index_spider(self, params_ret):
        response = self.session.get(url=self.url,params=params_ret, headers=self.headers).text
        demo = ''.join(re.findall('pins"] = (.*);', response))
        haha = json.loads(demo)
        for demo in haha:
            item = {}
            item['demo'] = demo
            yield item



    def save_data(self, index_item):
        aaa = 0
        for item in index_item:
            tupian = item['demo']["file"]["key"]
            tupian_url = "https://hbimg.huabanimg.com/" + tupian + "_fw658/format/webp"
            xiazai = requests.get(tupian_url)
            aaa += 1
            try:
                with open("????????????????????????/" + tupian + ".jpg","wb") as a:
                    print("???????????????%s?????????"%aaa)
                    a.write(xiazai.content)
            except:
                print("???????????????")

    def main(self):
        try:
            self.c = input("???????????????????????????")
            a = int(input("?????????????????????"))
            b = int(input("?????????????????????"))
            if not os.path.exists("????????????????????????"):
                print("?????????????????????...")
                os.makedirs("????????????????????????")
                time.sleep(2)
            for page in range(a,b):
                # page = 5
                params_ret = self.params_one(page)
                index_item = self.index_spider(params_ret)
                self.save_data(index_item)
                print("???%s????????????????????????" %page)
            print("\n\n???????????????????????????????????????????????????~")
            time.sleep(2)
        except:
            print("????????????????????????????????????????????????????????????????????????????????????")
            time.sleep(5)


if __name__ == '__main__':
    huaban = HuaBan()
    huaban.main()


