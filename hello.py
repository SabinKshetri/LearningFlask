from flask import Flask, render_template,request,redirect


app = Flask(__name__)

@app.route("/")
def hello_world():
    return  render_template('pages/home.html')


@app.route("/login")
def login2():
    return render_template('pages/login.html')

@app.route("/login",methods=['POST'])
def sigin():
    username=request.form['username']
    password=request.form['password']
    if username=='sabin' and password=='sabin123':
        return redirect('/')
    else:
        return redirect('/login')
   


if __name__=='__main__':
    app.run(debug=True)
















