#Create a simple flask application
from flask import Flask,redirect,url_for,render_template,request

##create the flask app

app=Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
    return "Hello World, I done it"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "<h4>the person is pass and score is: </h4>"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "<h4>the person is fail and score is: <h4>"+str(score)


@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        result=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"
            
        #return redirect(url_for(result,score=average_marks))
        return render_template('calculate.html',results=average_marks)


    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)


