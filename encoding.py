import numpy as np
import tensorflow as tf
import os

current_directory = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(current_directory, "model")
model = tf.keras.models.load_model(model_path)

def img_to_embedding(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0) # add a dimension of 1 as first dimension
    embedding = model.predict_on_batch(x_train)
    return embedding / np.linalg.norm(embedding, ord=2)
