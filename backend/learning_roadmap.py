COURSE_DATABASE = {
    "spring boot": [
        {"title": "Spring Boot Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=9SGDpanrc8U"},
        {"title": "Spring Boot - Chad Darby", "platform": "Udemy", "url": "https://www.udemy.com/course/spring-hibernate-tutorial"}
    ],
    "rest api": [
        {"title": "REST API with Spring Boot", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=9SGDpanrc8U"},
        {"title": "REST API Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/api-design"}
    ],
    "react": [
        {"title": "React JS Full Course 2024", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8"},
        {"title": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux"}
    ],
    "javascript": [
        {"title": "JavaScript Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
        {"title": "JavaScript Algorithms", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures"}
    ],
    "html": [
        {"title": "HTML Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=pQN-pnXPaVg"},
        {"title": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design"}
    ],
    "css": [
        {"title": "CSS Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=1Rs2ND1ryYc"},
        {"title": "CSS - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/css-the-complete-guide-incl-flexbox-grid-sass"}
    ],
    "docker": [
        {"title": "Docker Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE"},
        {"title": "Docker and Kubernetes", "platform": "Udemy", "url": "https://www.udemy.com/course/docker-kubernetes-the-practical-guide"}
    ],
    "scikit-learn": [
        {"title": "Scikit-learn Crash Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=0B5eIE_1vpU"},
        {"title": "ML with Python", "platform": "Coursera", "url": "https://www.coursera.org/learn/machine-learning-with-python"}
    ],
    "excel": [
        {"title": "Microsoft Excel Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg"},
        {"title": "Excel Skills for Business", "platform": "Coursera", "url": "https://www.coursera.org/specializations/excel"}
    ],
    "power bi": [
        {"title": "Power BI Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=AGrl-H87pRU"},
        {"title": "Data Analysis with Power BI", "platform": "Coursera", "url": "https://www.coursera.org/learn/data-analysis-power-bi"}
    ],
    "aws": [
        {"title": "AWS Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=k1RI5locZE4"},
        {"title": "AWS Cloud Practitioner", "platform": "Coursera", "url": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials"}
    ],
    "mongodb": [
        {"title": "MongoDB Full Course", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=ExcRbA7fy_A"},
        {"title": "MongoDB Basics", "platform": "MongoDB University", "url": "https://university.mongodb.com/courses/M001/about"}
    ]
}

def get_learning_roadmap(missing_skills):
    roadmap = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        if skill_lower in COURSE_DATABASE:
            roadmap.append({
                "skill":   skill,
                "courses": COURSE_DATABASE[skill_lower]
            })
        else:
            roadmap.append({
                "skill": skill,
                "courses": [
                    {"title": f"Search '{skill}' on YouTube", "platform": "YouTube",
                     "url": f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+tutorial"},
                    {"title": f"Search '{skill}' on Coursera", "platform": "Coursera",
                     "url": f"https://www.coursera.org/search?query={skill.replace(' ', '+')}"}
                ]
            })
    return roadmap