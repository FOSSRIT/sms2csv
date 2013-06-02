from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def smsResponse():
    """Respond to incoming calls with a simple text message."""
    resp = "Your, text has been received"
    return resp

@app.route("/incoming", methods=['GET', 'POST'])
def receiveResponse():
    data_dir = os.environ.get("OPENSHIFT_DATA_DIR", '.')
    body = request.args.get('Body')
    from_number = request.args.get('From', '1111111')
    if not body or from_number:
        return "Please don't go here manually."
    with open(os.path.join(data_dir, from_number), 'a') as log:
        log.write(str(body) + '\n')
    return str(body)

if __name__ == "__main__":
    app.run(debug=True)
