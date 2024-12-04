from math import sqrt
from flask import Flask, redirect, render_template, request, jsonify

def f(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return "無解"
    else:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
    if x2 > x1:
        x1, x2 = x2, x1
    return "x="+str(x1)+" or "+str(x2)
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        try:
            res = f(float(request.form.get("a")), float(request.form.get("b")), float(request.form.get("c")))
            return "計算結果："+res+'<br><input type="button" value="回首頁" onclick="location.href=\'/\';">'
        except Exception as e:
            print(e)
            return '發生錯誤，請重試<br><input type="button" value="回首頁" onclick="location.href=\'/\';">'  
    else:
        return render_template("index.html")

app.run("0.0.0.0", "80")