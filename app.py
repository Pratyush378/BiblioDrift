# Placeholder for Flask backend application structure.
# Initialize Flask app, configure CORS, and setup database connection here.

from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_service import generate_book_note

app = Flask(__name__)
CORS(app) # Allows app.js to talk to this server

@app.route('/api/v1/generate-note', methods=['POST'])
def handle_generate_note():
    data = request.json
    description = data.get('description', '')
    
    # Call the service logic
    vibe = generate_book_note(description)
    
    return jsonify({"vibe": vibe})

if __name__ == '__main__':
    app.run(debug=True, port=5000)