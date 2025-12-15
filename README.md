# AI-Generated Portfolio Website from Resume 🚀

An AI-powered web application that automatically converts a user's **PDF resume** into a fully functional **portfolio website** containing clean, modern, and responsive **HTML, CSS, and JavaScript** code.

Built using **Google Gemini (via LangChain)** and deployed through **Streamlit**, this tool produces a downloadable website package and shows a live preview instantly.

---

## 🌟 Features

- 📄 Upload your **PDF resume**
- 🤖 AI extracts information and generates website code
- 🎨 Professional frontend (HTML + CSS + JS)
- 🖥️ Live website preview inside Streamlit
- 💾 Downloadable ZIP package
- ⚡ Powered by **Gemini 2.5 Flash**
- 🎆 Fully styled neon-themed UI for a premium user experience

---

## 📘 Problem Statement

Creating a portfolio website normally requires:

- Knowledge of HTML/CSS/JS  
- Time to convert resume content into structured sections  
- Design expertise  

Many users lack the skills or time to build a polished website manually.

---

## 💡 Solution Overview

This project automates the entire workflow by:

1. Extracting resume text  
2. Using AI to create a structured website prompt  
3. Generating complete HTML/CSS/JS website code  
4. Rendering the output inside Streamlit  
5. Providing a downloadable ZIP package  

---

## 🏗️ System Architecture

### Components
- Streamlit UI  
- PyPDF2 (PDF parsing)  
- LangChain + Google Gemini  
- HTML preview engine  
- ZIP packaging module  

### Workflow
1. **Upload Resume (PDF)**
2. **Extract Text using PyPDF2**
3. **LLM Prompt → Website Code**
4. **Live HTML Preview**
5. **ZIP Download (HTML/CSS/JS)**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| UI | Streamlit |
| PDF Parser | PyPDF2 |
| LLM Workflow | LangChain |
| AI Model | Gemini 2.5 Flash |
| Packaging | zipfile |
| Rendering | Streamlit HTML components |

---

## 📦 Requirements
```txt
streamlit
langchain
langchain_google_genai
dotenv
PyPDF2
```
---

## 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

---

## 2. Install Dependencies
```bash
pip install -r req.txt
```

---

## 3. Add Your API Key
**Create a .env file:**
```ini
gemini=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## 4. Run the Application
```bash
streamlit run main.py
```

---

## 🧠 How AI Generation Works
### 1. Extract Resume Content
```python
for page in pdfreader.pages:
    text += page.extract_text() or ""
```

---

### 2. Send Extracted Text to Gemini
**The AI must output in this strict format:**
```css
--html--
[HTML code]
--html--

--css--
[CSS code]
--css--

--js--
[JS code]
--js--
```

---

### 3. Save Files
```python
file.write(response.content.split("--html--")[1])
```

---
### 4. ZIP Packaging
```python
zip.write("index.html")
zip.write("style.css")
zip.write("script.js")
```

---

### 5. Website Preview
```python
components.html(html_content, height=700, scrolling=True)
```

---
