from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

CORS(app)

# Mock data for content
contents = [
    {
        'id': 1,
        'title': 'Movie 1',
        'description': 'This is the description for Movie 1',
        'image_url': 'https://via.placeholder.com/200x300'
    },
    {
        'id': 2,
        'title': 'Movie 2',
        'description': 'This is the description for Movie 2',
        'image_url': 'https://via.placeholder.com/200x300'
    },
    {
        'id': 3,
        'title': 'Movie 3',
        'description': 'This is the description for Movie 3',
        'image_url': 'https://via.placeholder.com/200x300'
    }
]

@app.route('/content', methods=['GET'])
def get_all_content():
    return jsonify(contents)

@app.route('/content/<int:content_id>', methods=['GET'])
def get_content(content_id):
    content = next((c for c in contents if c['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)


# Streaming of a specific content (GET /content/{id}/stream)
@app.route('/content/<int:content_id>/stream', methods=['GET'])
def stream_content(content_id):
    content = next((item for item in contents if item['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)

# Content download
@app.route('/content/<int:content_id>/download', methods=['GET'])
def download_content(content_id):
    content = next((item for item in contents if item['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

