from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

CORS(app) # Enable CORS to allow cross-origin requests

# (simulate a contents database)
contents = [
    {
        'id': 1,
        'title': 'Inception',
        'description': 'Description: A mind-bending sci-fi thriller where a skilled thief.... Directed by Christopher Nolan',
        'image_url': 'https://via.placeholder.com/200x300'
    },
    {
        'id': 2,
        'title': 'The Shawshank Redemption',
        'description':'Description: A compelling drama about hope and friendship, .... wrongly imprisoned for murder',
        'image_url': 'https://via.placeholder.com/200x300'
    },
    {
        'id': 3,
        'title': 'The Dark Knight',
        'description': 'Description: In this gripping superhero film, Batman ....  of morality, justice, and sacrifice.',
        'image_url': 'https://via.placeholder.com/200x300'
    }
]

# Endpoint to get all content
@app.route('/content', methods=['GET'])
def get_all_content():
    """
    Get all content available.
    This endpoint returns a list of all contents in the system.
    
    Returns:
        JSON response with all available content information.
    """
    return jsonify(contents)

@app.route('/content', methods=['POST'])
def add_movie():
    """
    Add a new movie to the database.
    Expects a JSON payload with 'title', 'description', and 'image_url'.
    """
    data = request.json

    # Validate required fields
    if not data or 'title' not in data or 'description' not in data or 'image_url' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new movie entry
    new_movie = {
        'id': len(contents) + 1,  # Auto-incremental ID
        'title': data['title'],
        'description': data['description'],
        'image_url': data['image_url']
    }
    contents.append(new_movie)
    
    return jsonify({'message': 'Movie added successfully', 'movie': new_movie}), 201


# Endpoint to get details of a specific content by ID
@app.route('/content/<int:content_id>', methods=['GET'])
def get_content(content_id):
    """
    Get details of a specific content by ID.
    This endpoint returns the details of a particular content item if it exists.
    
    Args:
        content_id (int): ID of the content to retrieve.
        
    Returns:
        JSON response with content details if found, otherwise a 404 error.
    """
    content = next((c for c in contents if c['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)


# Endpoint to stream a specific content by ID
@app.route('/content/<int:content_id>/stream', methods=['GET'])
def stream_content(content_id):
    """
    Stream a specific content by ID.
    This endpoint simulates the streaming of a particular content item if it exists.
    
    Args:
        content_id (int): ID of the content to stream.
        
    Returns:
        JSON response with content details if found, otherwise a 404 error.
    """
    content = next((item for item in contents if item['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)

# Endpoint to download a specific content by ID
@app.route('/content/<int:content_id>/download', methods=['GET'])
def download_content(content_id):
    """
    Download a specific content by ID.
    This endpoint simulates the downloading of a particular content item if it exists.
    
    Args:
        content_id (int): ID of the content to download.
        
    Returns:
        JSON response with content details if found, otherwise a 404 error.
    """
    content = next((item for item in contents if item['id'] == content_id), None)
    if not content:
        abort(404, description="Content not found")
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

