from flask import Flask, render_template
from flask import request as rq
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/short-url",methods=['POST'])
def shorturl():
    url = rq.form['url']
    import os
    import sys
    import urllib.request
    import json
    client_id = "siw0feyLzxZjq6KMHPAE" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "YhKNkXALPc" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(url)
    data = "url=" + encText
    url = "https://openapi.naver.com/v1/util/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        string = response.read().decode('utf-8')
        result = json.loads(string)
        result = (result['result']['url'])
    else:
        result="Error Code:" + rescode
    return render_template("short-url.html",result=result)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
