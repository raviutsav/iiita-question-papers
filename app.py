from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

click_count = {
    'C1': { 'gvc': 0, 'iml': 0, 'ns': 0, 'ai': 0, 'ivp': 0 },
    'C2': { 'gvc': 0, 'iml': 0, 'ns': 0, 'ai': 0, 'ivp': 0 },
    'C3': { 'gvc': 0, 'iml': 0, 'ns': 0, 'ai': 0, 'ivp': 0 }
}

question_paper_links = {
    'C1': {
        'gvc': 'https://drive.google.com/file/d/1iRggemJrpHwpZAdljkrDP9NE5bb0vhRs/view?usp=sharing', 
        'iml': 'https://drive.google.com/file/d/1iZVR9E8sZY6MenKP6WC8t8X4QDwn3GXx/view?usp=sharing', 
        'ns': 'https://drive.google.com/file/d/1QszTv3jmFM-78ZXo9HkD7Pg-bXSk4By_/view?usp=sharing', 
        'ai': 'https://drive.google.com/file/d/1jAsia2mlczrsCjiBEeZJ4pmy0r72tM6P/view?usp=sharing', 
        'ivp': 'https://drive.google.com/file/d/1frJlgINaaM8CVZMYMe9ho5Dlc9Wvca8z/view?usp=sharing'
    },

    'C2': {
        'gvc': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'iml': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ns': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ai': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ivp': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    },

    'C3': {
        'gvc': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'iml': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ns': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ai': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        'ivp': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    }
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stats')
def stats():
    return render_template('stats.html', click_count = click_count)


@app.route('/paper/<string:subject>/<string:cx>')
def question_paper(subject, cx):
    click_count[cx][subject] += 1
    return redirect(question_paper_links[cx][subject])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
