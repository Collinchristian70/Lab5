from flask import Flask, json, jsonify, request, Response
import os
import hashlib
import requests
import sys
import getopt
import redis

REDIS = redis.Redis(host='redis-server')
status_code = " "
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
@app.route("/fibonacci/<int:number>")
def calc_fibonacci(number):
    fibonacci = [0]
    c1 = 0
    c2 = 1
    fib = 0
    check = 0

    if number < 0:
        return jsonify(input=number, output="Error: Please enter a number greater or equal to 0")
    elif number == 0:
        fibonacci = [0]
    else:
        while check == 0:
            fib = c1 + c2
            c2 = c1
            c1 = fib
            if fib <= number:
                fibonacci.append(fib)
            else:
                check = 1
    return jsonify(input=number, output=fibonacci)
# Fibonacci Code End


# Prime Code Start
@app.route('/is-prime/<int:number>')
def is_prime(number):
    isPrime = False
    if number == 2:
        isPrime = True
    if number > 2:
        isPrime = True
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

    if isPrime:
       return jsonify(input=number, output=True)
    else:
       return jsonify(input=number, output=False)
# Prime Code End

#send slack message using slack API
@app.route('/slack-alert/<string:message>')
def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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', data=payload)
    print(response.text)

    try: opts, arge = getopt.getopt(message, "hm:", ["message="])
    except getopt.GetoptError:
        return jsonify(input=message, output="0")
        sys.exit(2)
    if len(opts) == 0: 
        return jsonify(input=message, output='1')
        sys.exit(0)
    for opt, arg in opts:
        if opt == '-h':
            return jsonify(input=message, output=message)
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
    send_slack_message(message)
    return jsonify(input=message, output=message)
    sys.exit(1)
#end of slack message using slack API

#redis

@app.route('/keyval', methods = ['POST'])
def post():
    
	payload = request.get_json()
	
	
	if REDIS.exists(payload['key']):
		
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"CREATE {payload['key']}/{payload['value']}",
			result=False, 
			error="Key already exists"
		), 409
	else:	
		REDIS.set(payload['key'], payload['value'])
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"CREATE {payload['key']}/{payload['value']}",
			result=True, 
			error=""
		), 200

@app.route('/keyval/<string:user_key>', methods = ['GET'])
def get(user_key):
	
	if REDIS.exists(user_key):
		redis_val = REDIS.get(user_key)
		return jsonify(
			key=user_key,
			value=redis_val.decode('unicode-escape'), #decodes the byte string to python string
			command=f"GET {user_key}",
			result=True,
			error= ""
		), 200
	else:
		return jsonify(
			key=user_key, 
			value=None, 
			command=f"GET {user_key}",
			result=False, 
			error="Key does not exist"
		), 404

@app.route('/keyval', methods = ['PUT'])
def put():
	
	payload = request.get_json()
	
	if REDIS.exists(payload['key']):
		REDIS.set(payload['key'], payload['value'])
		return jsonify(
			key= payload['key'], 
			value=payload['value'], 
			command=f"UPDATE {payload['key']}/{payload['value']}",
			result=True, 
			error=""
		), 200
	else:
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"UPDATE {payload['key']}/{payload['value']}",
			result=False, 
			error="Key does not exist, use POST to create key value pair."
		), 404

@app.route('/keyval/<string:user_key>',methods = ['DELETE'])
def delete(user_key):
	
	if REDIS.exists(user_key):	
		redis_val = REDIS.get(user_key)
		REDIS.delete(user_key)
		return jsonify(
			key=user_key,
			value=redis_val.decode('unicode-escape'), #decodes the byte string to python string
			command=f"DELETE {user_key}",
			result=True,
			error= ""
		), 200
	else:
		return jsonify(
			key=user_key, 
			value=None, 
			command=f"DELETE {user_key}",
			result=False, 
			error="Key does not exist, use POST to create key value pair."
		), 404

if __name__ == "__main__":
	app.debug = False
	app.run(host='0.0.0.0', port=80)
#end redis