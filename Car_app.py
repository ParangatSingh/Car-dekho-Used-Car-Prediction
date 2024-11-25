# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# from PIL import Image

# # Page Configuration
# st.set_page_config(
#     page_title="CarDheko",
#     page_icon="🚗",
#     layout="wide"
# )

# # Custom CSS
# st.markdown("""
#     <style>
#     .main {
#         padding: 0rem 0rem;
#     }
#     .sidebar .sidebar-content {
#         background-color: #f8f9fa;
#     }
#     .stButton>button {
#         width: 100%;
#         background-color: #0066cc;
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # --- LOAD DATA AND MODEL ---
# @st.cache_data
# def load_data():
#     df = pd.read_csv("final_df.csv")  # Update with your file path
#     return df

# @st.cache_resource
# def load_model():
#     with open('pipeline.pkl', 'rb') as file:  # Update with your model path
#         model = pickle.load(file)
#     return model

# # --- MAIN APP ---
# def main():
#     df = load_data()
#     model = load_model()

#     # Main Application
#     st.title("Car Price Prediction System")
    
#     # Create three columns for input fields
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         with st.container():
#             st.markdown("### Basic Details")
#             Brand = st.selectbox("Brand", options=df['Brand'].unique())
#             filtered_models = df[df['Brand'] == Brand]['model'].unique()
#             Model = st.selectbox("Model", options=filtered_models)
#             Model_year = st.selectbox("Year", options=sorted(df['modelYear'].unique()))
#             Bt = st.selectbox("Body Type", ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 
#                                           'Minivans', 'Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks'])

#     with col2:
#         with st.container():
#             st.markdown("### Technical Details")
#             Ft = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
#             Tr = st.selectbox("Transmission", ['Manual', 'Automatic'])
#             ML = st.number_input("Mileage (km/l)", min_value=5, max_value=50, step=1)
#             seats = st.selectbox("Seats", options=sorted(df['Seats'].unique()))

#     with col3:
#         with st.container():
#             st.markdown("### Additional Info")
#             Owner = st.selectbox("Previous Owners", [0, 1, 2, 3, 4, 5])
#             Km = st.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000)
#             city = st.selectbox("City", options=df['City'].unique())
#             color = st.selectbox("Color", df['Color'].unique())
#             IV = st.selectbox("Insurance Validity", ['Third Party insurance', 'Comprehensive', 
#                                                    'Third Party', 'Zero Dep', '2', '1', 'Not Available'])

#     # Prediction button
#     if st.button("Predict Price 🚀"):
#         with st.spinner("Calculating..."):
#             # Create input dataframe
#             input_data = pd.DataFrame({
#                 'Fuel type': [Ft],
#                 'body type': [Bt],
#                 'transmission': [Tr],
#                 'ownerNo': [Owner],
#                 'Brand': [Brand],
#                 'model': [Model],
#                 'modelYear': [Model_year],
#                 'Insurance Validity': [IV],
#                 'Kms Driven': [Km],
#                 'Mileage': [ML],
#                 'Seats': [seats],
#                 'Color': [color],
#                 'City': [city]
#             })
            
#             # Make prediction
#             prediction = model.predict(input_data)
            
#             # Display result
#             st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")
            
#             # Display car details
#             st.subheader("Selected Car Details:")
#             st.json({
#                 "Brand": Brand,
#                 "Model": Model,
#                 "Year": Model_year,
#                 "Fuel Type": Ft,
#                 "Transmission": Tr,
#                 "Kilometers Driven": f"{Km:,}",
#                 "Mileage": f"{ML} km/l"
#             })

# if __name__ == '__main__':
#     main()

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="CarDheko",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
    }
    .stTextInput, .stSelectbox {
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA AND MODEL ---
@st.cache_data
def load_data():
    df = pd.read_csv("final_df.csv")  # Update with your file path
    return df

@st.cache_resource
def load_model():
    with open('pipeline.pkl', 'rb') as file:  # Update with your model path
        model = pickle.load(file)
    return model

# --- MAIN APP ---
def main():
    df = load_data()
    model = load_model()

    # Main Application Title
    st.title("Car Price Prediction System")
    
    # Create input sections
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("### **Car Details**")
        
        # Select Brand
        Brand = st.selectbox("Brand", options=df['Brand'].unique())
        
        # Filter Models Based on Selected Brand
        filtered_models = df[df['Brand'] == Brand]
        Model = st.selectbox("Model", options=filtered_models['model'].unique())
        
        # Automatically Select Body Type Based on Model
        body_type = filtered_models[filtered_models['model'] == Model]['body type'].values[0]
        st.text(f"Body Type: {body_type}")
        
        # Automatically Select Number of Seats Based on Model
        seats = filtered_models[filtered_models['model'] == Model]['Seats'].values[0]
        st.text(f"Number of Seats: {seats}")
        
        # Filter Year Based on Selected Model
        filtered_years = filtered_models[filtered_models['model'] == Model]['modelYear'].unique()
        Model_year = st.selectbox("Manufacturing Year", options=sorted(filtered_years))

    with col2:
        st.markdown("### **Technical Details**")
        Ft = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
        Tr = st.selectbox("Transmission Type", ['Manual', 'Automatic'])
        ML = st.number_input("Mileage (km/l)", min_value=5, max_value=50, step=1)

    with col3:
        st.markdown("### **Additional Details**")
        Owner = st.selectbox("Previous Owners", [1, 2, 3, 4, 5])  # Starts from 1
        Km = st.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000)
        city = st.selectbox("City", options=df['City'].unique())
        color = st.selectbox("Color", df['Color'].unique())
        IV = st.selectbox("Insurance Validity", ['Third Party insurance', 'Comprehensive', 
                                                 'Third Party', 'Zero Dep', '2', '1', 'Not Available'])

    # Prediction Button
    if st.button("Predict Price"):
        with st.spinner("Calculating..."):
            # Create input dataframe
            input_data = pd.DataFrame({
                'Fuel type': [Ft],
                'body type': [body_type],  # Auto-selected body type
                'transmission': [Tr],
                'ownerNo': [Owner],
                'Brand': [Brand],
                'model': [Model],
                'modelYear': [Model_year],
                'Insurance Validity': [IV],
                'Kms Driven': [Km],
                'Mileage': [ML],
                'Seats': [seats],  # Auto-selected seats
                'Color': [color],
                'City': [city]
            })
            
            # Make prediction
            prediction = model.predict(input_data)
            
            # Display result
            st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")
            
            # Display car details
            st.subheader("Selected Car Details:")
            st.json({
                "Brand": Brand,
                "Model": Model,
                "Year": Model_year,
                "Body Type": body_type,
                "Fuel Type": Ft,
                "Transmission": Tr,
                "Kilometers Driven": f"{Km:,}",
                "Mileage": f"{ML} km/l",
                "Seats": seats  # Display selected seats
            })

if __name__ == '__main__':
    main()


