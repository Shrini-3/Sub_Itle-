import os
from flask import Flask, render_template, request, redirect, url_for, flash, Response
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['subtitle']
subtitles_collection = db['subtitles']

# For testing purposes, a dummy user dictionary
users = {
    'user@example.com': 'password123',
    # Add more users as needed
}

def generate_subtitles(video_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    
    # Get the duration of the video in seconds
    duration = video_clip.duration
    
    # Generate subtitles as a string
    subtitles = ""
    for i, frame in enumerate(video_clip.iter_frames()):
        # For demonstration purposes, let's assume subtitles are generated based on frame number
        # Replace this logic with your actual subtitle generation algorithm
        subtitle_text = f"Subtitle {i+1} - Frame {i+1}"
        subtitles += f"{subtitle_text}\n"
    
    # Close the video clip
    video_clip.close()
    
    return subtitles

# Function to extract text from video
def extract_text_from_video(video_file):
    # Load the video clip
    video_clip = VideoFileClip(video_file)
    
    # Initialize speech recognizer
    recognizer = sr.Recognizer()
    
    # Extract audio from video
    audio = video_clip.audio.to_soundarray()
    
    # Convert audio to text
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the provided credentials are valid
    if email in users and users[email] == password:
        # Redirect to the dashboard on successful login
        return redirect(url_for('dashboard'))
    else:
        # Handle invalid credentials (you may want to show an error message)
        return render_template('login.html', error='Invalid credentials. Please try again.')

@app.route('/dashboard')
def dashboard():
    # Add logic for the dashboard here
    subtitles = subtitles_collection.find()
    return render_template('dashboard.html', subtitles=subtitles)

@app.route('/process_subtitle', methods=['POST'])
def process_subtitle():
    if 'video' not in request.files:
        return 'No file part'
    video_file = request.files['video']
    if video_file.filename == '':
        return 'No selected file'
    
    # Save the video file
    video_path = os.path.join('uploads', video_file.filename)
    video_file.save(video_path)
    
    # Generate subtitles
    generated_subtitles = generate_subtitles(video_path)
    
    # Save the subtitles to MongoDB
    subtitles_id = subtitles_collection.insert_one({'filename': video_file.filename, 'subtitles': generated_subtitles}).inserted_id
    
    return 'Subtitles generated and saved successfully'

# Route to handle video upload and display subtitles
@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            # Save the video file
            video_path = 'uploads/' + file.filename
            file.save(video_path)
            
            # Extract text from the video
            subtitles = extract_text_from_video(video_path)
            
            # Pass the subtitles to the template for display
            return render_template('video.html', video_path=video_path, subtitles=subtitles)
    
    return render_template('upload.html')

@app.route('/download_subtitle/<subtitle_id>')
def download_subtitle(subtitle_id):
    # Retrieve subtitles from MongoDB
    subtitle = subtitles_collection.find_one({'_id': ObjectId(subtitle_id)})
    if subtitle:
        # Send the subtitles data to the client for download
        subtitles = subtitle['subtitles']
        filename = subtitle['filename']
        headers = {
            'Content-Disposition': f'attachment;filename={filename.encode("utf-8")}',
            'Content-Type': 'text/plain; charset=utf-8'
        }
        return Response(subtitles, mimetype='text/plain', headers=headers)
    else:
        return 'Subtitles not found'

if __name__ == '__main__':
    app.run(debug=True)

