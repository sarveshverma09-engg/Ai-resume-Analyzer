# 📄 AI Resume Analyzer with Career Prediction

AI Resume Analyzer is a Streamlit-based web application that analyzes PDF resumes and provides career insights through skill matching and ATS-style scoring. The application extracts resume content, predicts the most suitable career role, identifies missing skills, and generates actionable suggestions to improve the resume.

## 🚀 Features

* Upload and analyze PDF resumes
* Extract resume text using PDF processing
* Predict suitable career roles based on detected skills
* Calculate ATS (Applicant Tracking System) score
* Detect relevant technical skills
* Identify missing skills required for the predicted role
* Rank multiple career paths by match percentage
* Provide resume improvement suggestions

## 🎯 Supported Career Roles

* AI Engineer
* Data Scientist
* Web Developer
* Backend Developer

## 📊 ATS Scoring System

The resume score is calculated using the following criteria:

| Category       | Weight     |
| -------------- | ---------- |
| Skills Match   | 40 Points  |
| Projects       | 30 Points  |
| Certifications | 15 Points  |
| Experience     | 15 Points  |
| Total          | 100 Points |

## 🛠️ Tech Stack

* Python
* Streamlit
* PDFPlumber

## 📂 Project Workflow

1. Upload a PDF resume.
2. Extract resume text.
3. Detect technical skills.
4. Predict the most suitable career role.
5. Calculate ATS score.
6. Identify missing skills.
7. Generate personalized feedback.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📋 Requirements

```text
streamlit
pdfplumber
pandas
```

## 🔮 Future Enhancements

* NLP-based resume parsing
* Support for additional career roles
* Resume report generation
* Job recommendation system
* Advanced ATS evaluation metrics
* Interactive analytics dashboard

## 👨‍💻 Author

**Sarvesh Verma**
B.Tech CSE (AI & ML)

---

If you found this project useful, consider giving it a ⭐ on GitHub.
