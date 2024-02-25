# Face Verification and Recognition System

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Descriptions](#file-descriptions)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
This project is a Face Verification and Recognition System implemented using Python and TensorFlow. It allows users to add persons to the system, verify their identity, and recognize faces.

## Installation
1. Clone the repository: `git clone https://github.com/your_username/face-recognition-system.git`

## Usage
1. Run the main.py file: `python main.py`
2. Use the GUI to interact with the system:
   - Add Person: Capture an image and save the person's name and facial encoding.
   - Verify: Capture an image and verify the identity of the person.
   - Recognize: Capture an image and recognize the person if they are in the database.

## File Descriptions
- allow_person.py: Contains functions for face verification and identification.
- save.py: Contains functions for saving images and their corresponding facial encodings to a database.
- encoding.py: Contains functions for converting images to facial embeddings using a pre-trained model.
- Database.py: Sets up the SQLite database for storing person information.
- main.py: The main file to run the Face Verification and Recognition System.
- model/: Directory containing the pre-trained model for face embedding.

## Contributing
Contributions to this project are welcome.
## License
This project is licensed under the [MIT License](LICENSE).
