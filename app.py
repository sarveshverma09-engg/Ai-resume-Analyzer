import streamlit as st
import pdfplumber

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer with Career Prediction")

# -----------------------------------
# ROLE DATABASE
# -----------------------------------

role_skills = {

    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas",
        "sql",
        "git",
        "github"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "pandas",
        "numpy",
        "statistics",
        "data analysis",
        "matplotlib",
        "machine learning"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "nodejs",
        "bootstrap",
        "git",
        "github"
    ],

    "Backend Developer": [
        "python",
        "django",
        "flask",
        "api",
        "sql",
        "postgresql",
        "git",
        "github"
    ]
}

# -----------------------------------
# PDF TEXT EXTRACTION
# -----------------------------------

def extract_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text.lower()


# -----------------------------------
# ROLE PREDICTION
# -----------------------------------

def predict_role(text):

    role_scores = {}

    for role, skills in role_skills.items():

        matched = 0

        for skill in skills:

            if skill.lower() in text:
                matched += 1

        percentage = (
            matched / len(skills)
        ) * 100

        role_scores[role] = percentage

    predicted_role = max(
        role_scores,
        key=role_scores.get
    )

    confidence = role_scores[predicted_role]

    return predicted_role, confidence, role_scores


# -----------------------------------
# SKILL DETECTION
# -----------------------------------

def find_skills(text, skills):

    found = []

    for skill in skills:

        if skill.lower() in text:
            found.append(skill)

    return found


# -----------------------------------
# PROJECT SCORE
# -----------------------------------

def detect_projects(text):

    keywords = [
        "project",
        "developed",
        "created",
        "built",
        "implemented"
    ]

    score = 0

    for word in keywords:

        if word in text:
            score += 6

    return min(score, 30)


# -----------------------------------
# CERTIFICATION SCORE
# -----------------------------------

def detect_certifications(text):

    keywords = [
        "certificate",
        "certification",
        "coursera",
        "google",
        "aws",
        "udemy"
    ]

    score = 0

    for word in keywords:

        if word in text:
            score += 3

    return min(score, 15)


# -----------------------------------
# EXPERIENCE SCORE
# -----------------------------------

def detect_experience(text):

    keywords = [
        "internship",
        "intern",
        "experience",
        "worked"
    ]

    score = 0

    for word in keywords:

        if word in text:
            score += 4

    return min(score, 15)


# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# -----------------------------------
# MAIN ANALYSIS
# -----------------------------------

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        text[:3000],
        height=250
    )

    # Predict Role

    predicted_role, confidence, all_scores = predict_role(text)

    st.subheader("🎯 Predicted Career Role")

    st.success(
        f"{predicted_role} ({confidence:.1f}% Match)"
    )

    required_skills = role_skills[predicted_role]

    detected_skills = find_skills(
        text,
        required_skills
    )

    # Missing Skills

    missing_skills = []

    for skill in required_skills:

        if skill not in detected_skills:
            missing_skills.append(skill)

    # ATS Score Calculation

    skill_score = int(
        (
            len(detected_skills)
            /
            len(required_skills)
        ) * 40
    )

    project_score = detect_projects(text)

    cert_score = detect_certifications(text)

    exp_score = detect_experience(text)

    total_score = (
        skill_score
        + project_score
        + cert_score
        + exp_score
    )

    total_score = min(total_score, 100)

    # -----------------------------------
    # SCORE DISPLAY
    # -----------------------------------

    st.subheader("📊 ATS Resume Score")

    st.progress(total_score)

    st.write(
        f"### {total_score}/100"
    )

    # -----------------------------------
    # SCORE BREAKDOWN
    # -----------------------------------

    st.subheader("📈 Score Breakdown")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Skills Score",
            f"{skill_score}/40"
        )

        st.metric(
            "Projects Score",
            f"{project_score}/30"
        )

    with col2:
        st.metric(
            "Certification Score",
            f"{cert_score}/15"
        )

        st.metric(
            "Experience Score",
            f"{exp_score}/15"
        )

    # -----------------------------------
    # DETECTED SKILLS
    # -----------------------------------

    st.subheader("✅ Detected Skills")

    if detected_skills:

        st.success(
            ", ".join(detected_skills)
        )

    else:

        st.warning(
            "No relevant skills found."
        )

    # -----------------------------------
    # MISSING SKILLS
    # -----------------------------------

    st.subheader("❌ Missing Skills")

    if missing_skills:

        st.warning(
            ", ".join(missing_skills)
        )

    else:

        st.success(
            "No important skills missing."
        )

    # -----------------------------------
    # ROLE RANKING
    # -----------------------------------

    st.subheader("🏆 Career Match Ranking")

    sorted_roles = sorted(
        all_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for role, score in sorted_roles:

        st.write(
            f"**{role}** : {score:.1f}%"
        )

    # -----------------------------------
    # FINAL FEEDBACK
    # -----------------------------------

    st.subheader("💡 Suggestions")

    if total_score >= 85:

        st.success(
            "Excellent Resume. Ready for internships and placements."
        )

    elif total_score >= 70:

        st.info(
            "Good Resume. Add more projects and certifications."
        )

    elif total_score >= 50:

        st.warning(
            "Improve skills, projects and certifications."
        )

    else:

        st.error(
            "Resume needs major improvements."
        )