from flask import Flask, render_template, request, jsonify
from Code import check_password_strength

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login logic here
    return 'Login successful'

@app.route('/check_strength', methods=['POST'])
def check_strength():
    data = request.get_json()
    email = data['email']
    password = data['password']

    strength = check_password_strength(password)
    return jsonify(strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
