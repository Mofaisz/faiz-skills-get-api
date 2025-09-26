from fastapi import FastAPI
app = FastAPI()
@app.get("/skills")
def get_skills():
    return {
        "name": "Md Faiz Ahmad",
        "role": "Software Engineer",
        "skills": ["React", "React Native", "FastAPI", "JavaScript","TypeScript", "AWS", "Docker","Kubernetes","MySQL"],
        "Experience":"11 Months"
        
    }