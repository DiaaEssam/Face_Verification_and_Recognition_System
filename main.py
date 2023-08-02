import tkinter as tk
from tkinter import *
import cv2
import functools
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import Image, ImageTk
from save import save_image, save_name_embedding
import os
from tkinter import messagebox
import Database
import allow_person
import numpy as np

current_directory = os.path.abspath(os.path.dirname(__file__))
images_path = os.path.join(current_directory, "Images")

def create_subroot(add=False,ver=False):

    def submit():
        global name
        name = name_entry.get()
                    
        subroot.quit()
        subroot.destroy()

    subroot = tk.Tk()
    subroot.title("Name")
    if add:
        Label(subroot, text='Enter his/her name').grid(row=0)
    if ver:
        Label(subroot, text='Enter your name').grid(row=0)
    name_entry = Entry(subroot)
    name_entry.grid(row=0, column=1)
                
    tk.Button(subroot,
            text="Submit", command=submit).grid(row=2,
                                column=1,
                                sticky=tk.W,
                                pady=4)
                
    subroot.mainloop()


class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Verification and Recognition System")
        window_width = 800
        window_height = 800
        self.root.geometry(f"{window_width}x{window_height}")

        # Create a button to capture image
        add_person = functools.partial(self.capture_image, add=True)
        self.add_person_button = tk.Button(self.root,width=20, height=2, text="Add Person", bg='green', command=add_person)
        self.add_person_button.pack()
        self.add_person_button.place(x=window_width-470, y=window_height-770)

        verify = functools.partial(self.capture_image, ver=True)
        self.verify_button = tk.Button(self.root, width=15, height=2, text="Verify", bg='green', command=verify)
        self.verify_button.pack()
        self.verify_button.place(x=window_width-700, y=window_height-700)

        recognize = functools.partial(self.capture_image, recognize=True)
        self.recognize_button = tk.Button(self.root, width=15, height=2, text="Recognize", bg='green',  command=recognize)
        self.recognize_button.pack()
        self.recognize_button.place(x=window_width-200, y=window_height-700)
        

        # Create a label to display the captured image
        self.image_label = tk.Label(self.root, width=500, height=500)
        self.image_label.pack()
        self.image_label.place(x=window_width-650,y=window_height-500)


        # Open the camera
        self.cap = cv2.VideoCapture(0)

    def capture_image(self, add=False, ver=False, recognize=False):
        
        
        global subroot, name_entry
        if add:
            create_subroot(add=add)
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
            frame_rgb = Image.open(file_path)

            frame_rgb = np.array(frame_rgb)

            bgr_image = cv2.cvtColor(np.array(frame_rgb), cv2.COLOR_RGB2BGR)

            save_image(images_path,bgr_image, name)
            save_name_embedding(images_path, name)
        # Capture frame from the camera
        if ver or recognize:
            ret, frame = self.cap.read()
        
            if ret:
            
                # Convert the frame to RGB format
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                if ver:
                    create_subroot(ver=ver)
                    save_image(images_path,frame, 'Camera0')
                    allow_person.verify(images_path+'/Camera0.png',name)
                    messagebox.showinfo("Result",allow_person.verify(images_path+'/Camera0.png',name))
            
                if recognize:
                    save_image(images_path,frame, 'Camera0')
                    messagebox.showinfo("Result",allow_person.who_is_it(images_path+'/Camera0.png'))

            # Create an ImageTk object from the captured frame
        image = Image.fromarray(frame_rgb)
        image_tk = ImageTk.PhotoImage(image)
            
        # Update the image label with the captured image
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

    def run(self):
        self.root.mainloop()

# Create the root window
root = tk.Tk()

# Create the camera app
app = CameraApp(root)

# Run the app
app.run()