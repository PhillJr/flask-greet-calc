# Put your app in here.
from flask import Flask
from flask import request
from markupsafe import escape
# from .operations import * #both wroks just curious 
from operations import add, sub, mult, div
app =  Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!- I'm changing<p><br><p>Change detected<p>"

#This works, but it doesn't use the query parameters
# @app.route("/add/<int:a>/<int:b>")
# def add(a,b):
#     sum = a + b
#     return f"sum={sum}"


#Works #Using query parameters
# @app.route("/add")
# def add():
#     a = request.args.get('a',type=int)
#     b = request.args.get('b',type=int)
#     return f'result = {a + b}'

@app.route("/add")
def add_():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f'{add(a,b)}'
@app.route("/sub")
def sub_():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f'{sub(a,b)}'
@app.route("/mult")
def mult_():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f'{mult(a,b)}'
@app.route("/div")
def div_():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f'{div(a,b)}'

operations = {
    'add':add,
    'sub':sub,
    'mult':mult,
    'div':div
}


@app.route("/math/<operation>")
def math_op(operation):
    a=request.args.get('a',type=int)
    b=request.args.get('b',type=int)
    
    if a is None or b is None:
        return "Error: Enter a value for both a and b"
    if operation not in operations:
        return "Please enter a valid operation"
    result = operations[operation](a,b)
    return f'{result}'