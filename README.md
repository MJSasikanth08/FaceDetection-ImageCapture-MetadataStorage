
# Face Detection and Metadata Storage

## Overview

This project focuses on detecting faces from a live video stream, saving the identified face images, and storing associated metadata in a MySQL database. The application leverages OpenCV for face detection, Pillow for metadata extraction, and MySQL for database operations.

## Components

1. **Face Detection**:
   - **OpenCV**: Utilized for detecting faces in real-time video streams captured from a webcam.

2. **Metadata Extraction**:
   - **Pillow**: Used to extract metadata from the saved images, including format, mode, size, and EXIF data.

3. **Database Storage**:
   - **MySQL**: Stores metadata about each detected face image, including the filename and extracted metadata.

## Installation

To set up the environment for this project, you need to install the following Python libraries:

```sh
pip install opencv-python mysql-connector-python pillow
```

Ensure you have a MySQL server running and create a database named `metadata` with a table called `captures` having columns for `filename` and `metadata`.

## Steps

1. **Train a Model with a Face**:
   - Although not explicitly covered in the provided code, this step involves training a face recognition model with sample face images. This can be achieved using various machine learning libraries and datasets.

2. **Capture Video Stream**:
   - The code continuously captures frames from a webcam stream using OpenCV.

3. **Face Detection and Metadata Storage**:
   - Each frame is processed to detect faces.
   - Detected faces are saved as images with timestamps.
   - Metadata for each saved image is extracted and stored in a MySQL database along with the image filename.

## Usage

Run the script to start capturing frames from your webcam. Detected faces will be saved as image files, and metadata will be stored in the MySQL database. The video stream will be displayed in a window until the user exits by pressing the 'q' key.

## Conclusion

This project integrates real-time face detection with metadata extraction and storage, demonstrating practical applications of computer vision and database management. It can be extended to include face recognition and more advanced metadata features.

