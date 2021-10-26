from flask import Flask, json, jsonify, request, Response
import os
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_world():
     return jsonify(input='Howdy!', output= 'Hello World')

#MD5 Code Start
@app.route("/md5/<string:str>")
def MD5(str):
    encoded_str = str.encode()
    hash_obj = hashlib.md5(encoded_str)
    hexa_value = hash_obj.hexdigest()
    return jsonify(input=str, output=hash_obj.hexdigest())
#MD5 Code End

#Factorial Code Start
@app.route('/factorial/<int:num>')
def Factorial(num):
    num=int(num)
    factorial = 1
    if num < 0:
        return jsonify(input=num, output= "Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        return jsonify(input=num, output= "The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
           factorial = factorial*i
        return jsonify(input=num, output=factorial)
#Factorial Code End

# Fibonacci Code Start
@app.route("/fibonacci/<int:n>")
def calc_fibonacci(n):
    if n < 0:
        return jsonify(input=n, output="Error: Please enter a number greater or equal to 0")
    sequence = [0,1]
    for i in range(2,n+1):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)
    return jsonify(input=n, output=sequence)
# Fibonacci Code End


# Prime Code Start
#print("Enter a number to check if its prime: ")
#n = (int(input()))

#def fibonacci(n):
#    if (n==1):
#        return False
#    elif (n==2):
#        return True;
#    else:
#        for x in range(2,n):
#            if(n % x==0):
#                return False
#        return True             
#print(fibonacci(n))
# Prime Code End

@app.route('/slack-alert/<string:msg>')
def slack(msg):
	try:
		response = client.chat_postMessage(
			channel="C011KJWHA22",
			text=msg
		)
		print("RESPONSE:", response)
		return jsonify(
			input=msg,
			message=msg,
			output= "Message was successfully sent in slack" if response['ok'] else ''
		), 200 if response['ok'] else 400
	except SlackApiError as e:
		assert e.response["error"]
		return jsonify(
			input=msg,
			message=msg,
			output=e.response["error"]
		)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")