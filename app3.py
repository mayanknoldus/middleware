from flask import Flask

app = Flask(__name__)    

@app.route('/')
def index():
    return 'Hello from server 3'

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')
