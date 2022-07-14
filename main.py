from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)






@app.route("/")
def sample():
    return render_template('index.html')


@app.route("/fun/")
def fun():
    model = {"title": "Hey here is your fun Fact "}
    return render_template('fun.html', model=model)

@app.route("/Data")
def data():
    return render_template('student.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)    



if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
