from flask import Flask, render_template, request, jsonify
from pytube import YouTube 


app = Flask(__name__) # name for the Flask app (refer to output)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')


@app.route('/form-handler', methods=['POST'])
def handle_data():
   
    link = request.form['url']
    
    try: 
        youtube = YouTube(link) 
    except: 
        return "Connection Error"
    d_video = youtube.streams.get_highest_resolution()
    try: 
        # downloading the video 
        d_video.download() 
    except: 
        return "Some Error!"
    return 'Task Completed!'

# running the server
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False)
