from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def Hello_sanskar():
    return "<h1>Hello, Sanskar!</h1>"
    
@app.route("/Sanskar_varshney2")
def Sanskar_varshney2():
    return "<h1>Hello, sanskar!1</h1>"
    
@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    a = 5+6
    return"this is my function to run app {}".format(a) 
    
@app.route("/test2/test2") # for input
def test2():
    data = request.args.get('x')
    return "this is a data input from  my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")


