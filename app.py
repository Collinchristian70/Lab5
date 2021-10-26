from flask import Flask, request, render_template
import hashlib
from typing import Sequence

from flask.templating import _render

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    encoded_str = name.encode()
    hash_obj = hashlib.md5(encoded_str)
    name = hash_obj.hexdigest()

    return render_template('index.html', name = name)
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

#MD5 Code Start
#def MD5():
    #print("Input MD5 string for conversion")
    #str = input()
    #encoded_str = str.encode()
    #hash_obj = hashlib.md5(encoded_str)
    #hexa_value = hash_obj.hexdigest()
    #print("\n", hexa_value, "\n")
    #return hexa_value
#MD5 Code End
#MD5()

#Factorial Code Start
def Factorial(): 
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
#Factorial Code End
#Factorial()

# Fibonacci Code Start
def fibonacci ():

    print("Input interger")
    n = int(input())

    if n < 0:
        print("Incorrect input")
    sequence = [0,1]
    for i in range(2,n+1):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)
    return sequence

    sequence = fibonacci(10)
    print(sequence)
# Fibonacci Code End
#fibonacci()

# Prime Code Start
def Prime():
    n = int(input("Enter a number: "))

    if n > 1:
        for i in range(2, n//2):
            if(n % i) == 0:
                print(n,": False")
                break
        else:
            print(n,": True")

    elif type(n) != int:
        print("Invalid")
# Prime Code End
#Prime()

# Slack Message Start
import sys
import getopt 

def send_slack_message(message):
    payload = '{"text":"s%"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
     data=payload)

    print(response.text)

def main(argv):

    message = ' '

    try: opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('Slackmessage.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        messege = "No, input detected" 
    for opt, arg in opts:
        if opt == '-h':
            print('Slackmessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg 


    send_slack_message(message)

    if __name__ == "__main__":
        main(sys.argv[1:])
    
# Slack Message End