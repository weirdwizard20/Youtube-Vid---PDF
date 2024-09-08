# app.py
from flask import Flask, render_template, request, send_file
from pdf_generator import generate_pdf_from_youtube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    youtube_link = request.form['youtube_link']
    pdf_path = generate_pdf_from_youtube(youtube_link)
    if pdf_path != "Invalid YouTube URL":
        return send_file(pdf_path, as_attachment=True)
    else:
        return "Invalid YouTube URL"

if __name__ == '__main__':
    app.run(debug=True)
