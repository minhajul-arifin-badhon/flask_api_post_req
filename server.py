from flask import Flask, request, json, jsonify #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/create_event', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.json

    event_name = req_data['event_name']
    event_desc = req_data['event_desc']
    event_note = req_data['event_note']

    return jsonify(
        {
          "event_name": event_name,
          "event_desc": event_desc,
          "event_note": event_note,
        }
    )

app.run(debug=True, port=5000) #run app in debug mode on port 5000
