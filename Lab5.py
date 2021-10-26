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

@app.route('/result2',methods=['POST', 'GET'])
def result2():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    name=int(name)
    factorial = 1
    if name < 0:
        name=str(name)
        name = "Sorry, factorial does not exist for negative numbers"
    elif name == 0:
        name=str(name)
        name = "1"
    else:
        for i in range(1,name + 1):
            name = factorial*i

    return render_template('index.html', name = name)

@app.route('/result3',methods=['POST', 'GET'])
def result3():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    name=int(name)
    if name < 0:
        print("Incorrect input")
    sequence = [0,1]
    for i in range(2,name+1):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)

    name = sequence

    return render_template('index.html', name = name)

@app.route('/result4',methods=['POST', 'GET'])
def result4():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    name=int(name)

    if name >= 1:
        for i in range(2, name//2):
            if(name % i) == 0:
                name = "False"
                break
        else:
            name ="True"

    elif name < 1:
        name="Error postive integers only"

    return render_template('index.html', name = name)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

@app.route('/result5',methods=['POST', 'GET'])
def result5():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    payload = '{"text":"s%"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
     data=payload)

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

    print(response.text)



    return render_template('index.html', name = name)