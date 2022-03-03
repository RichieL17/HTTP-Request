from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, my name is Richie! This is my HTTP Request.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')