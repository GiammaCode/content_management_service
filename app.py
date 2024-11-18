from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Mock data for content
data_store = [
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

# Homepage showing three movies
@app.route('/')
def home():
    return render_template('home.html', contents=data_store[:3])

# View all content
@app.route('/content', methods=['GET'])
def view_all_content():
    return render_template('all_content.html', contents=data_store)

# View a specific content
@app.route('/content/<int:content_id>', methods=['GET'])
def view_specific_content(content_id):
    content = next((item for item in data_store if item['id'] == content_id), None)
    if not content:
        return jsonify({'error': 'Content not found'}), 404
    return render_template('content_detail.html', content=content)

# Streaming of a specific content
@app.route('/content/<int:content_id>/stream', methods=['GET'])
def stream_content(content_id):
    content = next((item for item in data_store if item['id'] == content_id), None)
    if not content:
        return jsonify({'error': 'Content not found'}), 404
    return render_template('stream.html', content=content)

# Content download
@app.route('/content/<int:content_id>/download', methods=['POST'])
def download_content(content_id):
    content = next((item for item in data_store if item['id'] == content_id), None)
    if not content:
        return jsonify({'error': 'Content not found'}), 404
    return render_template('download.html', content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

