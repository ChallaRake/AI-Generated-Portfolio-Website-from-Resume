# import streamlit as st
# import dotenv
# import langchain
# from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()
# import os
# import zipfile
# from PyPDF2 import PdfReader
# import pandas as pd
# from io import StringIO
# from io import BytesIO
# import streamlit.components.v1 as components


# os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

# st.set_page_config(page_title="AI Portfolio Website Creation",page_icon="")

# st.title("AI-Generated Portfolio Website from Resume")


# file = st.file_uploader("Choose a file",type="pdf")

# if file is not None:
#     pdfreader = PdfReader(file)

#     text = ""
#     for page in pdfreader.pages:
#         text += page.extract_text() or ""  # Avoid NoneType errors
    
#     # st.subheader("Extracted Text")
#     # st.write(text if text.strip() else "No extractable text found.")
#     text = text.strip()


#     if st.button("Generate Portfolio"):
#         message=["system","""You are an expert in web development, specializing in frontend technologies. 
#                 Your role is to generate clean, responsive, and professional html, css, and JavaScript code for creating a 
#                 complete frontend professional portfolio website based on the given user's text.

#                 Always produce the output in the exact format shown below:
                
#                 --html--
#                 [html code]
#                 --html--
                
#                 --css--
#                 [css code]
#                 --css--
                
#                 --js--
#                 [js code]
#                 --js--
                
#                 """]
#         message.append(("user",text))

#         model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#         response = model.invoke(message)

        
#         with open("file.txt", "w",encoding="utf-8") as file:
#             file.write(response.content)

#         # st.write("Success")

#         with open("index.html","w",encoding="utf-8") as file:
#             file.write(response.content.split("--html--")[1])

#         with open("style.css","w",encoding="utf-8") as file:
#             file.write(response.content.split("--css--")[1])

#         with open("script.js","w",encoding="utf-8") as file:
#             file.write(response.content.split("--js--")[1])

#         with zipfile.ZipFile("portfolio.zip","w") as zip:
#             zip.write("index.html")
#             zip.write("style.css")
#             zip.write("script.js")

#         st.subheader("Website render preview")
#         with open("index.html", "r", encoding="utf-8") as f:
#             html_content = f.read()
        
#         components.html(html_content, height=700, scrolling=True)

#         st.download_button("click to download",
#                         data=open("portfolio.zip","rb"),
#                         file_name="portfolio.zip")
        
#         st.write("success")



# import streamlit as st
# import dotenv
# import langchain
# from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()
# import os
# import zipfile
# from PyPDF2 import PdfReader
# import pandas as pd
# from io import StringIO
# from io import BytesIO
# import streamlit.components.v1 as components


# os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

# # Advanced page configuration with custom theme
# st.set_page_config(
#     page_title="AI Portfolio Website Creation",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for advanced dark theme with neon styling
# st.markdown("""
#     <style>
#     /* Import Google Fonts */
#     @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap');
    
#     /* Main container styling - Dark Theme */
#     .main {
#         background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
#         font-family: 'Inter', sans-serif;
#         color: #e0e0e0;
#     }
    
#     /* Styledblock container */
#     .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#         max-width: 1200px;
#     }
    
#     /* Neon Title Header */
#     .neon-header {
#         background: rgba(10, 14, 39, 0.8);
#         padding: 4rem 2rem;
#         border-radius: 25px;
#         text-align: center;
#         box-shadow: 
#             0 0 20px rgba(0, 255, 255, 0.3),
#             0 0 40px rgba(255, 0, 255, 0.2),
#             0 15px 50px rgba(0, 0, 0, 0.5);
#         margin-bottom: 2rem;
#         animation: fadeInDown 0.8s ease-out;
#         border: 2px solid rgba(0, 255, 255, 0.3);
#         position: relative;
#         overflow: hidden;
#     }
    
#     .neon-header::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.1), transparent);
#         animation: shine 3s infinite;
#     }
    
#     @keyframes shine {
#         0% { left: -100%; }
#         100% { left: 100%; }
#     }
    
#     .neon-title {
#         font-family: 'Orbitron', sans-serif;
#         font-size: 4rem;
#         font-weight: 900;
#         margin-bottom: 1rem;
#         position: relative;
#         text-transform: uppercase;
#         letter-spacing: 0.1em;
#         background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ff00);
#         background-size: 300% 300%;
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         animation: neonGlow 3s ease-in-out infinite, gradientShift 5s ease infinite;
#         filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.8))
#                 drop-shadow(0 0 20px rgba(255, 0, 255, 0.6))
#                 drop-shadow(0 0 30px rgba(255, 255, 0, 0.4));
#     }
    
#     @keyframes neonGlow {
#         0%, 100% {
#             filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.8))
#                     drop-shadow(0 0 20px rgba(255, 0, 255, 0.6))
#                     drop-shadow(0 0 30px rgba(255, 255, 0, 0.4));
#         }
#         50% {
#             filter: drop-shadow(0 0 20px rgba(0, 255, 255, 1))
#                     drop-shadow(0 0 40px rgba(255, 0, 255, 0.8))
#                     drop-shadow(0 0 60px rgba(255, 255, 0, 0.6));
#         }
#     }
    
#     @keyframes gradientShift {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }
    
#     .neon-subtitle {
#         color: #00ffff;
#         font-size: 1.3rem;
#         font-weight: 300;
#         text-shadow: 
#             0 0 10px rgba(0, 255, 255, 0.8),
#             0 0 20px rgba(0, 255, 255, 0.5);
#         letter-spacing: 0.05em;
#     }
    
#     /* Feature cards with dark theme */
#     .feature-card {
#         background: linear-gradient(135deg, rgba(26, 26, 46, 0.95) 0%, rgba(22, 33, 62, 0.95) 100%);
#         padding: 2rem;
#         border-radius: 20px;
#         box-shadow: 
#             0 5px 20px rgba(0, 0, 0, 0.5),
#             0 0 15px rgba(0, 255, 255, 0.1);
#         margin: 1rem 0;
#         transition: transform 0.3s ease, box-shadow 0.3s ease;
#         border: 1px solid rgba(0, 255, 255, 0.2);
#     }
    
#     .feature-card:hover {
#         transform: translateY(-8px);
#         box-shadow: 
#             0 10px 40px rgba(0, 0, 0, 0.6),
#             0 0 30px rgba(0, 255, 255, 0.3),
#             0 0 40px rgba(255, 0, 255, 0.2);
#         border: 1px solid rgba(0, 255, 255, 0.5);
#     }
    
#     .feature-icon {
#         font-size: 3rem;
#         margin-bottom: 1rem;
#         filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.5));
#     }
    
#     .feature-title {
#         font-size: 1.5rem;
#         font-weight: 600;
#         background: linear-gradient(90deg, #00ffff, #00ff00);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 0.5rem;
#     }
    
#     .feature-description {
#         color: #b0b0b0;
#         font-size: 1rem;
#         line-height: 1.6;
#     }
    
#     /* Upload section with neon glow */
#     .upload-section {
#         background: rgba(26, 26, 46, 0.8);
#         padding: 3rem;
#         border-radius: 20px;
#         box-shadow: 
#             0 10px 40px rgba(0, 0, 0, 0.5),
#             0 0 20px rgba(255, 0, 255, 0.2);
#         margin: 2rem 0;
#         border: 3px dashed rgba(255, 0, 255, 0.5);
#         text-align: center;
#         transition: all 0.3s ease;
#     }
    
#     .upload-section:hover {
#         border-color: rgba(0, 255, 255, 0.7);
#         box-shadow: 
#             0 15px 50px rgba(0, 0, 0, 0.6),
#             0 0 40px rgba(0, 255, 255, 0.3);
#     }
    
#     /* Custom button styling with vibrant colors */
#     .stButton>button {
#         background: linear-gradient(135deg, #ff00ff 0%, #00ffff 50%, #ffff00 100%);
#         color: #000;
#         border: none;
#         padding: 1rem 3rem;
#         border-radius: 50px;
#         font-size: 1.1rem;
#         font-weight: 700;
#         box-shadow: 
#             0 5px 20px rgba(255, 0, 255, 0.4),
#             0 0 20px rgba(0, 255, 255, 0.3);
#         transition: all 0.3s ease;
#         width: 100%;
#         margin-top: 1rem;
#         text-transform: uppercase;
#         letter-spacing: 0.05em;
#     }
    
#     .stButton>button:hover {
#         transform: translateY(-3px) scale(1.02);
#         box-shadow: 
#             0 8px 30px rgba(255, 0, 255, 0.6),
#             0 0 40px rgba(0, 255, 255, 0.5);
#         background: linear-gradient(135deg, #ffff00 0%, #00ffff 50%, #ff00ff 100%);
#     }
    
#     /* Download button with different neon color */
#     .stDownloadButton>button {
#         background: linear-gradient(135deg, #00ff00 0%, #00ffff 50%, #0080ff 100%);
#         color: #000;
#         border: none;
#         padding: 1rem 3rem;
#         border-radius: 50px;
#         font-size: 1.1rem;
#         font-weight: 700;
#         box-shadow: 
#             0 5px 20px rgba(0, 255, 0, 0.4),
#             0 0 20px rgba(0, 255, 255, 0.3);
#         transition: all 0.3s ease;
#         width: 100%;
#         text-transform: uppercase;
#         letter-spacing: 0.05em;
#     }
    
#     .stDownloadButton>button:hover {
#         transform: translateY(-3px) scale(1.02);
#         box-shadow: 
#             0 8px 30px rgba(0, 255, 0, 0.6),
#             0 0 40px rgba(0, 255, 255, 0.5);
#     }
    
#     /* Success message with neon green */
#     .success-message {
#         background: linear-gradient(135deg, rgba(0, 255, 0, 0.2) 0%, rgba(0, 255, 255, 0.2) 100%);
#         color: #00ff00;
#         padding: 1.5rem;
#         border-radius: 15px;
#         text-align: center;
#         font-size: 1.2rem;
#         font-weight: 600;
#         margin: 2rem 0;
#         animation: fadeIn 0.5s ease-out;
#         border: 2px solid rgba(0, 255, 0, 0.5);
#         box-shadow: 
#             0 0 20px rgba(0, 255, 0, 0.3),
#             0 5px 20px rgba(0, 0, 0, 0.4);
#         text-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
#     }
    
#     /* Preview section with dark theme */
#     .preview-container {
#         background: rgba(26, 26, 46, 0.9);
#         padding: 2rem;
#         border-radius: 20px;
#         box-shadow: 
#             0 10px 40px rgba(0, 0, 0, 0.5),
#             0 0 20px rgba(255, 0, 255, 0.2);
#         margin: 2rem 0;
#         border: 1px solid rgba(0, 255, 255, 0.3);
#     }
    
#     .preview-header {
#         font-size: 2rem;
#         font-weight: 600;
#         background: linear-gradient(90deg, #ff00ff, #00ffff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 1.5rem;
#         text-align: center;
#         text-transform: uppercase;
#         letter-spacing: 0.1em;
#     }
    
#     /* Animations */
#     @keyframes fadeInDown {
#         from {
#             opacity: 0;
#             transform: translateY(-30px);
#         }
#         to {
#             opacity: 1;
#             transform: translateY(0);
#         }
#     }
    
#     @keyframes fadeIn {
#         from {
#             opacity: 0;
#         }
#         to {
#             opacity: 1;
#         }
#     }
    
#     /* Sidebar styling with dark theme */
#     .css-1d391kg {
#         background: linear-gradient(180deg, #0a0e27 0%, #1a1a2e 100%);
#     }
    
#     [data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #0a0e27 0%, #1a1a2e 100%);
#     }
    
#     [data-testid="stSidebar"] * {
#         color: #e0e0e0 !important;
#     }
    
#     /* File uploader styling */
#     .stFileUploader {
#         background: rgba(255, 0, 255, 0.1);
#         padding: 2rem;
#         border-radius: 15px;
#         border: 2px solid rgba(255, 0, 255, 0.3);
#     }
    
#     /* Progress bar styling with neon */
#     .stProgress > div > div > div {
#         background: linear-gradient(90deg, #00ff00, #00ffff, #ff00ff);
#     }
    
#     /* Info boxes with dark theme */
#     .info-box {
#         background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%);
#         padding: 1.5rem;
#         border-radius: 15px;
#         border-left: 5px solid #00ffff;
#         margin: 1rem 0;
#         box-shadow: 
#             0 5px 15px rgba(0, 0, 0, 0.3),
#             0 0 10px rgba(0, 255, 255, 0.2);
#         color: #010101;
#     }
    
#     .info-box-title {
#         font-weight: 600;
#         background: linear-gradient(90deg, #00ffff, #00ff00);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 0.5rem;
#         font-size: 1.1rem;
#     }
    
#     /* Steps container */
#     .steps-container {
#         display: flex;
#         justify-content: space-around;
#         margin: 2rem 0;
#         flex-wrap: wrap;
#     }
    
#     .step-item {
#         text-align: center;
#         flex: 1;
#         min-width: 200px;
#         padding: 1rem;
#     }
    
#     .step-number {
#         background: linear-gradient(135deg, #ff00ff 0%, #00ffff 100%);
#         color: #000;
#         width: 70px;
#         height: 70px;
#         border-radius: 50%;
#         display: inline-flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 1.8rem;
#         font-weight: 900;
#         margin-bottom: 1rem;
#         box-shadow: 
#             0 5px 20px rgba(255, 0, 255, 0.4),
#             0 0 20px rgba(0, 255, 255, 0.3);
#         font-family: 'Orbitron', sans-serif;
#     }
    
#     .step-title {
#         font-weight: 600;
#         color: #00ffff;
#         margin-bottom: 0.5rem;
#         font-size: 1.1rem;
#         text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
#     }
    
#     .step-description {
#         color: #b0b0b0;
#         font-size: 0.9rem;
#     }
    
#     /* Section headers with neon effect */
#     h2 {
#         background: linear-gradient(90deg, #ff00ff, #00ffff, #ffff00);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         font-family: 'Orbitron', sans-serif;
#         text-transform: uppercase;
#         letter-spacing: 0.1em;
#         text-align: center;
#         margin: 2rem 0;
#     }
    
#     /* Markdown text color */
#     .stMarkdown {
#         color: #e0e0e0;
#     }
    
#     /* Glowing divider */
#     hr {
#         border: none;
#         height: 2px;
#         background: linear-gradient(90deg, transparent, #00ffff, #ff00ff, #00ffff, transparent);
#         box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
#         margin: 3rem 0;
#     }
    
#     /* Pulse animation for special elements */
#     @keyframes pulse {
#         0%, 100% {
#             opacity: 1;
#         }
#         50% {
#             opacity: 0.7;
#         }
#     }
    
#     /* Spinning animation for loading */
#     @keyframes spin {
#         from { transform: rotate(0deg); }
#         to { transform: rotate(360deg); }
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Neon Header section
# st.markdown("""
#     <div class="neon-header">
#         <div class="neon-title">🚀 AI PORTFOLIO GENERATOR 🚀</div>
#         <p class="neon-subtitle">Transform Your Resume Into A Stunning Digital Masterpiece</p>
#     </div>
# """, unsafe_allow_html=True)

# # Sidebar with information
# with st.sidebar:
#     st.markdown("### 📋 About")
#     st.markdown("""
#     This AI-powered tool automatically generates a complete, responsive portfolio website from your resume PDF.
#     """)
    
#     st.markdown("### ✨ Features")
#     st.markdown("""
#     - 🎨 Professional Design
#     - 📱 Fully Responsive
#     - ⚡ Fast Generation
#     - 💾 Downloadable Files
#     - 🔍 Live Preview
#     """)
    
#     st.markdown("### 🛠️ Technologies")
#     st.markdown("""
#     - HTML5
#     - CSS3
#     - JavaScript
#     - AI-Powered
#     """)
    
#     st.markdown("---")
#     st.markdown("### 💡 Tips")
#     st.markdown("""
#     - Use a well-formatted PDF resume
#     - Include all relevant information
#     - Ensure text is readable
#     """)

# # How it works section
# st.markdown("## 📊 How It Works")
# st.markdown("""
#     <div class="steps-container">
#         <div class="step-item">
#             <div class="step-number">1</div>
#             <div class="step-title">Upload Resume</div>
#             <div class="step-description">Upload your PDF resume file</div>
#         </div>
#         <div class="step-item">
#             <div class="step-number">2</div>
#             <div class="step-title">AI Processing</div>
#             <div class="step-description">AI analyzes and extracts information</div>
#         </div>
#         <div class="step-item">
#             <div class="step-number">3</div>
#             <div class="step-title">Generate Website</div>
#             <div class="step-description">Professional portfolio is created</div>
#         </div>
#         <div class="step-item">
#             <div class="step-number">4</div>
#             <div class="step-title">Download & Deploy</div>
#             <div class="step-description">Download files and go live</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # Feature cards section
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">⚡</div>
#             <div class="feature-title">Lightning Fast</div>
#             <div class="feature-description">Generate your portfolio in seconds with AI-powered processing</div>
#         </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">🎨</div>
#             <div class="feature-title">Beautiful Design</div>
#             <div class="feature-description">Professional, modern, and responsive design automatically applied</div>
#         </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#         <div class="feature-card">
#             <div class="feature-icon">📱</div>
#             <div class="feature-title">Fully Responsive</div>
#             <div class="feature-description">Perfect viewing experience on all devices and screen sizes</div>
#         </div>
#     """, unsafe_allow_html=True)

# # Main upload section
# st.markdown("## 📤 Upload Your Resume")
# st.markdown("""
#     <div class="info-box">
#         <div class="info-box-title">💡 Pro Tip</div>
#         Upload a PDF resume with clear sections (Education, Experience, Skills, etc.) for the best results.
#     </div>
# """, unsafe_allow_html=True)

# # Original code starts here - NOT MODIFIED
# file = st.file_uploader("Choose a file",type="pdf")

# if file is not None:
#     # Show file details
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown(f"""
#             <div class="info-box">
#                 <div class="info-box-title">📄 File Details</div>
#                 <strong>Name:</strong> {file.name}<br>
#                 <strong>Size:</strong> {file.size / 1024:.2f} KB
#             </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("""
#             <div class="info-box">
#                 <div class="info-box-title">✅ Status</div>
#                 File uploaded successfully! Ready to generate.
#             </div>
#         """, unsafe_allow_html=True)
    
#     pdfreader = PdfReader(file)

#     text = ""
#     for page in pdfreader.pages:
#         text += page.extract_text() or ""  # Avoid NoneType errors
    
    
#     text = text.strip()


#     if st.button("Generate Portfolio"):
#         with st.spinner('🎨 AI is crafting your portfolio...'):
#             message=["system","""You are an expert in web development, specializing in frontend technologies. 
#                     Your role is to generate clean, responsive, and professional html, css, and JavaScript code for creating a 
#                     complete frontend professional portfolio website based on the given user's text.

#                     Always produce the output in the exact format shown below:
                    
#                     --html--
#                     [html code]
#                     --html--
                    
#                     --css--
#                     [css code]
#                     --css--
                    
#                     --js--
#                     [js code]
#                     --js--
                    
#                     """]
#             message.append(("user",text))

#             model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#             response = model.invoke(message)

            
#             with open("file.txt", "w",encoding="utf-8") as file:
#                 file.write(response.content)

            

#             with open("index.html","w",encoding="utf-8") as file:
#                 file.write(response.content.split("--html--")[1])

#             with open("style.css","w",encoding="utf-8") as file:
#                 file.write(response.content.split("--css--")[1])

#             with open("script.js","w",encoding="utf-8") as file:
#                 file.write(response.content.split("--js--")[1])

#             with zipfile.ZipFile("portfolio.zip","w") as zip:
#                 zip.write("index.html")
#                 zip.write("style.css")
#                 zip.write("script.js")

#             st.markdown("""
#                 <div class="success-message">
#                     ✅ Portfolio Generated Successfully!
#                 </div>
#             """, unsafe_allow_html=True)

#             st.markdown('<div class="preview-container">', unsafe_allow_html=True)
#             st.markdown('<div class="preview-header">🖥️ Live Preview</div>', unsafe_allow_html=True)
            
#             with open("index.html", "r", encoding="utf-8") as f:
#                 html_content = f.read()
            
#             components.html(html_content, height=700, scrolling=True)
#             st.markdown('</div>', unsafe_allow_html=True)

#             # Download section with enhanced styling
#             st.markdown("## 💾 Download Your Portfolio")
#             col1, col2, col3 = st.columns([1,2,1])
#             with col2:
#                 st.download_button(
#                     "⬇️ Download Complete Portfolio Package",
#                     data=open("portfolio.zip","rb"),
#                     file_name="portfolio.zip",
#                     mime="application/zip"
#                 )
            
#             st.markdown("""
#                 <div class="info-box">
#                     <div class="info-box-title">📦 Package Contents</div>
#                     Your download includes:<br>
#                     • <strong>index.html</strong> - Main HTML file<br>
#                     • <strong>style.css</strong> - Styling file<br>
#                     • <strong>script.js</strong> - JavaScript file<br><br>
#                     Simply extract and open index.html in your browser!
#                 </div>
#             """, unsafe_allow_html=True)
            
#             st.balloons()  # Celebration effect!
            
#             st.write("success")
# # Original code ends here

# # Footer with neon styling
# st.markdown("---")
# st.markdown("""
#     <div style="text-align: center; padding: 2rem;">
#         <p style="color: #00ffff; font-size: 1.2rem; text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);">
#             Made with ❤️ using Streamlit and Google Gemini AI
#         </p>
#         <p style="color: #b0b0b0; font-size: 0.9rem; margin-top: 1rem;">
#             © 2024 AI Portfolio Generator • Transform Your Career Story Into A Digital Masterpiece
#         </p>
#     </div>
# """, unsafe_allow_html=True)





import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile
from PyPDF2 import PdfReader
import pandas as pd
from io import StringIO
from io import BytesIO
import streamlit.components.v1 as components


os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

# Advanced page configuration with custom theme
st.set_page_config(
    page_title="AI Portfolio Website Creation",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for advanced dark theme with neon styling
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap');
    
    /* Main container styling - Dark Theme with Deep Gradients */
    .main {
        background: linear-gradient(135deg, #000000 0%, #0a0e27 25%, #1a1a2e 50%, #16213e 75%, #0f3460 100%);
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
        min-height: 100vh;
    }
    
    /* App container with dark gradient */
    .appview-container {
        background: linear-gradient(180deg, #000000 0%, #0a0e27 20%, #1a1a2e 50%, #16213e 80%, #0f3460 100%);
    }
    
    /* Styledblock with gradient overlay */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0a0e27 25%, #1a1a2e 50%, #16213e 75%, #0f3460 100%);
        background-attachment: fixed;
    }
    
    /* Styledblock container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        background: linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(10, 14, 39, 0.2) 50%, transparent 100%);
    }
    
    /* Neon Title Header */
    .neon-header {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.9) 0%, rgba(10, 14, 39, 0.95) 30%, rgba(26, 26, 46, 0.95) 70%, rgba(15, 52, 96, 0.9) 100%);
        padding: 4rem 2rem;
        border-radius: 25px;
        text-align: center;
        box-shadow: 
            0 0 20px rgba(0, 255, 255, 0.3),
            0 0 40px rgba(255, 0, 255, 0.2),
            0 15px 50px rgba(0, 0, 0, 0.7),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
        border: 2px solid rgba(0, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .neon-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.1), transparent);
        animation: shine 3s infinite;
    }
    
    .neon-header::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(ellipse at top, rgba(0, 255, 255, 0.15), transparent 50%),
                    radial-gradient(ellipse at bottom, rgba(255, 0, 255, 0.15), transparent 50%);
        pointer-events: none;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 1rem;
        position: relative;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ff00);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: neonGlow 3s ease-in-out infinite, gradientShift 5s ease infinite;
        filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.8))
                drop-shadow(0 0 20px rgba(255, 0, 255, 0.6))
                drop-shadow(0 0 30px rgba(255, 255, 0, 0.4));
        z-index: 1;
    }
    
    @keyframes neonGlow {
        0%, 100% {
            filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.8))
                    drop-shadow(0 0 20px rgba(255, 0, 255, 0.6))
                    drop-shadow(0 0 30px rgba(255, 255, 0, 0.4));
        }
        50% {
            filter: drop-shadow(0 0 20px rgba(0, 255, 255, 1))
                    drop-shadow(0 0 40px rgba(255, 0, 255, 0.8))
                    drop-shadow(0 0 60px rgba(255, 255, 0, 0.6));
        }
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .neon-subtitle {
        color: #00ffff;
        font-size: 1.3rem;
        font-weight: 300;
        text-shadow: 
            0 0 10px rgba(0, 255, 255, 0.8),
            0 0 20px rgba(0, 255, 255, 0.5);
        letter-spacing: 0.05em;
        position: relative;
        z-index: 1;
    }
    
    /* Feature cards with dark theme and multiple gradient layers */
    .feature-card {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.95) 0%, rgba(10, 14, 39, 0.95) 30%, rgba(26, 26, 46, 0.95) 70%, rgba(22, 33, 62, 0.95) 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.7),
            0 0 15px rgba(0, 255, 255, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(0, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at top right, rgba(255, 0, 255, 0.15), transparent 50%),
                    radial-gradient(circle at bottom left, rgba(0, 255, 255, 0.15), transparent 50%);
        pointer-events: none;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.8),
            0 0 30px rgba(0, 255, 255, 0.3),
            0 0 40px rgba(255, 0, 255, 0.2);
        border: 1px solid rgba(0, 255, 255, 0.5);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.5));
        position: relative;
        z-index: 1;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        background: linear-gradient(90deg, #00ffff, #00ff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }
    
    .feature-description {
        color: #b0b0b0;
        font-size: 1rem;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    /* Upload section with neon glow and deep gradient */
    .upload-section {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.95) 0%, rgba(10, 14, 39, 0.9) 30%, rgba(26, 26, 46, 0.85) 70%, rgba(22, 33, 62, 0.8) 100%);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.7),
            0 0 20px rgba(255, 0, 255, 0.2),
            inset 0 1px 0 rgba(255, 0, 255, 0.1);
        margin: 2rem 0;
        border: 3px dashed rgba(255, 0, 255, 0.5);
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(8px);
    }
    
    .upload-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(255, 0, 255, 0.2), transparent 70%);
        pointer-events: none;
    }
    
    .upload-section:hover {
        border-color: rgba(0, 255, 255, 0.7);
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.8),
            0 0 40px rgba(0, 255, 255, 0.3);
    }
    
    /* Custom button styling with vibrant colors */
    .stButton>button {
        background: linear-gradient(135deg, #ff00ff 0%, #00ffff 50%, #ffff00 100%);
        color: #000;
        border: none;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        box-shadow: 
            0 5px 20px rgba(255, 0, 255, 0.4),
            0 0 20px rgba(0, 255, 255, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 8px 30px rgba(255, 0, 255, 0.6),
            0 0 40px rgba(0, 255, 255, 0.5);
        background: linear-gradient(135deg, #ffff00 0%, #00ffff 50%, #ff00ff 100%);
    }
    
    /* Download button with different neon color */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #00ff00 0%, #00ffff 50%, #0080ff 100%);
        color: #000;
        border: none;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        box-shadow: 
            0 5px 20px rgba(0, 255, 0, 0.4),
            0 0 20px rgba(0, 255, 255, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 8px 30px rgba(0, 255, 0, 0.6),
            0 0 40px rgba(0, 255, 255, 0.5);
    }
    
    /* Success message with neon green and dark gradient */
    .success-message {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.9) 0%, rgba(0, 50, 0, 0.8) 20%, rgba(0, 100, 0, 0.6) 50%, rgba(0, 255, 0, 0.2) 80%, rgba(0, 255, 255, 0.2) 100%);
        color: #00ff00;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 2rem 0;
        animation: fadeIn 0.5s ease-out;
        border: 2px solid rgba(0, 255, 0, 0.5);
        box-shadow: 
            0 0 20px rgba(0, 255, 0, 0.3),
            0 5px 20px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(0, 255, 0, 0.2);
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(5px);
    }
    
    .success-message::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(0, 255, 0, 0.25), transparent 70%);
        pointer-events: none;
    }
    
    /* Preview section with dark theme and multi-layer gradients */
    .preview-container {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.95) 0%, rgba(10, 14, 39, 0.95) 20%, rgba(26, 26, 46, 0.95) 50%, rgba(22, 33, 62, 0.95) 80%, rgba(15, 52, 96, 0.9) 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.7),
            0 0 20px rgba(255, 0, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        margin: 2rem 0;
        border: 1px solid rgba(0, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .preview-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(ellipse at top left, rgba(255, 0, 255, 0.12), transparent 50%),
                    radial-gradient(ellipse at bottom right, rgba(0, 255, 255, 0.12), transparent 50%);
        pointer-events: none;
    }
    
    .preview-header {
        font-size: 2rem;
        font-weight: 600;
        background: linear-gradient(90deg, #ff00ff, #00ffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        position: relative;
        z-index: 1;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* Sidebar styling with dark gradient */
    .css-1d391kg {
        background: linear-gradient(180deg, #000000 0%, #0a0e27 20%, #1a1a2e 40%, #16213e 60%, #0f3460 80%, #1a1a2e 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #000000 0%, #0a0e27 20%, #1a1a2e 40%, #16213e 60%, #0f3460 80%, #1a1a2e 100%);
        border-right: 1px solid rgba(0, 255, 255, 0.2);
        box-shadow: 5px 0 20px rgba(0, 0, 0, 0.7);
        position: relative;
    }
    
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(ellipse at top, rgba(0, 255, 255, 0.08), transparent 50%),
                    radial-gradient(ellipse at bottom, rgba(255, 0, 255, 0.08), transparent 50%);
        pointer-events: none;
    }
    
    [data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }
    
    /* File uploader styling with gradient */
    .stFileUploader {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.7) 0%, rgba(10, 14, 39, 0.6) 30%, rgba(26, 26, 46, 0.7) 70%, rgba(255, 0, 255, 0.15) 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid rgba(255, 0, 255, 0.3);
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.5),
            0 0 15px rgba(255, 0, 255, 0.2),
            inset 0 1px 0 rgba(255, 0, 255, 0.1);
        backdrop-filter: blur(5px);
    }
    
    /* Progress bar styling with neon */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #00ff00, #00ffff, #ff00ff);
    }
    
    /* Info boxes with dark theme and rich gradients */
    .info-box {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.8) 0%, rgba(10, 14, 39, 0.85) 30%, rgba(22, 33, 62, 0.8) 70%, rgba(15, 52, 96, 0.7) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #00ffff;
        margin: 1rem 0;
        box-shadow: 
            0 5px 15px rgba(0, 0, 0, 0.5),
            0 0 10px rgba(0, 255, 255, 0.2),
            inset 0 1px 0 rgba(0, 255, 255, 0.1);
        color: #e0e0e0;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(5px);
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at left, rgba(0, 255, 255, 0.15), transparent 60%),
                    radial-gradient(circle at right, rgba(255, 0, 255, 0.1), transparent 60%);
        pointer-events: none;
    }
    
    .info-box-title {
        font-weight: 600;
        background: linear-gradient(90deg, #00ffff, #00ff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
        position: relative;
        z-index: 1;
    }
    
    /* Steps container */
    .steps-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        flex-wrap: wrap;
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.4) 0%, rgba(10, 14, 39, 0.3) 50%, rgba(26, 26, 46, 0.2) 100%);
        padding: 2rem;
        border-radius: 20px;
    }
    
    .step-item {
        text-align: center;
        flex: 1;
        min-width: 200px;
        padding: 1rem;
    }
    
    .step-number {
        background: linear-gradient(135deg, #ff00ff 0%, #00ffff 100%);
        color: #000;
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 900;
        margin-bottom: 1rem;
        box-shadow: 
            0 5px 20px rgba(255, 0, 255, 0.4),
            0 0 20px rgba(0, 255, 255, 0.3);
        font-family: 'Orbitron', sans-serif;
    }
    
    .step-title {
        font-weight: 600;
        color: #00ffff;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
        text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
    }
    
    .step-description {
        color: #b0b0b0;
        font-size: 0.9rem;
    }
    
    /* Section headers with neon effect */
    h2 {
        background: linear-gradient(90deg, #ff00ff, #00ffff, #ffff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* Markdown text color */
    .stMarkdown {
        color: #e0e0e0;
    }
    
    /* Glowing divider with gradient background */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent, #00ffff, #ff00ff, #ffff00, #00ffff, transparent);
        box-shadow: 
            0 0 10px rgba(0, 255, 255, 0.5),
            0 0 20px rgba(255, 0, 255, 0.3);
        margin: 3rem 0;
        position: relative;
    }
    
    hr::before {
        content: '';
        position: absolute;
        top: -10px;
        left: 0;
        right: 0;
        height: 20px;
        background: linear-gradient(180deg, rgba(0, 255, 255, 0.15), transparent);
        filter: blur(10px);
    }
    
    /* Column backgrounds with subtle gradients */
    [data-testid="column"] {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.4) 0%, rgba(10, 14, 39, 0.3) 50%, rgba(26, 26, 46, 0.2) 100%);
        border-radius: 15px;
        padding: 1rem;
    }
    
    /* Pulse animation for special elements */
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    /* Spinning animation for loading */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
""", unsafe_allow_html=True)

# Neon Header section
st.markdown("""
    <div class="neon-header">
        <div class="neon-title">🚀 AI PORTFOLIO GENERATOR 🚀</div>
        <p class="neon-subtitle">Transform Your Resume Into A Stunning Digital Masterpiece</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("### 📋 About")
    st.markdown("""
    This AI-powered tool automatically generates a complete, responsive portfolio website from your resume PDF.
    """)
    
    st.markdown("### ✨ Features")
    st.markdown("""
    - 🎨 Professional Design
    - 📱 Fully Responsive
    - ⚡ Fast Generation
    - 💾 Downloadable Files
    - 🔍 Live Preview
    """)
    
    st.markdown("### 🛠️ Technologies")
    st.markdown("""
    - HTML5
    - CSS3
    - JavaScript
    - AI-Powered
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Use a well-formatted PDF resume
    - Include all relevant information
    - Ensure text is readable
    """)

# How it works section
st.markdown("## 📊 How It Works")
st.markdown("""
    <div class="steps-container">
        <div class="step-item">
            <div class="step-number">1</div>
            <div class="step-title">Upload Resume</div>
            <div class="step-description">Upload your PDF resume file</div>
        </div>
        <div class="step-item">
            <div class="step-number">2</div>
            <div class="step-title">AI Processing</div>
            <div class="step-description">AI analyzes and extracts information</div>
        </div>
        <div class="step-item">
            <div class="step-number">3</div>
            <div class="step-title">Generate Website</div>
            <div class="step-description">Professional portfolio is created</div>
        </div>
        <div class="step-item">
            <div class="step-number">4</div>
            <div class="step-title">Download & Deploy</div>
            <div class="step-description">Download files and go live</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Feature cards section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-description">Generate your portfolio in seconds with AI-powered processing</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Beautiful Design</div>
            <div class="feature-description">Professional, modern, and responsive design automatically applied</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📱</div>
            <div class="feature-title">Fully Responsive</div>
            <div class="feature-description">Perfect viewing experience on all devices and screen sizes</div>
        </div>
    """, unsafe_allow_html=True)

# Main upload section
st.markdown("## 📤 Upload Your Resume")
st.markdown("""
    <div class="info-box">
        <div class="info-box-title">💡 Pro Tip</div>
        Upload a PDF resume with clear sections (Education, Experience, Skills, etc.) for the best results.
    </div>
""", unsafe_allow_html=True)

# Original code starts here - NOT MODIFIED
file = st.file_uploader("Choose a file",type="pdf")

if file is not None:
    # Show file details
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="info-box">
                <div class="info-box-title">📄 File Details</div>
                <strong>Name:</strong> {file.name}<br>
                <strong>Size:</strong> {file.size / 1024:.2f} KB
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="info-box">
                <div class="info-box-title">✅ Status</div>
                File uploaded successfully! Ready to generate.
            </div>
        """, unsafe_allow_html=True)
    
    pdfreader = PdfReader(file)

    text = ""
    for page in pdfreader.pages:
        text += page.extract_text() or ""  # Avoid NoneType errors
    
    
    text = text.strip()


    if st.button("Generate Portfolio"):
        with st.spinner('🎨 AI is crafting your portfolio...'):
            message=["system","""You are an expert in web development, specializing in frontend technologies. 
                    Your role is to generate clean, responsive, and professional html, css, and JavaScript code for creating a 
                    complete frontend professional portfolio website based on the given user's text.

                    Always produce the output in the exact format shown below:
                    
                    --html--
                    [html code]
                    --html--
                    
                    --css--
                    [css code]
                    --css--
                    
                    --js--
                    [js code]
                    --js--
                    
                    """]
            message.append(("user",text))

            model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

            response = model.invoke(message)

            
            with open("file.txt", "w",encoding="utf-8") as file:
                file.write(response.content)

            

            with open("index.html","w",encoding="utf-8") as file:
                file.write(response.content.split("--html--")[1])

            with open("style.css","w",encoding="utf-8") as file:
                file.write(response.content.split("--css--")[1])

            with open("script.js","w",encoding="utf-8") as file:
                file.write(response.content.split("--js--")[1])

            with zipfile.ZipFile("portfolio.zip","w") as zip:
                zip.write("index.html")
                zip.write("style.css")
                zip.write("script.js")

            st.markdown("""
                <div class="success-message">
                    ✅ Portfolio Generated Successfully!
                </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="preview-container">', unsafe_allow_html=True)
            st.markdown('<div class="preview-header">🖥️ Live Preview</div>', unsafe_allow_html=True)
            
            with open("index.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            
            components.html(html_content, height=700, scrolling=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Download section with enhanced styling
            st.markdown("## 💾 Download Your Portfolio")
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.download_button(
                    "⬇️ Download Complete Portfolio Package",
                    data=open("portfolio.zip","rb"),
                    file_name="portfolio.zip",
                    mime="application/zip"
                )
            
            st.markdown("""
                <div class="info-box">
                    <div class="info-box-title">📦 Package Contents</div>
                    Your download includes:<br>
                    • <strong>index.html</strong> - Main HTML file<br>
                    • <strong>style.css</strong> - Styling file<br>
                    • <strong>script.js</strong> - JavaScript file<br><br>
                    Simply extract and open index.html in your browser!
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()  # Celebration effect!
            
            st.write("success")
# Original code ends here

# Footer with neon styling
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <p style="color: #00ffff; font-size: 1.2rem; text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);">
            Made with ❤️ using Streamlit and Google Gemini AI
        </p>
        <p style="color: #b0b0b0; font-size: 0.9rem; margin-top: 1rem;">
            © 2024 AI Portfolio Generator • Transform Your Career Story Into A Digital Masterpiece
        </p>
    </div>
""", unsafe_allow_html=True)