from flask import Flask,render_template
app =Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/reg')
def Registration_form():
    return render_template('reg.html')

@app.route('/sign')
def sign_form():
    return render_template('signup.html')

@app.route('/about')
def about_form():
    return render_template('AboutUs.html')

if __name__ =="__main__":
    app.run(debug=True)