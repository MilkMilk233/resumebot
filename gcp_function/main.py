import requests
from flask import jsonify, make_response
import uuid

def langflow_proxy(request):
    print(f"Received request method: {request.method}")
    # ✅ Explicitly handle preflight request
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.set('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.set('Access-Control-Max-Age', '3600')
        return response, 204

    # ✅ Actual POST handler
    request_json = request.get_json()
    input_value = request_json.get("input", "")
    session_id = str(uuid.uuid4())

    payload = {
        "input_value": input_value,
        "output_type": "chat",
        "input_type": "chat",
        "session_id": session_id
    }

    headers = {
        "Authorization": "Bearer AstraCS:qHIXPAXHlnHEpZMjEKWBlrMX:955b4abef70f4f471fad42de4062df2b6db51ae76ce3a9efc24c52e09b163d29",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(
            "https://api.langflow.astra.datastax.com/lf/963d37c2-24b5-48ce-b135-b85b304510bc/api/v1/run/01c34a98-2ac9-492e-b872-233b00fc3315",
            json=payload,
            headers=headers
        )
        response = make_response(jsonify(res.json()))
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        response.headers.set('Access-Control-Allow-Origin', '*')
        return response
