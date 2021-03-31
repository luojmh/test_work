
from mitmproxy import ctx,http
class AD:
    def requests(self,flow:http.HTTPFlow):
        url=flow.request.pretty_url
        method = flow.request.method
        with open("template.txt") as f:
            data = f.read()
            new_data = data.format(method=method,url=url)
        with open("template.py","w",encoding='utf-8') as f:
            f.write(new_data)

    def reponse(self, flow:http.HTTPFlow):
        pass

addons = [
    AD()
]