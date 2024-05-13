#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:value>")
def print_string(value):
    print(value)
    return value


@app.route("/count/<int:number>")
def count(number):
    numbers_list = "\n".join(str(num) for num in range(number))
    return f"{numbers_list}\n"


@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Invalid input"

    result = None
    if operation == "+":
        result = num1 + num2
        # Check if the result is a whole number
        if result.is_integer():
            result = int(result)  # Convert to integer if it's a whole number
    elif operation == "-":
        result = num1 - num2
        if result.is_integer():
            result = int(result)
    elif operation == "*":
        result = num1 * num2
        if result.is_integer():
            result = int(result)
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: division by zero"
    elif operation == "%":
        result = num1 % num2
        if result.is_integer():
            result = int(result)
    else:
        return "Error: Invalid operation"

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
