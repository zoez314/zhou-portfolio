import streamlit as st
from pathlib import Path

# ----------------- Config -----------------
st.set_page_config(page_title="Zhou Zhou | Portfolio", page_icon="🧠", layout="wide")

ASSETS_DIR = Path(__file__).parent / "assets"


def img_path(name: str) -> Path:
    return ASSETS_DIR / name


def render_project_card(
    title: str,
    subtitle: str,
    description: str,
    img_file: str,
    target_page: str,
    disabled: bool = False,
):
    """Render a project card (image + text + button)"""
    with st.container(border=True):
        p = img_path(img_file)

        if p.exists():
            st.image(str(p), width="stretch")
        else:
            st.markdown(
                """
                <div style="
                    height:160px; border-radius:14px;
                    background: linear-gradient(135deg, rgba(56,189,248,0.35), rgba(167,139,250,0.25));
                    border: 1px solid rgba(255,255,255,0.15);
                    display:flex; align-items:center; justify-content:center;
                    font-size:44px;
                ">🧩</div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(f"### {title}")
        st.caption(subtitle)
        st.write(description)

        if disabled:
            st.button("Coming soon", disabled=True, width="stretch")
        else:
            if st.button("Open project", key=f"open_{target_page}", width="stretch"):
                st.session_state["page"] = target_page
                st.rerun()


# ----------------- Sidebar Navigation -----------------
st.sidebar.title("Zhou Zhou")
st.sidebar.markdown("**Data Scientist**")
st.sidebar.markdown("GMU – M.S. in Data Analytics Engineering")

# Persist navigation state
if "page" not in st.session_state:
    st.session_state["page"] = "🏠 Home"

PAGES = [
    "🏠 Home",
    "🧠 AI Resume Optimizer",
    "📍 Public Safety → Housing",
    "📊 Customer Value & Churn Risk",
    "🚧 Coming Soon",
    "📫 Contact",
]

page = st.sidebar.radio("Navigate", PAGES, index=PAGES.index(st.session_state["page"]))
st.session_state["page"] = page

st.sidebar.markdown("---")
st.sidebar.markdown("**Work Authorization:** U.S. Permanent Resident (Green Card)")
st.sidebar.markdown("")


# ----------------- Pages -----------------
def home():
    st.title("👋 Hi, I'm Zhou Zhou")
    st.subheader("Data Scientist | AI, NLP & Applied Analytics")
    st.write(
        """
I’m a Master’s student at George Mason University focused on **AI, NLP, and machine learning**.
I build applied, end-to-end projects that turn data into useful products and dashboards.
        """
    )

    st.markdown("## ⭐ Featured Projects")
    st.caption("Click **Open project** to view the project page. (Left sidebar also works.)")

    # Row 1: 3 cards
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        render_project_card(
            title="AI Resume Optimizer (Demo)",
            subtitle="NLP • Semantic Matching • LLM-style Suggestions",
            description=(
                "A resume–job description matcher that highlights skill gaps and generates improvement suggestions. "
                "Designed as a product-style UI demo for job search workflows."
            ),
            img_file="resume_optimizer.jpg",
            target_page="🧠 AI Resume Optimizer",
        )

    with col2:
        render_project_card(
            title="Public Safety → Housing Impact",
            subtitle="Event Study • Difference-in-Differences • Streamlit + Plotly",
            description=(
                "Interactive dashboard analyzing housing price trends before/after public safety incidents, "
                "with treatment vs control comparison and DID effect estimation."
            ),
            img_file="public_safety.jpg",
            target_page="📍 Public Safety → Housing",
        )

    with col3:
        render_project_card(
            title="Customer Value & Churn Risk Intelligence",
            subtitle="ML Pipeline • Explainable Drivers • Streamlit App",
            description=(
                "A production-style app that predicts churn risk, highlights top drivers, and generates a practical "
                "customer playbook for retention actions."
            ),
            img_file="Customer_Risk.jpg",
            target_page="📊 Customer Value & Churn Risk",
        )

    # Optional: second row
    st.markdown("")
    colA, colB, colC = st.columns(3, gap="large")
    with colA:
        render_project_card(
            title="Project #4 (Coming Soon)",
            subtitle="Next: a more advanced AI/DS project",
            description=(
                "I’m currently building the next portfolio project with deeper modeling + stronger product polish. "
                "Stay tuned."
            ),
            img_file="coming_soon.jpg",
            target_page="🚧 Coming Soon",
            disabled=True,
        )
    with colB:
        st.empty()
    with colC:
        st.empty()

    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.write("- **LinkedIn:** (https://www.linkedin.com/in/zoe-zhou-a327bb319/)")
    st.write("- **GitHub:** (https://github.com/zoez314)")
    st.write("- **Email:** zoezhou314@gmail.com")


def resume_optimizer():
    st.title("🧠 AI Resume Optimizer — Demo UI")
    st.caption("NLP • Semantic similarity • Product-style UI demo")

    st.write(
        """
This demo shows a simplified workflow: upload a resume, paste a job description,
and view a simulated match score + suggestions.
        """
    )

    col1, col2 = st.columns([1.1, 1.3], gap="large")

    with col1:
        st.subheader("Inputs")
        st.file_uploader("Upload resume (PDF/DOC/DOCX)", type=["pdf", "doc", "docx"])
        jd = st.text_area("Paste job description", height=220)
        analyze = st.button("🔍 Analyze Match", width="stretch")
        suggest = st.button("✨ Generate Suggestions", width="stretch")

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
            st.write(
                "- Built an AI resume optimizer using NLP + semantic matching.\n"
                "- Developed ML pipelines and dashboards to support decisions."
            )
        elif suggest and not jd:
            st.warning("Please paste a job description first.")


def public_safety():
    st.title("📍 Public Safety Events → Housing Market Impact")
    st.caption("Event Study • Difference-in-Differences (DID) • Streamlit Dashboard")

    st.write(
        """
This project explores how major public safety incidents may correlate with nearby housing price movements,
using a treatment vs control comparison and a light DID estimator.
        """
    )

    st.markdown("### 🧰 Tech Stack")
    st.write(
        """
- Python, Pandas, NumPy  
- Streamlit, Plotly  
- Event Study Windowing, Difference-in-Differences (DID)  
- Data Cleaning + Time-series Visualization  
        """
    )

    st.markdown("### 🔗 Links")
    st.write("- Live app: (https://public-safety-housing-impact-and3pu5nenedqo58zuapoa.streamlit.app/)")
    st.write("- GitHub repo: (https://github.com/zoez314/public-safety-housing-impact)")


def customer_value_churn_risk():
    st.title("📊 Customer Value & Churn Risk Intelligence")
    st.caption("ML Pipeline • Explainable Drivers • Streamlit App")

    hero = img_path("Customer_Risk.jpg")
    if hero.exists():
        st.image(str(hero), width="stretch")

    st.write(
        """
This app predicts customer churn risk and turns the prediction into a **decision-ready playbook**:
- **Risk prediction** (probability)
- **Top drivers** (explainable, coefficient-based for Logistic Regression)
- **Recommended actions** (retention playbook)
        """
    )

    st.markdown("### 🧰 Tech Stack")
    st.write(
        """
- Python, Pandas, NumPy  
- Scikit-learn Pipeline (preprocessing + model)  
- Streamlit UI  
- Model persistence with `joblib`  
        """
    )

    st.markdown("### ✅ Live App")
    st.link_button(
        "Open Live App",
        "https://customer-value-and-churn-risk-intelligence.streamlit.app/",
        width="stretch",
    )

    st.markdown("### 🔗 GitHub")
    st.link_button(
        "Open GitHub Repo",
        "https://github.com/zoez314/customer-value-and-churn-risk-intelligence/tree/main",
        width="stretch",
    )

    st.markdown("---")
    st.info(
        "Note: The deployed environment may use newer sklearn versions. "
        "If you update the model pipeline, re-save the `joblib` and keep versions aligned."
    )


def coming_soon():
    st.title("🚧 Project — Coming Soon")
    st.write(
        """
I’m actively building the next project with a more advanced model + product polish.
This section will be updated soon.
        """
    )
    st.markdown("### What’s planned")
    st.write("- Stronger ML/AI depth (modeling + evaluation)")
    st.write("- Cleaner storytelling (problem → method → results → impact)")
    st.write("- Production-style UI / reproducible pipeline")


def contact():
    st.title("📫 Contact")
    st.write("**Email:** zoezhou314@gmail.com")
    st.write("**LinkedIn:** https://www.linkedin.com/in/zoe-zhou-a327bb319/")
    st.write("**GitHub:** https://github.com/zoez314")
    st.write("**Work Authorization:** U.S. Permanent Resident (Green Card)")

    st.markdown("---")
    st.subheader("📄 Resume")

    resume_path = img_path("Zhou_Zhou_Resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            st.download_button(
                label="Download Resume (PDF)",
                data=f,
                file_name="Zhou_Zhou_Resume.pdf",
                mime="application/pdf",
                width="stretch",
            )
    else:
        st.warning(
            "Resume file not found. Put `Zhou_Zhou_Resume.pdf` into the `assets/` folder, then redeploy."
        )


# ----------------- Router -----------------
if page == "🏠 Home":
    home()
elif page == "🧠 AI Resume Optimizer":
    resume_optimizer()
elif page == "📍 Public Safety → Housing":
    public_safety()
elif page == "📊 Customer Value & Churn Risk":
    customer_value_churn_risk()
elif page == "🚧 Coming Soon":
    coming_soon()
else:
    contact()