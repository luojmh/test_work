"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
mitmdump -s
"""

from mitmproxy import ctx, http

class Counter:

    def request(self, flow:http.HTTPFlow):
        # 使用request事件实现 MapLocal
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("xueqiu.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "text/html"}  # (optional) headers
                )

    def response(self,flow:http.HTTPFlow):
        pass

addons = [
    Counter()
]