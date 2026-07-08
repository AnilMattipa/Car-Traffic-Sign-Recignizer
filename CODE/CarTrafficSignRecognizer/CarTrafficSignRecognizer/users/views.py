from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel


def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def UserTraining(request):
    import numpy as np
    import os
    from sklearn.model_selection import train_test_split
    from keras.utils import to_categorical
    from keras.models import Sequential
    from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
    from django.conf import settings
    from PIL import Image
    import matplotlib.pyplot as plt

    data = []
    labels = []
    classes = 43

    # Load dataset
    for i in range(classes):
        path = os.path.join(settings.MEDIA_ROOT, 'DataSet/Train', str(i))
        images = os.listdir(path)
        for a in images:
            try:
                image = Image.open(os.path.join(path, a))
                image = image.resize((30, 30))
                image = np.array(image)
                data.append(image)
                labels.append(i)
            except:
                print("Error loading image")

    # Convert to NumPy + normalize
    data = np.array(data) / 255.0
    labels = np.array(labels)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.2, random_state=42
    )

    # One-hot encode labels
    y_train = to_categorical(y_train, classes)
    y_test = to_categorical(y_test, classes)

    # Build CNN model with fixed input shape
    model = Sequential()
    model.add(Conv2D(32, (5, 5), activation='relu', input_shape=(30, 30, 3)))
    model.add(Conv2D(32, (5, 5), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train
    epochs = 15
    history = model.fit(X_train, y_train, batch_size=32, epochs=epochs, validation_data=(X_test, y_test))

    acc = history.history['accuracy'][-1]
    loss = history.history['loss'][-1]

    # ✅ Always overwrite same model file
    model_path = os.path.join(settings.MEDIA_ROOT, "traffic_classifier.h5")
    model.save(model_path)
    print(f"✅ Model saved at: {model_path}")

    # Save training plots as images
    plt.figure(0)
    plt.plot(history.history['accuracy'], label='training accuracy')
    plt.plot(history.history['val_accuracy'], label='val accuracy')
    plt.title('Accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()
    plt.savefig(os.path.join(settings.MEDIA_ROOT, "training_accuracy.png"))
    plt.close()

    plt.figure(1)
    plt.plot(history.history['loss'], label='training loss')
    plt.plot(history.history['val_loss'], label='val loss')
    plt.title('Loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.savefig(os.path.join(settings.MEDIA_ROOT, "training_loss.png"))
    plt.close()

    return render(request, 'users/UserTraining.html', {'acc': acc, 'loss': loss})


def UserPredict(request):
    from keras.models import load_model
    from PIL import Image
    import numpy as np
    import os
    from django.conf import settings

    classes = {
        1: 'Speed limit (20km/h)',
        2: 'Speed limit (30km/h)',
        3: 'Speed limit (50km/h)',
        4: 'Speed limit (60km/h)',
        5: 'Speed limit (70km/h)',
        6: 'Speed limit (80km/h)',
        7: 'End of speed limit (80km/h)',
        8: 'Speed limit (100km/h)',
        9: 'Speed limit (120km/h)',
        10: 'No passing',
        11: 'No passing veh over 3.5 tons',
        12: 'Right-of-way at intersection',
        13: 'Priority road',
        14: 'Yield',
        15: 'Stop',
        16: 'No vehicles',
        17: 'Veh > 3.5 tons prohibited',
        18: 'No entry',
        19: 'General caution',
        20: 'Dangerous curve left',
        21: 'Dangerous curve right',
        22: 'Double curve',
        23: 'Bumpy road',
        24: 'Slippery road',
        25: 'Road narrows on the right',
        26: 'Road work',
        27: 'Traffic signals',
        28: 'Pedestrians',
        29: 'Children crossing',
        30: 'Bicycles crossing',
        31: 'Beware of ice/snow',
        32: 'Wild animals crossing',
        33: 'End speed + passing limits',
        34: 'Turn right ahead',
        35: 'Turn left ahead',
        36: 'Ahead only',
        37: 'Go straight or right',
        38: 'Go straight or left',
        39: 'Keep right',
        40: 'Keep left',
        41: 'Roundabout mandatory',
        42: 'End of no passing',
        43: 'End no passing veh > 3.5 tons'
    }

    sign = None

    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, "wb+") as dest:
            for chunk in uploaded_file.chunks():
                dest.write(chunk)

        # preprocess image
        image = Image.open(file_path)
        image = image.resize((30, 30))
        image = np.array(image) / 255.0
        image = image.reshape(1, 30, 30, 3)   # ensure correct shape

        # load the latest model
        model_path = os.path.join(settings.MEDIA_ROOT, "traffic_classifier.h5")
        model = load_model(model_path)

        pred = model.predict(image)[0]
        sign = classes[np.argmax(pred) + 1]

    return render(request, "users/UserPredict.html", {"sign": sign})
