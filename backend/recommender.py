from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

def load_jobs():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'jobs.json')
    with open(path, 'r') as f:
        return json.load(f)

def recommend_jobs(user_skills):
    jobs = load_jobs()

    # Convert user skills list to a single string
    user_profile = ' '.join(user_skills)

    # Build list of job descriptions
    job_descriptions = [job['description'] for job in jobs]

    # Add user profile at the beginning
    all_texts = [user_profile] + job_descriptions

    # Apply TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Calculate cosine similarity between user and each job
    user_vector = tfidf_matrix[0]
    job_vectors = tfidf_matrix[1:]
    similarities = cosine_similarity(user_vector, job_vectors)[0]

    # Attach scores to jobs and sort
    for i, job in enumerate(jobs):
        job['match_score'] = round(float(similarities[i]) * 100, 2)

    ranked_jobs = sorted(jobs, key=lambda x: x['match_score'], reverse=True)
    return ranked_jobs