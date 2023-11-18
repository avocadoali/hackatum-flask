from flask import Flask, render_template, send_file, Response

app = Flask(__name__)

# Replace 'path/to/your/video.mp4' with the path to your video file
video_path = '/home/ali/projects/hackatum/video_sound_files/susanne.wav'

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    with open(video_path, 'rb') as video_file:
        while True:
            # Read the video file in chunks
            chunk = video_file.read(1024)
            if not chunk:
                break

            yield chunk

@app.route('/video')
def video():
    # Use the Response class to create a streaming response
    return Response(generate(), mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)

