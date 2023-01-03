from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route("/",methods=["POST",'GET'])
def fun():
    temp=None
    if request.form.get("input")!=None:
        code=request.form.get("input")
        url="https://api.mfapi.in/mf/"+code
        resp=requests.get(url)
        temp=resp.json()
    return render_template("index.html",data1=temp)

@app.route("/api",methods=["POST","GET"])
def fun1():
    code=request.json.get("input")
    url="https://api.mfapi.in/mf/"+str(code)
    resp=requests.get(url)
    temp=resp.json()
    return temp
 



if __name__=="__main__":
    app.run(debug=True)