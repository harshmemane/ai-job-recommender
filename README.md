# AI Job Recommender & Skill Gap Analyzer

An AI-powered system that analyzes your resume and recommends jobs based on your skills.

## Features
- Resume Parser using NLP (spaCy)
- Job Recommendation using TF-IDF + Cosine Similarity
- Skill Gap Analysis
- Learning Roadmap with course suggestions

## Technologies Used
- Python, Flask, spaCy, Scikit-learn, PyMuPDF
- HTML, CSS, JavaScript

## How to Run
1. Install dependencies:
pip install flask flask-cors spacy scikit-learn PyMuPDF
python -m spacy download en_core_web_sm

2. Start the server:
cd backend
python app.py

3. Open browser:
http://127.0.0.1:5000/ui

## Project Structure
- backend/ - Flask API + ML modules
- data/ - Job dataset
- frontend/ - UI files