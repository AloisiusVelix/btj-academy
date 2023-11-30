from flask import Flask
app = Flask(__name__)

@app.route('/Velix')
def hello_velix():
    return 'Hello, Velix!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5555)
