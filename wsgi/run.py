from flask import Flask, request, redirect
import twilio.twiml
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def smsResponse():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.sms("Your, text has been received")
    return str(resp)

@app.route("/incoming", methods=['GET', 'POST'])
def receiveResponse():
    body = request.args.get('body')
    if not body:
        print request.args.keys()
    return body

if __name__ == "__main__":
    app.run(debug=True)
