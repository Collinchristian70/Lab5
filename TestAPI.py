import requests
import sys
import getopt
#send slack message using slack API
def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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', data=payload)
    print(response.text)

def main(argv):

    message = ''

    try: opts, arge = getopt.getopt(argv, "hm:", ["message="])
    except getopt.GetoptError:
        print("slackmessage.py -m <message>")
        sys.exit(2)
    if len(opts) == 0: 
        message = "HELLO, World!"
    for opt, arg in opts:
        if opt == '-h':
            print("slackmessage.py -m <message>")
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])
