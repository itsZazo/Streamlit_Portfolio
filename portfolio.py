import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Aitzaz Ahmed - AI Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with modern design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #0f1419 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1a1f2e;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #00d4ff, #0099cc);
        border-radius: 4px;
    }
    
    /* Navigation Bar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(15, 20, 25, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(0, 212, 255, 0.2);
        padding: 1rem 2rem;
    }
    
    .nav-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .nav-link {
        color: #ffffff;
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .nav-link:hover {
        color: #00d4ff;
        background: rgba(0, 212, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-link:hover::before {
        left: 100%;
    }
    
    /* Hero Section */
    .hero-container {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-top: 80px;
    }
    
    .hero-content {
        z-index: 2;
        position: relative;
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d4ff 0%, #ffffff 50%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: glow 2s ease-in-out infinite alternate;
        line-height: 1.1;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.3)); }
        to { filter: drop-shadow(0 0 30px rgba(0, 212, 255, 0.6)); }
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #b8bcc8;
        margin-bottom: 2rem;
        font-weight: 300;
        opacity: 0;
        animation: fadeInUp 1s ease 0.5s forwards;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .hero-cta {
        display: inline-flex;
        gap: 1rem;
        margin-top: 2rem;
        opacity: 0;
        animation: fadeInUp 1s ease 1s forwards;
    }
    
    .cta-button {
        padding: 1rem 2rem;
        border: none;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        font-size: 1rem;
    }
    
    .cta-primary {
        background: linear-gradient(135deg, #9966ff, #0099cc);
        color: #f0f8ff;    
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    }
    
    .cta-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.5);
    }
    
    .cta-secondary {
        background: transparent;
        color: #00d4ff;
        border: 2px solid #00d4ff;
    }
    
    .cta-secondary:hover {
        background: #00d4ff;
        color: #0f1419;
        transform: translateY(-3px);
    }
    
    /* Section Styles */
    .section {
        padding: 5rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
        background: linear-gradient(135deg, #ffffff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #0099cc);
        border-radius: 2px;
    }
    
    /* About Section */
    .about-content {
        background: rgba(26, 31, 46, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .about-content::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0, 212, 255, 0.1), transparent);
        animation: rotate 10s linear infinite;
        pointer-events: none;
    }
    
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #e1e5e9;
        position: relative;
        z-index: 2;
        margin-bottom: 2rem;
    }
    
    .contact-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 2;
    }
    
    .contact-link {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.8rem 1.5rem;
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 15px;
        color: #00d4ff;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .contact-link:hover {
        background: rgba(0, 212, 255, 0.2);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.2);
    }
    
    /* Project Cards */
    .project-card {
        background: rgba(26, 31, 46, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        cursor: pointer;
        margin-bottom: 2rem;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        border-color: rgba(0, 212, 255, 0.5);
        box-shadow: 0 20px 50px rgba(0, 212, 255, 0.1);
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #0099cc, #00d4ff);
        background-size: 200% 100%;
        animation: shimmer 2s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .project-title {
        font-size: 2.5rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .project-description {
        color: #b8bcc8;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        font-size: 1.2rem;
    }
    
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .tech-tag {
        padding: 0.4rem 0.8rem;
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 20px;
        color: #00d4ff;
        font-size: 0.8rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .tech-tag:hover {
        background: rgba(0, 212, 255, 0.2);
        transform: scale(1.05);
    }
    
    /* Image Gallery */
    .image-gallery {
        display: flex;
        gap: 1rem;
        overflow-x: auto;
        padding: 1rem 0;
    }
    
    .gallery-image {
        min-width: 200px;
        height: 120px;
        border-radius: 10px;
        object-fit: cover;
        border: 2px solid rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .gallery-image:hover {
        border-color: #00d4ff;
        transform: scale(1.05);
    }
    
    /* Floating Animation */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
        }
        
        .section {
            padding: 3rem 1rem;
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
        }
        
        .nav-links {
            flex-direction: column;
            gap: 1rem;
        }
        
        .contact-links {
            flex-direction: column;
            align-items: center;
        }
    }
    
    /* Skills Animation */
    .skills-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .skill-category {
        background: rgba(26, 31, 46, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 212, 255, 0.5);
    }
    
    .skill-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .skill-title {
        font-size: 1.9rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .skill-list {
        color: #b8bcc8;
        line-height: 1.6;
        font-size: 1.1rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div class="nav-container">
    <div class="nav-links">
        <a href="#home" class="nav-link">Home</a>
        <a href="#about" class="nav-link">About</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#contact" class="nav-link">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Helper function to load and encode images
def load_image(image_path):
    """Load and return image. Handle both local paths and PIL Image objects."""
    try:
        if isinstance(image_path, str):
            # Check if it's a valid file path that exists
            import os
            if os.path.exists(image_path):
                return Image.open(image_path)
            else:
                # Return None if path doesn't exist
                return None
        return image_path
    except Exception as e:
        st.warning(f"Could not load image: {image_path}")
        return None

# Enhanced Portfolio Data Structure
PORTFOLIO_DATA = {
    "personal_info": {
        "name": "AITZAZ AHMED",
        "title": "AI ENGINEER & DEVELOPER",
        "email": "official.aitzaz@gmail.com",
        "linkedin": "https://linkedin.com/in/aitzaz-ahmed-akazazo",
        "github": "https://github.com/itsZazo",
        "bio": """Results-driven AI Developer with expertise in machine learning, deep learning (ANNs, CNNs, RNNs), 
        and Generative AI. Skilled in model optimization, feature engineering, and hyperparameter tuning to 
        improve predictive accuracy. Experienced in building GenAI pipelines with LangChain, LLMs, and vector 
        databases for advanced retrieval-augmented generation (RAG) applications. Strong collaborative and 
        problem-solving skills with full-cycle AI development experience."""
    },
    
    "skills": {
        "AI & Machine Learning": {
            "icon": "🤖",
            "skills": ["Deep Learning", "Neural Networks", "Computer Vision", "NLP", "Model Optimization"]
        },
        "Generative AI": {
            "icon": "✨",
            "skills": ["LangChain", "LLMs", "RAG Systems", "Vector Databases", "Prompt Engineering"]
        },
        "Programming": {
            "icon": "💻",
            "skills": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "OpenCV"]
        },
        "Deployment": {
            "icon": "☁️",
            "skills": ["Flask", "Streamlit", "API Development"]
        }
    },
    
    "projects": [
        {
            "title": "🎓 AI-TUTOR Using GenAI",
            "description": """Designed and developed an intelligent AI Agent to assist users in studying and understanding concepts 
            across diverse fields including Physics, Chemistry, Mathematics, and History. Built to be universally 
            accessible — even for 1st-grade students — the agent leverages adaptive learning strategies, constant 
            student feedback, and real-world analogies to simplify complex topics into easily digestible lessons.The AI Tutor supports voice commands for natural interaction and accepts PDFs and text files as input, 
            allowing users to upload study materials. It can automatically read and extract information from these 
            files to explain concepts, summarize key points, and generate custom quizzes for self-assessment.""",
            "technologies": ["LangChain", "LLM", "PineCone", "Groq API", "AWS", "Voice Recognition"],
            "images": [
                r"images/ai_tutor_1.png",
                r"images/ai_tutor_2.png"
            ],
            "demo_link": "#",
            "github_link": "#"
        },
        
        {
            "title": "🎨 AI Image Generation Agent (Stable Diffusion & Gemini)",
            "description": """"An AI-powered Agent that generates high-resolution images from natural language prompts using 
            Stable Diffusion. Users can enter creative prompts and receive custom artwork or photorealistic outputs in seconds. 
            Integrated user-friendly UI with Flask, allowing seamless image generation, download, and prompt editing. 
            This Agent uses MCP (Model Context Protocol) based Tools, those tools help the Agent generate images.
            Enabled use-cases in content creation, visual storytelling, and concept art prototyping.""",
            "technologies": ["LangGraph", "Stable Diffusion", "Gemini", "AI Agent", "MCP", "Flask", "LLM"],
            "images": [
                 r"images/chick.jpeg",
                 r"images/chick_2.jpeg",
            ],
            "demo_link": "#",
            "github_link": "#"
        },
        
         {
            "title": "🐥 Chick Vaccine Prediction System",
            "description": """A robust machine learning model to predict G Mean, mortality rate, and production outcomes in poultry 
            based on complex vaccine combinations and disease profiles. Processed high-dimensional datasets containing 
            vaccine sequences administered to chicks exposed to diseases such as IBDV, IBV, and NDV.Applied advanced feature engineering, dimensionality reduction (PCA), and supervised learning algorithms 
            to model the nonlinear interactions between vaccines and biological responses. Achieved significant 
            improvements in prediction accuracy, enabling cost reduction and optimization of vaccine protocols.""",
            "technologies": ["Python", "NumPy", "Pandas", "Scikit-learn", "Flask", "PCA", "MLflow"],
            "images": [
                 r"images/chick.jpeg",
                 r"images/chick_2.jpeg",
            ],
            "demo_link": "#",
            "github_link": "#"
        },
        
        {
            "title": "🚦 Road Sign Detection & OCR",
            "description": """Developed a high-performance computer vision pipeline for real-time road sign detection and recognition. 
            Utilized an advanced YOLOv11 object detection model, achieving 98% detection accuracy in a highly 
            unbalanced dataset for classifying and localizing road signs across diverse driving environments.Following object detection, integrated an Optical Character Recognition (OCR) module to extract and 
            digitize textual information from detected signs with 95-99% text extraction accuracy. Designed for 
            end-to-end automation, enabling deployment in mobile or embedded applications for real-time driver assistance.""",
            "technologies": ["CNN", "YOLOv11", "Transfer Learning", "OCR", "OpenCV", "Data Augmentation", "Computer Vision"],
            "images": [
                r"images/ocr_1.png",
                r"images/ocr_2.png",
                r"images/ocr_3.png"
            ],
            "demo_link": "#",
            "github_link": "#"
        },

        {
            "title": "📝 AI Quiz Generator",
            "description": """Engineered an automated quiz generation system leveraging LangChain framework and large language models. 
            Enabled ingestion of user-uploaded documents (PDF, TXT) via document loaders with embedded chunking for 
            optimized context extraction.Implemented semantic search pipelines using vector embeddings (Pinecone, FAISS) to retrieve topic-specific 
            sections based on user-specified queries. Applied advanced prompt engineering and output parsing to generate 
            structured, contextually relevant multiple-choice questions for domain-specific self-assessment.""",
            "technologies": ["LangChain", "Prompt Engineering", "PineCone", "Groq API", "AWS", "Vectorization", "Ollama"],
            "images": [
                r"images/mcq_1.png",
                r"images/mcq_2.png"
            ],
            "demo_link": "#",
            "github_link": "#"
        },
    ]
}

def display_hero():
    """Display enhanced hero section"""
    st.markdown("""
    <div class="hero-container" id="home">
        <div class="hero-content">
            <h1 class="hero-title floating">AITZAZ AHMED</h1>
            <p class="hero-subtitle">AI Engineer & Developer | Building the Future with Intelligent Systems</p>
            <div class="hero-cta">
                <a href="#projects" class="cta-button cta-primary">View My Work</a>
                <a href="#contact" class="cta-button cta-secondary">Get In Touch</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_about():
    """Display enhanced about section"""
    st.markdown('<div class="section" id="about">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="about-content">
        <div class="about-text">
            🚀 {PORTFOLIO_DATA["personal_info"]["bio"]}
        </div>
        <div class="contact-links">
            <a href="mailto:{PORTFOLIO_DATA['personal_info']['email']}" class="contact-link">
                📧 Email
            </a>
            <a href="{PORTFOLIO_DATA['personal_info']['linkedin']}" class="contact-link" target="_blank">
                💼 LinkedIn
            </a>
            <a href="{PORTFOLIO_DATA['personal_info']['github']}" class="contact-link" target="_blank">
                🐙 GitHub
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def display_skills():
    """Display skills section"""
    st.markdown('<div class="section" id="skills">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Skills & Expertise</h2>', unsafe_allow_html=True)
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    
    for category, data in PORTFOLIO_DATA["skills"].items():
        skills_list = " • ".join(data["skills"])
        st.markdown(f'''
        <div class="skill-category">
            <span class="skill-icon">{data["icon"]}</span>
            <h3 class="skill-title">{category}</h3>
            <div class="skill-list">{skills_list}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

def display_projects():
    """Display enhanced projects section"""
    st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
    
    for project in PORTFOLIO_DATA["projects"]:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown(f'<h3 class="project-title">{project["title"]}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="project-description">{project["description"]}</p>', unsafe_allow_html=True)
        
        # Technology tags
        tech_tags = "".join([f'<span class="tech-tag">{tech}</span>' for tech in project["technologies"]])
        st.markdown(f'<div class="tech-stack">{tech_tags}</div>', unsafe_allow_html=True)
        
        # Display images using Streamlit's native image display
        if project["images"]:
            st.markdown("**Project Screenshots:**")
            
            # Create columns for image layout
            num_images = len(project["images"])
            if num_images == 1:
                cols = st.columns(1)
            elif num_images == 2:
                cols = st.columns(2)
            else:
                cols = st.columns(3)
            
            for i, img_path in enumerate(project["images"]):
                try:
                    image = load_image(img_path)
                    if image:
                        with cols[i % len(cols)]:
                            st.image(image, caption=f"Screenshot {i+1}", use_container_width=True)
                except Exception as e:
                    with cols[i % len(cols)]:
                        st.info(f"📸 Image {i+1} - Add your project screenshot here")
                        st.caption(f"Path: {img_path.split('\\')[-1] if '\\' in img_path else img_path}")
        else:
            st.info("📸 Add project images to showcase your work!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_contact():
    """Display enhanced contact section"""
    st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s Connect</h2>', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="about-content">
        <div class="about-text" style="text-align: center;">
            🚀 Ready to collaborate on cutting-edge AI projects? I'm always interested in new opportunities 
            and innovative challenges. Let's build something amazing together!
        </div>
        <div class="contact-links">
            <a href="mailto:{PORTFOLIO_DATA['personal_info']['email']}" class="contact-link">
                📧 Send Email
            </a>
            <a href="{PORTFOLIO_DATA['personal_info']['linkedin']}" class="contact-link" target="_blank">
                💼 Connect on LinkedIn
            </a>
            <a href="{PORTFOLIO_DATA['personal_info']['github']}" class="contact-link" target="_blank">
                🐙 View GitHub Profile
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application with enhanced single-page layout"""
    display_hero()
    display_about()
    display_skills()
    display_projects()
    display_contact()

if __name__ == "__main__":
    main()
