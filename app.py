import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import timedelta
from moviepy.config import change_settings
import tempfile
import ffmpeg
import whisper

# Set the path to the ImageMagick binary (if required)
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

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
    temp_dir = tempfile.gettempdir()
    audio_path = os.path.join(temp_dir, 'audio.wav')

    # Extract audio from video
    ffmpeg.input(video_path).output(audio_path, acodec='pcm_s16le', ac=1, ar='16k').run(quiet=True, overwrite_output=True)

    # Load Whisper model
    model_name = 'small'
    model = whisper.load_model(model_name)

    # Transcribe audio to generate subtitles
    result = model.transcribe(audio_path)

    # Prepare subtitles in SRT format
    subtitles = ""
    for i, segment in enumerate(result['segments'], start=1):
        start_time = timedelta(seconds=segment['start'])
        end_time = timedelta(seconds=segment['end'])
        text = segment['text']
        subtitles += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"

    return subtitles

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
    # Fetch subtitles from MongoDB
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
    os.makedirs(os.path.dirname(video_path), exist_ok=True)
    video_file.save(video_path)
    
    # Generate subtitles
    generated_subtitles = generate_subtitles(video_path)
    
    # Save the subtitles to a temporary SRT file
    srt_path = os.path.join(tempfile.gettempdir(), video_file.filename.split('.')[0] + '.srt')
    with open(srt_path, 'w') as f:
        f.write(generated_subtitles)
    
    # Embed subtitles into the video
    output_video_path = os.path.join(tempfile.gettempdir(), 'output_' + video_file.filename)
    video_clip = VideoFileClip(video_path)
    
    subtitle_clips = []
    for line in generated_subtitles.split("\n\n"):
        if line.strip():
            parts = line.split("\n")
            index = parts[0]
            time_range = parts[1].split(" --> ")
            start_time = sum(x * float(t) for x, t in zip([3600, 60, 1], time_range[0].split(":")))
            end_time = sum(x * float(t) for x, t in zip([3600, 60, 1], time_range[1].split(":")))
            text = " ".join(parts[2:])
            subtitle_clip = TextClip(text, font='Arial', fontsize=24, color='white', bg_color='black')
            subtitle_clip = subtitle_clip.set_position(('center', 'bottom')).set_start(start_time).set_end(end_time)
            subtitle_clips.append(subtitle_clip)
    
    final_video = CompositeVideoClip([video_clip] + subtitle_clips)
    final_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
    
    # Save the subtitles and video path to MongoDB
    subtitles_id = subtitles_collection.insert_one({
        'filename': video_file.filename,
        'subtitles': generated_subtitles,
        'output_video_path': output_video_path
    }).inserted_id
    
    # Redirect to dashboard or display success message
    return redirect(url_for('dashboard'))

@app.route('/download_video/<subtitle_id>')
def download_video(subtitle_id):
    subtitle = subtitles_collection.find_one({'_id': ObjectId(subtitle_id)})
    if subtitle:
        output_video_path = subtitle['output_video_path']
        if os.path.exists(output_video_path):
            return send_file(output_video_path, as_attachment=True, download_name='video_with_subtitles.mp4')
        else:
            return 'Processed video not found'
    else:
        return 'Subtitles not found'

if __name__ == '__main__':
    app.run(debug=True)
