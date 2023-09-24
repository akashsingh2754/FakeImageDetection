import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

# Simulated dataset (replace with real data)
# Assume X_real contains real images, and X_fake contains fake images generated by GANs.
# You should prepare a proper dataset with labeled real and fake images.
X_real = np.random.randn(100, 64, 64, 3)
X_fake = np.random.randn(100, 64, 64, 3)

# Create labels for real and fake images
y_real = np.ones((X_real.shape[0], 1))
y_fake = np.zeros((X_fake.shape[0], 1))

# Combine real and fake data and labels
X = np.vstack((X_real, X_fake))
y = np.vstack((y_real, y_fake))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a simple CNN model for fake image detection
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # Binary classification output
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_accuracy}')

# Make predictions (you can use this for individual image detection)
predictions = model.predict(X_test)

# Example: Classify a single image (replace 'input_image' with your image data)
input_image = np.random.randn(1, 64, 64, 3)
prediction = model.predict(input_image)
if prediction > 0.5:
    print("Real Image")
else:
    print("Fake Image")
