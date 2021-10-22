from flask import Flask, request, render_template
import hashlib
from typing import Sequence

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

#MD5 Code Start
print("Input MD5 string for conversion")
str = input()
encoded_str = str.encode()
hash_obj = hashlib.md5(encoded_str)
hexa_value = hash_obj.hexdigest()
print("\n", hexa_value, "\n")
#MD5 Code End

#Factorial Start
print("Input an integer")
num = int(input())
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
print("")
#Factorial End

# Fibonacci Start
def fibonacci (n):
    if n < 0:
        print("Incorrect input")
    sequence = [0,1]
    for i in range(2,n+1):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)
    return sequence

sequence = fibonacci(10)
print(sequence)
# Fibonacci End