from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from summarizer2 import summarize_text
from youtube_transcript_summarizer import YT_summarizer
from pdf_summarizer import extract_text_from_pdf, save_summary_to_pdf
from quiz_generator import generate_quiz  
from chatbot import chatbot_response
import mysql.connector

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
SUMMARY_FOLDER = 'static/summaries'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SUMMARY_FOLDER, exist_ok=True)


# =============================
# 1. Home Page
# =============================
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/home')
def home_page():
    return render_template('index.html')


# =============================
#  Youtube Page
# =============================
@app.route('/youtube')
def youtube_page():
    return render_template('youtube.html')


# =============================
#  PDF summarizer Page
# =============================
@app.route('/pdf')
def pdfsummarizer_page():
    return render_template('pdf_s.html')

# =============================
#  Quiz Page
# =============================
@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')


# =============================
#  Previous paper Page
# =============================
@app.route('/pyq')
def pyq_page():
    return render_template('pyq.html')


# =============================
# 2. YouTube Transcript Summarizer
# =============================
@app.route('/summarize_youtube', methods=['POST'])
def summarize_youtube():
    data = request.json
    youtube_link = data['link']
    language = data.get('language', 'en')
    length = int(data.get('length', 50))

    summary = YT_summarizer(youtube_link, length, language)

    return jsonify({'summary': summary})
    

# =============================
# 3. PDF Summarizer
# =============================
@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    file = request.files.get('pdf')
    if not file:
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return jsonify({'success': True, 'filename': filename})

@app.route('/summarize_pdf', methods=['POST'])
def summarize_pdf():
    data = request.get_json()
    filename = data.get('filename')
    word_limit = int(data.get('word_limit', 50))
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(filepath):
        return jsonify({'error': 'Uploaded file not found'}), 404

    extracted_content = extract_text_from_pdf(filepath)
    summary_text = summarize_text(extracted_content, word_limit)

    summary_filename = f"summary_{filename}"
    summary_path = os.path.join(SUMMARY_FOLDER, summary_filename)
    save_summary_to_pdf(summary_text, summary_path)

    download_url = url_for('static', filename=f'summaries/{summary_filename}')
    return jsonify({'summary': summary_text, 'download_url': download_url})


# =============================
# 4. Quiz Maker
# =============================
@app.route('/generater_quiz', methods=['POST'])
def generater_quiz():
    data = request.get_json()
    topic = data.get("topic", "")
    try:
        quiz_json = generate_quiz(topic)
        return jsonify( quiz_json)
    except Exception as e:
        print(f"Error generating quiz: {e}")
        return jsonify({"error": "Quiz generation failed."}), 500
    

# =============================
# 5. Previous Year Papers
# =============================

# MySQL connection config

@app.route('/previous_papers', methods=['POST'])
def previous_papers():
    print("Received POST request at /previous_papers")
    data = request.json
    cursor = db.cursor(dictionary=True)
    query = """
        SELECT * FROM question_papers 
        WHERE branch = %s AND semester = %s AND subjects = %s AND p_year = %s
    """
    cursor.execute(query, (data["branch"], data["semester"], data["subject"], data["year"]))
    results = cursor.fetchall()
    return jsonify(results)


# =============================
# 6. Chatbot
# =============================
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Call your chatbot logic here (Replace this mock response with your own code)
    bot_response = chatbot_response(user_message)

    return jsonify({'reply': bot_response})


if __name__ == '__main__':
    app.run(debug=True)

