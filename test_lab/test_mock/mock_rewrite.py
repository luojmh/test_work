"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
mitmdump -s
"""
import json

from mitmproxy import ctx, http


from mitmproxy import ctx


class Counter:

    def request(self, flow:http.HTTPFlow):
       pass

    def response(self,flow:http.HTTPFlow):
        # 实现rewrite
        # flow.response.text 是str 属性，所以要操作这个对象必须转换为python字典的数据结构
        list=[-100,-1,-0.1,0,0.1,1,100]
        for i in range(len(list)):
            if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
                data = json.loads(flow.response.text)
                data["data"]["items"][i]["quote"]["percent"]=list[i]
                flow.response.text = json.dumps(data)

addons = [
    Counter()
]