from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import io

app = Flask(__name__)

# Load your trained model
model = load_model('plant_ClassifierRse_02.keras')

# Class names
classes = [
    "aloevera", "banana", "bilimbi", "cantaloupe", "cassava", "coconut",
    "corn", "cucumber", "curcuma", "eggplant", "galangal", "ginger",
    "guava", "kale", "longbeans", "mango", "melon", "orange", "paddy",
    "papaya", "peper chili", "pineapple", "pomelo", "shallot", "soybeans",
    "spinach", "sweet potatoes", "tobacco", "waterapple", "watermelon"
]

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling image upload and prediction for multiple images
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    files = request.files.getlist('file')
    if not files:
        return jsonify({'error': 'No files selected'}), 400

    predictions_result = []

    for file in files:
        try:
            # Convert the uploaded file to a file-like object in memory
            image_bytes = io.BytesIO(file.read())
            
            # Load the image with the in-memory file-like object
            image = load_img(image_bytes, target_size=(224, 224))  # Resize to model's input size
            image = img_to_array(image) / 255.0            # Normalize to [0, 1]
            image = np.expand_dims(image, axis=0)          # Add batch dimension

            # Make a prediction
            predictions = model.predict(image)
            predicted_class = classes[np.argmax(predictions)]
            confidence = np.max(predictions) * 100

            predictions_result.append({
                'class': predicted_class,
                'confidence': f"{confidence:.2f}%"
            })

        except Exception as e:
            predictions_result.append({'error': str(e)})

    return jsonify({
        'predictions': predictions_result
    })

if __name__ == '__main__':
    app.run(debug=True)
