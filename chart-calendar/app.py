# from flask import Flask, render_template, request, redirect
# import firebase_admin
# from firebase_admin import credentials, storage

# # Initialize Flask app
# app = Flask(__name__)

# # Initialize Firebase
# cred = credentials.Certificate('C:/Users/ashly/Documents/Programming/Firebase/Python/credentials/key.json')

# firebase_admin.initialize_app(cred, {'storageBucket': 'test-fd199.appspot.com'})  # Replace with your bucket name

# # Route to upload an image
# @app.route('/', methods=['GET', 'POST'])
# def upload_image():
#     if request.method == 'POST':
#         # Check if an image file was uploaded
#         if 'image' in request.files:
#             image = request.files['image']

#             # Upload the image file to Firebase Storage
#             bucket = storage.bucket()
#             blob = bucket.blob(image.filename)
#             blob.upload_from_file(image)

#     return render_template('upload.html')
# # Route to display images
# @app.route('/images')
# def display_images():
#     bucket = storage.bucket()
#     blobs = bucket.list_blobs()

#     image_urls = [blob.public_url for blob in blobs]

#     return render_template('images.html', image_urls=image_urls)

# if __name__ == '__main__':
#     app.run()

#------------------------------------------------------------
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate('C:/Users/ashly/Documents/Programming/Firebase/Python/credentials/firebase_credentials.json')  # Replace with your credentials file path
firebase_admin.initialize_app(cred, {'storageBucket': 'test-fd199.appspot.com'})  # Replace with your bucket name

# Route to upload an image
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if an image file was uploaded
        if 'image' in request.files:
            try:
                image = request.files['image']

                # Upload the image file to Firebase Storage
                bucket = storage.bucket()
                blob = bucket.blob(image.filename)
                blob.upload_from_file(image)

                return redirect('/images')

            except Exception as e:
                return f"An error occurred: {str(e)}"

    return render_template('upload.html')

# Route to display images
@app.route('/images')
def display_images():
    try:
        bucket = storage.bucket()
        blobs = bucket.list_blobs()

        image_urls = [blob.public_url for blob in blobs]

        return render_template('images.html', image_urls=image_urls)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()
