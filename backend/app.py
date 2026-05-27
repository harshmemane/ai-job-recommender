from flask import Flask, request, jsonify, make_response, send_file
from resume_parser import parse_resume
from recommender import recommend_jobs
from skill_gap import analyze_skill_gap
from learning_roadmap import get_learning_roadmap
import os

app = Flask(__name__)

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin']  = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.after_request
def after_request(response):
    return add_cors_headers(response)

@app.route('/', methods=['GET','OPTIONS'])
def home():
    return jsonify({"message": "Job Recommender API is running!"})

@app.route('/test', methods=['GET','OPTIONS'])
def test():
    return jsonify({"status": "success", "message": "Backend is working correctly"})

@app.route('/ui')
def ui():
    return send_file('index.html')

@app.route('/parse-resume', methods=['POST','OPTIONS'])
def parse():
    if request.method == 'OPTIONS':
        return make_response('', 204)
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['resume']
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Only PDF files are supported"}), 400
    save_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(save_path)
    result = parse_resume(save_path)
    return jsonify(result)

@app.route('/recommend', methods=['POST','OPTIONS'])
def recommend():
    if request.method == 'OPTIONS':
        return make_response('', 204)
    data = request.get_json()
    if not data or 'skills' not in data:
        return jsonify({"error": "Please provide skills list"}), 400
    recommendations = recommend_jobs(data['skills'])
    return jsonify(recommendations)

@app.route('/analyze', methods=['POST','OPTIONS'])
def analyze():
    if request.method == 'OPTIONS':
        return make_response('', 204)
    data = request.get_json()
    if not data or 'skills' not in data:
        return jsonify({"error": "Please provide skills list"}), 400
    jobs = recommend_jobs(data['skills'])
    gap_analysis = analyze_skill_gap(data['skills'], jobs)
    return jsonify(gap_analysis)

@app.route('/full-analysis', methods=['POST','OPTIONS'])
def full_analysis():
    if request.method == 'OPTIONS':
        return make_response('', 204)
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['resume']
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Only PDF files are supported"}), 400
    save_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(save_path)
    parsed       = parse_resume(save_path)
    skills       = parsed['skills']
    jobs         = recommend_jobs(skills)
    gap_analysis = analyze_skill_gap(skills, jobs)
    all_missing  = []
    for job in gap_analysis:
        all_missing.extend(job['missing_skills'])
    unique_missing = list(set(all_missing))
    roadmap = get_learning_roadmap(unique_missing)
    return jsonify({
        "candidate":        parsed,
        "recommended_jobs": jobs[:3],
        "skill_gaps":       gap_analysis,
        "learning_roadmap": roadmap
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)