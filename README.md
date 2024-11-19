# Content Management Service

This repository contains a **Content Management Service** implemented using Flask. The service allows users to retrieve, stream, and download different types of content. It uses Flask's RESTful capabilities to expose several endpoints for interacting with the content.

## Overview

- **Programming Language**: Python 3
- **Framework**: Flask
- **Dependencies**: Flask-JWT-Extended, Flask-CORS
- **Port**: Runs on `localhost:5001`

## Features

1. **View All Content**: Retrieve a list of all available content.
2. **View Specific Content**: Retrieve details of a specific content by its ID.
3. **Stream Content**: Endpoint for streaming a particular content by ID.
4. **Download Content**: Endpoint for downloading a particular content by ID.

## Project Structure

```
content_management_service/
|-- app.py                 # Main Flask application
|-- requirements.txt       # Dependencies required to run the application
```

## Endpoints

1. **`GET /content`**: Retrieve all available content.
   - **Description**: Returns a JSON list of all content currently available.
   - **Response**: A list containing all the available content, including metadata like `id`, `title`, `description`, and `image_url`.

2. **`GET /content/<int:content_id>`**: Retrieve specific content by ID.
   - **Description**: Returns detailed information about the content specified by the given `content_id`.
   - **Path Parameters**:
     - `content_id` (int): ID of the content to be retrieved.
   - **Response**: A JSON object containing details of the requested content. Returns a 404 error if the content is not found.

3. **`GET /content/<int:content_id>/stream`**: Stream specific content by ID.
   - **Description**: Simulates streaming of the specified content.
   - **Path Parameters**:
     - `content_id` (int): ID of the content to stream.
   - **Response**: A JSON object containing details of the content to be streamed. Returns a 404 error if the content is not found.

4. **`GET /content/<int:content_id>/download`**: Download specific content by ID.
   - **Description**: Simulates downloading the specified content.
   - **Path Parameters**:
     - `content_id` (int): ID of the content to download.
   - **Response**: A JSON object containing details of the content to be downloaded. Returns a 404 error if the content is not found.

## How to Run the Project

### Prerequisites
- **Python 3.x**
- **Flask** and other required dependencies (see `requirements.txt`)

### Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd content_management_service
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
Run the Flask application using the following command:
```sh
python app.py
```
The service will start on `http://localhost:5001`.

## Dependencies
- **Flask**: Web framework used to build the service.
- **Flask-JWT-Extended**: Used for JWT authentication.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing (CORS) for cross-origin requests.

