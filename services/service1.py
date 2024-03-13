from flask import Flask, send_file

from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# will accept image id as a ulr parameter

@app.route('/image/<image_id>', methods=['GET'])
def get_picture(image_id):
    # Use the image_id parameter to retrieve the picture path dynamically
    # set the path 
    picture_path = f'aws-training/s3/{image_id}.jpeg'
    # generate random image and return it use numpy
    return send_file(picture_path, mimetype='image/jpeg')


@app.route('/image', methods=['GET'])
def info_about_images():
    # return informative text html about ids
    # generate html with all the image ids


    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image ID Request</title>
    </head>
    <body>
        <h1>Please provide an image id</h1>
    </body>
    """


@app.route('/image/random', methods=['GET'])
def get_random_picture():
    # Generate a random image
    width, height = 640, 480  # You can change these values as needed
    random_image_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    random_image = Image.fromarray(random_image_array)

    # Save the image to a BytesIO object
    byte_io = io.BytesIO()
    random_image.save(byte_io, 'JPEG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()