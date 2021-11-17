from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route("/data", methods=["POST","GET"])
def index():
    d={"Q No.":[],"Answers":[]}
    if request.method=="POST":
        for i,j in request.form.items():
            d["Q No."].append(i)
            d["Answers"].append(j)
        df=pd.DataFrame(d)
        print(df)
        df.to_excel("D:/SVCE_RESULTS.xlsx")
        return d
    else:
        k=request.args.get("n1")
        return k+"k"
if __name__=="__main__":
    app.run(debug=True)
