from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello,World!</h1>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)

@app.route('/user/<usernaem>')
def show_user_profile(username):
    return f'User{escape(username)}'

@app.route('/factorial/<int:input_val>')
def show_factorial(input_val):
    factorial = compute_factorial(input_val)
    return render_template('factorial.html',
           input = input_val
           factorial=factorial  )
