# 🚦 Car Traffic Sign Recognizer

A deep learning-based web application that recognizes and classifies traffic signs from uploaded images. The application uses a Convolutional Neural Network (CNN) model trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset and is built using Django for the web interface.

## 📌 Project Overview

The Car Traffic Sign Recognizer is designed to automatically identify traffic signs from images and predict their corresponding classes. This project demonstrates the use of Computer Vision and Deep Learning to improve road safety by assisting drivers and autonomous vehicles in recognizing road signs accurately.

---

## ✨ Features

- Upload traffic sign images through a web interface
- Automatic image preprocessing
- CNN-based traffic sign classification
- Displays predicted traffic sign name
- User-friendly Django web application
- Fast and accurate prediction

---

## 🛠️ Technologies Used

- Python 3.x
- Django
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- HTML5
- CSS3
- Bootstrap
- JavaScript

---

## 📂 Project Structure

```
CarTrafficSignRecognizer/
│
├── CODE/
│   ├── CarTrafficSignRecognizer/
│   ├── assets/
│   ├── media/
│   ├── templates/
│   └── manage.py
│
├── DATABASE/
│
├── DOCUMENTS/
│
└── README.md
```

---

## 🧠 Dataset

This project uses the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset.

- 43 Traffic Sign Classes
- Thousands of labeled training images
- Real-world traffic sign images

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YourUsername/Car-Traffic-Sign-Recognizer.git
```

### Navigate to the project folder

```bash
cd Car-Traffic-Sign-Recognizer
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🚀 How to Use

1. Open the application.
2. Upload a traffic sign image.
3. Click **Predict**.
4. The model processes the image.
5. The predicted traffic sign is displayed.

---

## 🧠 Model Information

- Model Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow/Keras
- Input Size: 30 × 30 pixels
- Output Classes: 43
- Optimizer: Adam
- Loss Function: Categorical Crossentropy

---

## 📊 Results

- High classification accuracy on the GTSRB dataset
- Fast prediction time
- Responsive web interface
- Suitable for educational and research purposes

---

## 🔮 Future Enhancements

- Real-time traffic sign detection using a webcam
- Mobile application integration
- Video-based traffic sign recognition
- Object detection using YOLO
- Improved model accuracy with transfer learning

---

## 📷 Screenshots

Add screenshots of:

- Home Page
- Upload Page
- Prediction Result
- Traffic Sign Classification

---

## 👨‍💻 Author

**Anil Mattipa**

- MCA Graduate (2025)
- Python Developer
- Data Analyst Enthusiast
- Full Stack Developer

GitHub:
https://github.com/AniMattipa

LinkedIn:
(Add your LinkedIn profile here)

---

## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
