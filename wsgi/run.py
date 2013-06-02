from flask import Flask, request, redirect
import os
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def smsResponse():
    """Respond to incoming calls with a simple text message."""
    resp = "Your, text has been received"
    return resp

@app.route("/incoming", methods=['GET', 'POST'])
def receiveResponse():
    data_dir = os.environ.get("OPENSHIFT_DATA_DIR")
    with open(os.path.join(data_dir, 'tempfile'), 'a') as log:

        body = request.args.get('body')
        if not body:
            body = request.args.keys()
        log.write(body)

if __name__ == "__main__":
    app.run(debug=True)
