from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student data from JSON file
with open('q-vercel-python.json', 'r') as f:
    student_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get multiple 'name' parameters
    marks = []

    for name in names:
        found = False
        for student in student_data:
            if student['name'] == name:
                marks.append(student['marks'])
                found = True
                break
        if not found:
            marks.append(None) # Or handle the case where the name isn't found differently (e.g., return an error)

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production