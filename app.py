from flask import Flask,render_template, request
from summary import summarizer

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("base.html")
@app.route("/summary",methods=['GET','POST'])
def summary():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,original_txt,len_orig_text,len_summary =summarizer(rawtext)
    return render_template('summary.html',summary=summary,original_txt=original_txt,len_orig_text=len_orig_text,len_summary=len_summary)

if __name__=="__main__":
    app.run(debug=True)