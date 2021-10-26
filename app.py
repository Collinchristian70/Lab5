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

#Factorial Code Start
print("Input an integer for a factorial conversion")
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

# Fibonacci Code Start
print("Input an integer for the Fibonacci sequence")
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
# Fibonacci Code End
print("")
# Prime Code Start
print("Enter a number to check if its prime: ")
n = (int(input()))

def fibonacci(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(fibonacci(n))
# Prime Code End


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