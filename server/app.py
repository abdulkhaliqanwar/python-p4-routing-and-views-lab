#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>", 200  

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  
    return text 


@app.route('/count/<int:number>')
def count(number): 
    numbers = "\n".join(str(i) for i in range(number)) + "\n"
    return numbers # Join numbers with <br> for browser display


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return "Error: Division by zero is not allowed.", 400
        result = num1 / num2
    elif operation == "%":
        if num2 == 0:
            return "Error: Modulo by zero is not allowed.", 400
        result = num1 % num2
    else:
        return "Error: Invalid operation. Use +, -, *, div, or %.", 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
