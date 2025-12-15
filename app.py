import streamlit as st

st.set_page_config(page_title="Zhou Zhou | Portfolio", page_icon="🧠", layout="wide")

st.sidebar.title("Zhou Zhou")
st.sidebar.markdown("**Data Scientist**")
st.sidebar.markdown("GMU – M.S. in Data Analytics Engineering")
page = st.sidebar.radio("Navigate", ["🏠 Home", "🧠 AI Resume Optimizer (Demo)", "📫 Contact"])

def home():
    st.title("👋 Hi, I'm Zhou Zhou")
    st.subheader("Data Scientist | AI, NLP & Predictive Analytics")
    st.write(
        """
I’m a Data Scientist and Master’s student at George Mason University. 
My focus is **AI, NLP, and machine learning**, and I build applied projects that turn data into useful products.
        """
    )
    st.markdown("### ⭐ Featured Project: AI Resume Optimizer")
    st.write(
        """
An AI-powered tool that analyzes how well a resume matches a job description using NLP & semantic similarity,
then generates optimization suggestions with LLMs.
        """
    )
    st.info("Use the left sidebar to open **AI Resume Optimizer (Demo)**.")

def demo():
    st.title("🧠 AI Resume Optimizer — Demo UI")
    st.write("Upload a resume and paste a job description to see a simulated analysis and suggestions.")

    col1, col2 = st.columns([1.1, 1.3])

    with col1:
        st.subheader("Inputs")
        st.file_uploader("Upload resume (PDF/DOC/DOCX)", type=["pdf", "doc", "docx"])
        jd = st.text_area("Paste job description", height=220)
        analyze = st.button("🔍 Analyze Match")
        suggest = st.button("✨ Generate Suggestions")

    with col2:
        st.subheader("Outputs")
        if analyze and jd:
            st.metric("Match Score (demo)", "74%", "+12% (simulated)")
            st.write("- ✅ Python\n- ✅ SQL\n- ⚠️ NLP/Transformers (low emphasis)\n- ⚠️ Cloud (briefly mentioned)")
            st.write("**Suggested focus:** add NLP/embeddings bullets, highlight ML pipeline + deployment.")
        elif analyze and not jd:
            st.warning("Please paste a job description first.")

        if suggest and jd:
            st.write("**Optimized Summary (example):**")
            st.write("Data Scientist with strong Python/SQL skills and hands-on NLP + ML project experience.")
            st.write("**Optimized Bullets (example):**")
            st.write("- Built an AI resume optimizer using NLP + semantic matching.\n- Developed ML pipelines and dashboards to support decisions.")
        elif suggest and not jd:
            st.warning("Please paste a job description first.")

def contact():
    st.title("📫 Contact")
    st.write("**Email:** zoezhou314@gmail.com")
    st.write("**LinkedIn:** https://linkedin.com/in/your-link")
    st.write("**GitHub:** https://github.com/your-github")
    st.write("**Work Authorization:** U.S. Permanent Resident (Green Card)")

if page == "🏠 Home":
    home()
elif page == "🧠 AI Resume Optimizer (Demo)":
    demo()
else:
    contact()