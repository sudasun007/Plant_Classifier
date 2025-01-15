
# Plant Classifier App

The **Plant Classifier App** is an AI-powered web application that allows users to upload images of plants and receive predictions about their species using a pre-trained deep learning model. The app utilizes **TensorFlow** for image classification and **Flask** for the backend API.

## Features

- **Image Upload**: Upload an image of a plant to get a prediction of its species.
- **AI Classification**: Uses a TensorFlow model trained on various plant species to predict the class.
- **Confidence Score**: Displays the confidence level of the prediction.
- **Batch Prediction**: Supports batch prediction for a folder of images, processing each image one by one.

## Technologies Used

- **Frontend**: 
  - HTML, CSS, and JavaScript for a responsive and user-friendly interface.
  - Modern UI design with hover effects and progress indicators.
  
- **Backend**:
  - **Flask** for creating the API that handles image uploads and interactions with the AI model.
  - **TensorFlow** for the pre-trained deep learning model to classify plant species from images.
  
- **Deployment**:
  - The app can be deployed using platforms such as **Heroku** or any other cloud service provider.
  
## Setup & Installation

### Prerequisites

To run this project locally, you need to have the following installed:

- **Python 3.x**
- **TensorFlow**
- **Flask**
- **NumPy**
- **Pillow** (for image processing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sudasun007/Plant_Classifier.git
   cd Plant_Classifier
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app locally:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to access the app.

## Uploading Images

- **Single Image Upload**: Use the file upload form to select a single image of a plant. The app will return the predicted plant species and confidence score.
  
- **Batch Image Upload**: Upload a folder containing multiple images. The backend processes each image one by one, making predictions for all images in the folder.

## Folder Structure

Here's a brief overview of the folder structure of this project:

```
PlantClassifierProject/
│
├── app.py                   # Main Python file to run the Flask server
├── model/                   # Folder containing the trained model file (e.g., 'plant_ClassifierRse_02.keras')
├── templates/               # Folder for HTML templates
│   └── index.html           # The homepage HTML
├── static/                  # Folder for static files (e.g., CSS, JS, images)
│   └── style.css            # The CSS stylesheet
├── multimedia/              # Folder for demo videos
│   └── PlantClassifierDemo.mp4
├── requirements.txt         # List of dependencies for the project
└── README.md                # This file
```

## Frontend Overview

The frontend is built using HTML, CSS, and JavaScript. It consists of the following components:

- **Homepage (index.html)**:
  - A form for users to upload an image for classification.
  - Displays prediction results and confidence score.
  - A loader is shown during the image upload process.

### Styles

The application has a clean and minimalistic design with the following key elements:

- A vibrant green gradient background.
- The file upload button is styled with padding, border radius, and hover effects.
- A spinner is displayed during the loading process to indicate the app is processing the image.
- The result is shown in a styled box, displaying the predicted class and confidence score.

## Backend Overview

The backend is built using **Flask**, a lightweight web framework for Python. The backend has the following functionality:

- **Image Upload**: Handles file uploads from the frontend and stores them temporarily for processing.
- **Image Processing**: The uploaded image is resized and preprocessed to match the model's input requirements (224x224 pixels).
- **AI Prediction**: The image is passed to a **TensorFlow** model for prediction, and the result (predicted class and confidence score) is returned to the frontend.

The backend also supports processing multiple images in a folder.

### Routes

- **`/`**: The homepage route that renders the `index.html` file.
- **`/predict`**: The route that handles the image upload and returns the prediction result in JSON format.

## Example

### Upload a single image:

1. Open the app in your browser.
2. Use the form to upload an image of a plant.
3. The app will predict the plant species and display the result with confidence.

### Upload a folder of images:

1. Modify the backend to accept a folder of images.
2. Upload the folder to the backend.
3. The app will process each image in the folder and return the predictions one by one.

## Contributing

Feel free to fork this repository and make contributions. Here are some ways you can help improve this project:

- Report bugs or issues.
- Suggest new features.
- Submit a pull request with bug fixes or improvements.

