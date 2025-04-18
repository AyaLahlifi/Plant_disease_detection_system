import streamlit as st
import tensorflow as tf
import numpy as np
import json
import markdown

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# css style
def local_css():
    st.markdown("""
    <style>
    /* Overall App Styling */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #4CAF50;
        font-weight: 600;
    }
    
    /* Text Styling */
    .stMarkdown {
        color: #e0e0e0;
    }
    
    /* Sidebar Styling */
    .css-1aumxhk {
        background-color: #1e1e1e;
        border-right: 2px solid #4CAF50;
    }
    
    /* Sidebar Selectbox */
    .stSelectbox > div > div > div {
        background-color: #2c2c2c;
        color: #e0e0e0;
        border: 1px solid #4CAF50;
        border-radius: 5px;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #45a049;
    }
    
    /* Card-like Containers */
    .stContainer {
        background-color: #1e1e1e;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        padding: 20px;
        margin-bottom: 20px;
        color: #e0e0e0;
    }
    
    /* Alert and Info Boxes */
    .stAlert {
        border-radius: 5px;
    }
    
    /* Image Upload */
    .uploadedImage {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Expander */
    .stExpander {
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    
    /* File Uploader */
    .stFileUploader > div > div {
        background-color: #2c2c2c;
        color: #e0e0e0;
    }
    
    /* Success, Warning, Info Messages */
    .stAlert-success {
        background-color: #2e7d32;
        color: white;
    }
    
    .stAlert-warning {
        background-color: #f57c00;
        color: white;
    }
    
    .stAlert-info {
        background-color: #1976d2;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Load Disease Information
def load_disease_info():
    try:
        with open('disease_info.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Disease information file not found. Please ensure disease_info.json exists.")
        return {}

# Function to read guide
def read_farmers_guide():
    try:
        with open('first_time_farmers_guide.md', 'r', encoding='utf-8') as f:
            guide_content = f.read()
        return markdown.markdown(guide_content)
    except FileNotFoundError:
        return "Farmer's Guide file not found."

# Main App
def main():
    local_css()
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    #disease map
    CLASS_NAMES = [
        'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 
        'Apple___healthy', 'Blueberry___healthy', 
        'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
        'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
        'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
        'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 
        'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
        'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
        'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
        'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
        'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
        'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
        'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
    ]

    # Sidebar
    st.sidebar.title("🌿 Plant Health Dashboard")
    app_mode = st.sidebar.selectbox("Navigate", [
        "Home", 
        "About",
        "Disease Recognition", 
        "Farmer's Guide"
    ], index=[
        "Home", 
        "About",
        "Disease Recognition", 
        "Farmer's Guide"
       
    ].index(st.session_state.page))

    st.session_state.page = app_mode

   # Home page
    if app_mode == "Home":
        st.title("Plant Disease Recognition System")
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            ## Revolutionizing Agricultural Health 🌿

            ### Empowering Farmers with AI-Driven Insights
            - 🔬 Advanced Disease Detection
            - 📊 Instant Crop Analysis
            - 🌍 Sustainable Farming Solutions
            """)
            
            # Get Started Button with Navigation
            if st.button("Explore Plant Health", type="primary"):
                st.session_state.page = "Disease Recognition"
                st.experimental_rerun()
        
        with col2:
            st.image("home1.jpg", use_container_width=True, 
                     caption="Healthy Crops, Thriving Farms")
        
        # Features Section with Icons and Detailed Descriptions
        st.markdown("## Our Innovative Features")
        
        # Create a grid-like layout for features
        features = [
            {
                "icon": "🔍",
                "title": "Precision Detection",
                "description": "Our AI-powered system identifies plant diseases with remarkable accuracy, providing farmers with critical insights."
            },
            {
                "icon": "📚",
                "title": "Expert Guidance",
                "description": "Receive comprehensive treatment recommendations and preventive strategies tailored to specific plant conditions."
            },
            {
                "icon": "🌐",
                "title": "Continuous Learning",
                "description": "Access a growing database of plant health information, updated with the latest agricultural research."
            }
        ]
        
        # affichage
        cols = st.columns(3)
        for i, feature in enumerate(features):
            with cols[i]:
                st.markdown(f"### {feature['icon']} {feature['title']}")
                st.write(feature['description'])
        

    # Disease Recognition page
    elif app_mode == "Disease Recognition":
        # Load disease information
        disease_info = load_disease_info()

        st.title("Plant Disease Detection 🔎🌱")
        
        # Image Upload Section
        st.markdown("### Upload Plant Leaf Image")
        test_image = st.file_uploader("Choose an Image", type=['jpg', 'png', 'jpeg'])
        
        if test_image is not None:
            # Display uploaded image
            st.image(test_image, use_container_width=True, 
                     caption="Uploaded Plant Leaf", 
                     output_format='PNG')
            
            # Predict Button
            if st.button("Analyze Disease", type="primary"):
                with st.spinner("Analyzing image..."):
                    # Get prediction
                    result_index = model_prediction(test_image)
                    detected_disease = CLASS_NAMES[result_index]
                    
                    #  prediction
                    st.success(f"Detected Disease: {detected_disease}")
                    
                    # is it 'healthy'
                    if 'healthy' not in detected_disease.lower():
                        # disease info 
                        if detected_disease in disease_info:
                            # symptoms & solutions
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.markdown("### 🔍 Symptoms")
                                st.write(disease_info[detected_disease]["symptoms"])
                            
                            with col2:
                                st.markdown("### 🛠️ Recommended Solutions")
                                solutions = disease_info[detected_disease]["solutions"]
                                for solution in solutions:
                                    st.markdown(f"- {solution}")
                        else:
                            st.warning(f"Detailed information for {detected_disease} is not available in our database.")
                    else:
                        st.info("Great news! The plant appears to be healthy.")

    # Farmer's Guide page
    elif app_mode == "Farmer's Guide":
        st.title(" First-Time Farmer's Comprehensive Guide👩🏻‍🌾")
        
        # markdown guide
        guide_content = read_farmers_guide()
        
        # Render the guide content with HTML rendering
        st.markdown(guide_content, unsafe_allow_html=True)
        
        # YouTube videos
        st.markdown("## 📽️ Recommended Learning Videos")
        
        # Define video information
        videos = [
            {
                "title": "How Plants Grow",
                "description": "Understand the fundamental stages of plant growth and development",
                "url": "https://www.youtube.com/watch?v=CBjrdMlZlfE&ab_channel=NextGenerationScience"  
            },
            {
                "title": "Cabbage Farming for Beginners",
                "description": "Step-by-step guide to growing cabbage from planting to harvesting",
                "url": "https://www.youtube.com/watch?v=UPk72G1CIt8&t=98s&ab_channel=FarmChannel"  
            },
            {
                "title": "Starting a Farm from Scratch",
                "description": "Essential tips for new farmers on growing vegetables for profit",
                "url": "https://www.youtube.com/watch?v=fRlUhUWS0Hk&t=18s&ab_channel=TheDutchFarmer"  
            }
        ]
        
        cols = st.columns(3)
        
        for i, video in enumerate(videos):
            with cols[i]:
                st.markdown(f"### {video['title']}")
                st.write(video['description'])
                st.link_button("Watch Video", video['url'], type="primary")

    # About Page
    elif app_mode == "About":
        st.title("About Our Plant Disease Recognition System")
        
        # Mission and Vision Section
        st.markdown("## Our Mission ")
        st.markdown("""
        To revolutionize agricultural health by providing farmers with cutting-edge, AI-powered plant disease detection and management tools.

        ### Vision
        We envision a world where technology empowers farmers to:
        - Protect their crops with precision
        - Increase agricultural productivity
        - Promote sustainable farming practices
        """)
        
        # Technology Section
        st.markdown("## Technology Behind Our Solution ")
        
        # Create columns for technology details
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.markdown("### 🧠 AI & Machine Learning")
            st.write("""
            - Advanced Deep Learning Algorithms
            - Convolutional Neural Networks (CNN)
            - Transfer Learning Techniques
            """)
        
        with tech_col2:
            st.markdown("### 🔬 Data-Driven Approach")
            st.write("""
            - 87,000+ High-Resolution Plant Images
            - 38 Different Plant Disease Categories
            - Continuous Model Improvement
            """)
        
        # Dataset Breakdown
        st.markdown("## Dataset Composition 📊")
        
        # Progress bars for dataset visualization
        st.markdown("### Training Dataset Breakdown")
        st.progress(0.7, text="Training Set: 70,295 images (70%)")
        st.progress(0.18, text="Validation Set: 17,572 images (18%)")
        st.progress(0.02, text="Test Set: 33 images (2%)")
        
        # Team and Collaboration Section
        st.markdown("## Our Team 👥")
        
        # Team members (you can replace with actual team info)
        team_members = [
            {
                "name": "LAHLIFI Aya"
            },
            {
                "name": "ZERZANE Abdelmouneim"
            
            }
        ]
        
        # Display team members
        cols = st.columns(2)
        for i, member in enumerate(team_members):
            with cols[i]:
                st.markdown(f"### {member['name']}")
        

# Run the app
if __name__ == "__main__":
    main()
