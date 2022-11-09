from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "There's going to be a library here soon"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')