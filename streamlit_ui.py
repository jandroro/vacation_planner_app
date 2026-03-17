"""
AI-Powered Vacation Planner - Streamlit Web Interface

Professional-level vacation planning accessible to everyone through
a beautiful, user-friendly web interface.
"""

import streamlit as st
from src.vacation_planner.crew import VacationPlanner
import os
from dotenv import load_dotenv
from datetime import datetime
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Vacation Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">✈️ AI-Powered Vacation Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Professional-Level Travel Planning for Everyone | Powered by Amazon Bedrock & CrewAI</p>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("🎯 Your Vacation Preferences")
    
    with st.expander("📍 Destination", expanded=True):
        destination_name = st.text_input(
            "Destination Name",
            placeholder="e.g., Lima, Paris, Tokyo",
            help="Enter any city or country you'd like to explore!"
        )
    
    st.markdown("---")
    
    # Display summary
    st.markdown("### 📋 Planning Summary")
    st.markdown(f"""
    - **Destination Name:** {destination_name or "Lima"}
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🚀 Generate Your Perfect Vacation Plan")
    
    st.markdown("""
    <div class="info-box">
        <h4>How It Works:</h4>
        <ol>
            <li><b>Research Specialist</b> gathers real-time destination information</li>
            <li><b>Itinerary Planner</b> creates your optimized itinerary</li>
        </ol>
        <p><b>⏱️ Planning typically takes 1-5 minutes</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Planning button
    if st.button("🎯 Plan My Perfect Vacation", type="primary"):
        
        # Prepare inputs
        inputs = {
            'topic': destination_name or "Lima",
        }
        
        # Create progress indicators
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        #try:
        # Initialize crew
        status_text.text("🤖 Initializing AI agents...")
        progress_bar.progress(10)
        
        vacation_planner = VacationPlanner()
        crew = vacation_planner.crew()
        
        # Research phase
        status_text.text("🔍 Research Specialist gathering destination information...")
        progress_bar.progress(25)
        
        # Planning phase
        status_text.text("📋 Itinerary Planner creating your itinerary...")
        progress_bar.progress(50)
        
        # Execute crew
        with st.spinner("AI agents working collaboratively..."):
            result = crew.kickoff(inputs=inputs)
        
        # Print result for debugging
        print(result)
        if result is None:
            st.error("❌ No result generated. Please check your inputs and try again.")
            st.stop()
        
        progress_bar.progress(100)
        status_text.text("✅ Vacation plan complete!")
        
        # Success message
        st.markdown("""
        <div class="success-box">
            <h3>🎉 Your Personalized Vacation Plan is Ready!</h3>
            <p>Our AI agents have created a comprehensive plan tailored specifically for you.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"vacation_plan_{timestamp}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(result))
        
        # Display results in tabs
        tab1, tab2 = st.tabs(["📄 Full Itinerary", "📥 Download"])
        
        with tab1:
            st.markdown("### Your Complete Vacation Plan")
            st.markdown(result)
        
        with tab2:
            st.markdown("### 📥 Download Your Plan")
            
            # Download button for main plan
            with open(output_file, 'r', encoding='utf-8') as f:
                plan_content = f.read()
            
            st.download_button(
                label="📄 Download Full Itinerary (Markdown)",
                data=plan_content,
                file_name=output_file,
                mime="text/markdown"
            )
            
            st.success(f"✅ Files saved locally: {output_file}")
            
        # except Exception as e:
        #     st.error(f"❌ Error generating vacation plan: {str(e)}")
        #     st.markdown("""
        #     ### Troubleshooting Tips:
        #     - ✅ Check your AWS credentials are configured
        #     - ✅ Verify Bedrock model access in AWS Console
        #     - ✅ Ensure SERPER_API_KEY is set in .env file
        #     - ✅ Check your internet connection
        #     - ✅ Review CloudWatch logs for detailed errors
        #     """)
            
        #     with st.expander("🔍 Error Details"):
        #         st.code(str(e))

with col2:
    st.markdown("### 💡 Travel Planning Tips")
    
    st.info("""
    **For Best Results:**
    - Be specific about your interests
    - Consider seasonal weather
    - Include any special requirements
    - Think about your ideal pace
    """)
    
    st.markdown("### 🌟 Features")
    
    st.success("""
    ✅ **Real-time Research**
    - Current prices & availability
    - Latest travel advisories
    - Seasonal recommendations
    """)
    
    st.success("""
    ✅ **Smart Optimization**
    - Geographic clustering
    - Realistic timing
    - Budget maximization
    """)
    
    st.success("""
    ✅ **Local Insights**
    - Authentic experiences
    - Hidden gems
    - Cultural sensitivity
    """)
    
    st.markdown("### 🤖 About")
    
    st.markdown("""
    **Powered By:**
    - 🧠 Amazon Bedrock (Nova Pro)
    - 🤝 CrewAI Multi-Agent System
    - 🔍 Real-time Web Research
    - 📊 Intelligent Analytics
    
    **Our Mission:**
    Democratize expert travel planning
    by making professional-level vacation
    planning accessible to everyone,
    24/7, at no cost.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><b>AI-Powered Vacation Planner v1.0</b></p>
    <p>Made with ❤️ using Amazon Bedrock, CrewAI & Streamlit</p>
    <p>🌍 Making Expert Travel Planning Accessible to Everyone 🌍</p>
</div>
""", unsafe_allow_html=True)
