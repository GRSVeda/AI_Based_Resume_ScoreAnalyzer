import streamlit as st
import PyPDF2
import re

# Page Settings
st.set_page_config(page_title="Rajeswari's AI Resume Screener", page_icon="🎯", layout="centered")

# Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; height: 3em; font-size: 1.2em; }
    .match-score { font-size: 60px; font-weight: bold; color: #28a745; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 AI-Powered Resume Screener")
st.markdown("Created by **Gadepalli Rajeswari Srikruthi Veda**")
st.divider()

def get_text(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([p.extract_text() for p in reader.pages]).lower()

# UI Layout
jd = st.text_area("1. Paste Job Description (JD)", height=200, placeholder="Example: Need a React, Node.js and MongoDB expert...")
file = st.file_uploader("2. Upload Resume (PDF Only)", type="pdf")

if st.button("Analyze Profile 🚀"):
    if jd and file:
        with st.spinner("Comparing skills..."):
            text = get_text(file)
            # Skills database based on your actual profile 
            skills = ['react', 'node.js', 'express', 'mongodb', 'javascript', 'html', 'css', 'python', 'java', 'sql', 'git', 'github']
            
            found = [s for s in skills if s in text]
            required = [s for s in skills if s in jd.lower()]
            
            if required:
                matches = set(found) & set(required)
                missing = set(required) - set(found)
                score = round((len(matches) / len(required)) * 100, 2)
                
                st.markdown(f"<div class='match-score'>{score}% Match</div>", unsafe_allow_html=True)
                
                c1, c2 = st.columns(2)
                with c1:
                    st.success(f"✅ **Matched Skills ({len(matches)})**")
                    st.write(", ".join(matches))
                with c2:
                    st.warning(f"⚠️ **Missing Skills ({len(missing)})**")
                    st.write(", ".join(missing) if missing else "None")
                
                if score > 75:
                    st.balloons()
                    st.info("Perfect Match! This candidate is highly suitable for the role.")
            else:
                st.error("Please add technical skills (like React, Java, Git) to the JD for comparison.")
    else:
        st.error("Please provide both the Job Description and the Resume file.")
