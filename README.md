# 🎯 CareerAI – Your Intelligent Career Assistant

CareerAI is an AI-powered resume analysis application that helps job seekers optimize their resumes for specific job descriptions. It evaluates resume-job compatibility, performs ATS (Applicant Tracking System) analysis, identifies missing skills, and provides personalized career recommendations using Google's Gemini AI.

Built with Python and Streamlit, CareerAI combines traditional resume analysis with Generative AI to deliver actionable feedback that helps users improve their chances of landing interviews.

---

## ✨ Features

### 📄 Resume Parsing
- Upload resumes in PDF format
- Automatically extracts text from resumes
- Supports structured resume analysis

### 📋 Job Description Parsing
- Upload job descriptions in PDF format
- Extracts required skills and keywords
- Enables resume-job comparison

### 🧠 Skill Extraction
- Identifies technical skills from both the resume and job description
- Categorizes skills into:
  - Programming Languages
  - Data Analytics
  - Machine Learning
  - Cloud Technologies
  - Data Engineering
  - Databases
  - Tools & Platforms

### 🎯 Resume Match Score
- Calculates the overall compatibility between the resume and the job description
- Displays:
  - Match Percentage
  - Matched Skills
  - Missing Skills

### 📑 ATS Resume Checker
Evaluates resumes for ATS compatibility by checking:
- Resume length
- Email address
- Phone number
- Section headings
- Overall ATS score

Provides recommendations to improve ATS performance.

### 🤖 AI Career Insights (Powered by Gemini)
Generates personalized feedback including:
- Overall resume assessment
- Strengths
- Weaknesses
- Resume improvement suggestions
- Learning roadmap
- Career advice

---

# 🛠 Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### AI
- Google Gemini API

### Libraries
- pdfplumber
- python-dotenv
- google-genai
- pandas

### Tools
- Git
- GitHub

---

# 📁 Project Structure

```text
CareerAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── src/
│   ├── ai/
│   │   ├── gemini_client.py
│   │   ├── prompt_builder.py
│   │   └── feedback_generator.py
│   │
│   ├── analysis/
│   │   ├── analyzer.py
│   │   ├── ats_checker.py
│   │   └── scorer.py
│   │
│   ├── extractors/
│   │   └── skill_extractor.py
│   │
│   ├── parsers/
│   │   ├── resume_parser.py
│   │   └── jd_parser.py
│   │
│   └── ui/
│       ├── theme.py
│       └── results.py
│
└── tests/
    └── test_gemini.py
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Tejashwita-18/CareerAI.git

cd CareerAI
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Gemini API

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain a free API key from Google AI Studio.

---

## 5. Run the application

```bash
streamlit run app.py
```

---

# 📊 Application Workflow

```text
Upload Resume
        │
        ▼
Extract Resume Text
        │
        ▼
Upload Job Description
        │
        ▼
Extract Job Description
        │
        ▼
Skill Extraction
        │
        ▼
Resume Match Scoring
        │
        ▼
ATS Analysis
        │
        ▼
Gemini AI Feedback
        │
        ▼
Interactive Dashboard
```

---

# 📸 Screenshots

## Home Page

> Add a screenshot here

---

## Resume Analysis

> Add a screenshot here

---

## AI Career Insights

> Add a screenshot here

---

# 💡 Future Enhancements

- Resume rewriting using AI
- Cover letter generation
- Interview question generator
- Resume scoring history
- Resume comparison against multiple job descriptions
- Resume keyword optimization
- Export AI report as PDF
- Cloud deployment

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Object-Oriented Programming
- Modular Software Design
- Prompt Engineering
- REST API Integration
- Generative AI
- Streamlit Development
- Resume Parsing
- ATS Optimization
- Git Version Control
- Python Project Architecture

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve CareerAI, feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Tejashwita Priya**

Master of Data Science  
Monash University

GitHub: https://github.com/Tejashwita-18

LinkedIn: https://www.linkedin.com/in/tejashwita-priya-4302311b9/