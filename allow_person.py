import numpy as np
import tensorflow as tf
from encoding import img_to_embedding
import sqlite3
import os
import json

current_directory = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(current_directory, "Institution.db")

def verify(image_path, identity):
    
    encoding = img_to_embedding(image_path)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT encoding FROM Person WHERE name = ?",(identity,))
    result = cursor.fetchall()[0][0]
    encoding_2 = np.array(json.loads(result))

    dist = np.linalg.norm(tf.subtract(encoding_2, encoding))
    if dist < 0.7:
        message = "It's " + str(identity) + ", welcome in!"
        allowed = True
    else:
        message = "It's not " + str(identity) + ", please go away"
        allowed = False
    print(dist, allowed)
    return message


def who_is_it(image_path):
    
    encoding =  img_to_embedding(image_path)

    min_dist = 100

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT encoding FROM Person")
    result = cursor.fetchall()
    

    min_dist = 100
    cn = 0
    for element in result:
        encoding_2 = np.array(json.loads(element[0]))
    
        dist = np.linalg.norm(tf.subtract(encoding_2, encoding))

        if dist < min_dist:
            cn += 1
            min_dist = dist
            cursor.execute("SELECT name FROM Person WHERE id = ?",(cn,))
            result_2 = cursor.fetchall()
            identity = result_2[0][0]

    if min_dist > 0.7:
        message = "Not in the database."
    else:
        message = "it's " + str(identity) + ", the distance is " + str(min_dist)

    print(min_dist, identity)

    return message