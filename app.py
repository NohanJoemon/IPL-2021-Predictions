from flask import Flask, render_template, request
import predictor
import os

app = Flask(__name__)

# set paths to upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['Models'] = os.path.join(APP_ROOT, 'Training')

@app.route("/", methods=["GET","POST"])
def predict():
    venues=['M.Chinnaswamy Stadium',
            'Arun Jaitley Stadium',
            'Wankhede Stadium',
            'MA Chidambaram Stadium',
            'Eden Gardens',
            'Narendra Modi Stadium']
    teams= ['Kolkata Knight Riders',
            'Royal Challengers Bangalore',
            'Rajasthan Royals',
            'Delhi Capitals',
            'Mumbai Indians',
            'Chennai Super Kings',
            'Punjab Kings',
            'Sunrisers Hyderabad']
    preds=None
    model_hashtable=None
    selected=None
    if request.method  == "POST":
        hashmap={}
        hashmap["venue"]=str(request.form["venue"])
        hashmap["innings"]=int(request.form["innings"])
        hashmap["batting_team"]=str(request.form["batteam"])
        hashmap["bowling_team"]=str(request.form["bowlteam"])
        hashmap["NumBatsmen"]=int(request.form["nbat"])
        hashmap["NumBowlers"]=int(request.form["nbowl"])
        preds,model_hashtable = predictor.predict([hashmap],app.config['Models'])
        selected=hashmap
    

    return render_template("index.html",preds=preds,model_hashtable=model_hashtable,venues=venues,teams=teams,selected=selected)

if __name__=="__main__":
    app.run(debug=True)