import fitz  # PyMuPDF
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Common tech skills to detect
SKILLS_LIST = [
    "python", "java", "javascript", "react", "spring boot", "sql", "mysql",
    "mongodb", "html", "css", "machine learning", "deep learning", "nlp",
    "tensorflow", "scikit-learn", "docker", "git", "rest api", "flask",
    "django", "nodejs", "c++", "c#", "aws", "linux", "excel", "power bi"
]

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_skills(text):
    found_skills = []
    for skill in SKILLS_LIST:
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))

def extract_email(text):
    match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return match[0] if match else "Not found"

def extract_phone(text):
    match = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return match[0] if match else "Not found"

def extract_education(text):
    education_keywords = ["b.tech", "m.tech", "bsc", "msc", "bachelor", 
                         "master", "phd", "diploma", "degree", "university", "college"]
    lines = text.split('\n')
    education = []
    for line in lines:
        if any(keyword in line.lower() for keyword in education_keywords):
            clean = line.strip()
            if len(clean) > 5:
                education.append(clean)
    return education[:3]  # return top 3 matches

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    return {
        "email":     extract_email(text),
        "phone":     extract_phone(text),
        "skills":    extract_skills(text),
        "education": extract_education(text),
        "raw_text":  text[:500]  # first 500 chars preview
    }