# AI Job Recommender & Skill Gap Analyzer

An AI-powered system that analyzes your resume and recommends jobs based on your skills.

## 🌐 Live Demo
👉 https://ai-job-recommender-1jqw.onrender.com/ui

## ✨ Features
- Resume Parser using NLP (spaCy)
- Job Recommendation using TF-IDF + Cosine Similarity
- Skill Gap Analysis
- Learning Roadmap with real course links (YouTube, Coursera, Udemy)

## 🧠 Technologies Used
- Python, Flask, spaCy, Scikit-learn, PyMuPDF
- HTML, CSS, JavaScript
- Deployed on Render.com

## 🚀 How to Run Locally
1. Install dependencies:
pip install flask flask-cors spacy scikit-learn PyMuPDF
python -m spacy download en_core_web_sm

2. Start the server:
cd backend
python app.py

3. Open browser:
http://127.0.0.1:5000/ui

## ⚠️ Note for Local Development
If running locally, open backend/index.html and change this line:
xhr.open('POST', 'https://ai-job-recommender-1jqw.onrender.com/full-analysis', true);
back to:
xhr.open('POST', 'http://127.0.0.1:5000/full-analysis', true);


## 📁 Project Structure
- backend/ - Flask API + ML modules
- data/ - Job dataset
- frontend/ - UI files

## 👨‍💻 Author
Harsh Gokul Memane
M.Tech Computer Science (Intelligent Systems and Analytics)
MIT ADT University, Pune