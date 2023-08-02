import cv2
import os
import sqlite3
from encoding import img_to_embedding
import json

def save_image(images_path, image, name):

    cv2.imwrite(os.path.join(images_path, name+'.png'), image)


def save_name_embedding(images_path, name):

    encoding = img_to_embedding(images_path+'/'+name+'.png')
    # Convert the list to a JSON string
    json_encoding = json.dumps(encoding.tolist())

    current_directory = os.path.abspath(os.path.dirname(__file__))
    database_path = os.path.join(current_directory, "Institution.db")

    # Connect to the SQLite database again
    conn = sqlite3.connect(database_path)

    # Create a cursor object
    c = conn.cursor()

    # Define the SQL query to insert the image path into the table
    query = 'INSERT INTO Person (name, encoding) VALUES (?, ?)'

    # Execute the query with the image path as a parameter
    c.execute(query, (name, json_encoding))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    c.close()
    conn.close()