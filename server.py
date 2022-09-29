from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello")
    return "Hello World!"

@app.route('/dojo')
def dojo():
    print("dojo")
    return "Dojo!"

@app.route('/hi_user/<string:name>') #created one url pattern and function that can handle inputting a parameter, name.
def hi_user(name):
    print(name)
    return "hi " + name

@app.route('/hello_int/<int:num>/<string:name>') #created one url pattern and function that prints hello x number of times.
def hello_int(num, name):
    print(num)
    return name * num

if __name__=="__main__":
    app.run(debug=True)
