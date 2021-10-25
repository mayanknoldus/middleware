from flask import Flask

app = Flask(__name__)    

@app.route('/')
def index():
    return 'Hello from server 1'
@app.route('/server1')
def index1():
    return 'Hello from server 1'
if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
