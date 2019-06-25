from django.shortcuts import render
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from keras.models import load_model
import pickle
import csv

global graph,model


#initializing the graph
graph = tf.get_default_graph()

#loading our trained model
print("Keras model loading.......")
model = load_model('food_ai/data/food_ai_model.hdf5')
encoder = pickle.load(open('food_ai/data/cls_name','rb'))

print("Model loaded!!")

def get_nutrisi(class_name):
    filedata = 'food_ai/data/nilainutrisi.csv'
    nilai_nutrisi = csv.DictReader(open(filedata))
    for row in nilai_nutrisi:
        data = dict(row)
        if data['product_name'] == class_name:
            return data
    
    return False

def recognize(img_data):
    img = image.load_img(img_data, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    # img = img/255
    with graph.as_default():
        preds = model.predict(img)[0]
    
    cls_idx = np.argmax(preds)
    cls_name = encoder[cls_idx]
    acc = "%.2f" % (preds[cls_idx] * 100)

    return cls_name, acc

