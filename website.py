import streamlit as st
import cmath

# Import 4 calculation functions from 4 files in Project_1 folder
from lumped_element import lumped_element_matching_method
from shorted_stub import shorted_stub_matching_method
from opened_stub import opened_stub_matching_method
from quarter_wavelength import quarter_wavelength_matching_method

st.set_page_config(page_title="Impedance Matching", layout="wide")
st.title("Impedance Matching Tool")
st.divider()

# AREA 1: INPUT PARAMETERS
st.subheader("1. System Parameters Input")

# Use st.columns to divide input fields horizontally for neatness
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    r_l = st.number_input("Real part of Z_L", value=None, placeholder="Ex: 100")
with col2:
    x_l = st.number_input("Imaginary part of Z_L", value=None, placeholder="Ex: 50")
with col3:
    Z_0 = st.number_input("Impedance Z_0", value=None, placeholder="Ex: 50")
with col4:
    f = st.number_input("Frequency f (Hz)", value=None, format="%e", placeholder="Ex: 2.4e9")
with col5:
    e_r = st.number_input("Dielectric const e_r", value=None, placeholder="Ex: 4.4")

# Combine real and imaginary parts into a complex number


st.divider()

# AREA 2: SELECT MATCHING METHOD
st.subheader("2. Select Matching Method")
btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

with btn_col1:
    btn_shunt = st.button("Lumped Element (L, C)", use_container_width=True)
with btn_col2:
    btn_shorted = st.button("Shorted Stub", use_container_width=True)
with btn_col3:
    btn_opened = st.button("Opened Stub", use_container_width=True)
with btn_col4:
    btn_quarter = st.button("Quarter-Wave Transformer", use_container_width=True)

st.divider()

# AREA 3: PROCESS LOGIC AND DISPLAY RESULTS
st.subheader("3. Results")

# Function to check if the user has entered all 5 parameters
def kiem_tra_dau_vao():
    # 1. Bắt lỗi để trống dữ liệu
    if None in [r_l, x_l, Z_0, f, e_r]:
        # If any field is empty, warn and stop the web app from continuing
        st.warning("⚠️ Please enter all 5 parameters above before calculating!")
        st.stop()
        
    # 2. Bắt lỗi vật lý vô lý (Giá trị âm hoặc bằng 0)
    if f <= 0 or e_r <= 0 or Z_0 <= 0:
        st.error("❌ Physical Error: Frequency (f), Dielectric constant (e_r), and Characteristic Impedance (Z0) must be strictly strictly positive (>0)!")
        st.stop()
        
    return complex(r_l, x_l)

# --- Process when each button is clicked ---
if btn_shunt:
    Z_l = kiem_tra_dau_vao()
    st.info("Currently using method: **Lumped Element (L, C)**")
    
    # 1. Get result from the function
    ket_qua = lumped_element_matching_method(Z_l, Z_0, f, e_r)
    
    # 2. Divide space: 3 parts text, 2 parts image
    col_chu, col_anh = st.columns([3, 2])
    
    # 3. Put text on the left
    with col_chu:
        st.write(ket_qua)
        
    # 4. Put 2 images on the right
    with col_anh:
        # Image 1: Capacitor
        st.image("shunt_element_capacitor.png", caption="Using Capacitor", use_container_width=True)
        # Image 2: Inductor 
        st.image("shunt_element_inductor.png", caption="Using Inductor", use_container_width=True)

elif btn_shorted:
    Z_l = kiem_tra_dau_vao()
    st.info("Currently using method: **Shorted Stub**")
    
    # 1. Run function to get text result first
    ket_qua = shorted_stub_matching_method(Z_l, Z_0, f, e_r)
    
    # 2. Divide the space below into 2 columns 
    # [3, 2] means text column takes 60% width, image column takes 40%
    col_chu, col_anh = st.columns([3, 2]) 
    
    # 3. Put text in the left column
    with col_chu:
        st.write(ket_qua)
        
    # 4. Put image in the right column
    with col_anh:
        st.image("shorted_stub_im.png", caption="Shorted Stub Diagram", use_container_width=True)


elif btn_opened:
    Z_l = kiem_tra_dau_vao()
    st.info("Currently using method: **Opened Stub**")
    
    # 1. Get result from the function
    ket_qua = opened_stub_matching_method(Z_l, Z_0, f, e_r)
    
    # 2. Divide space: 3 parts text, 2 parts image
    col_chu, col_anh = st.columns([3, 2])
    
    # 3. Put text on the left
    with col_chu:
        st.write(ket_qua)
        
    # 4. Put image on the right (Remember quotes around file name)
    with col_anh:
        st.image("opened_stub_im.png", caption="Opened Stub Diagram", use_container_width=True)

elif btn_quarter:
    Z_l = kiem_tra_dau_vao()
    st.info("Currently using method: **Quarter-Wave Transformer**")
    
    # 1. Get result from the function
    ket_qua = quarter_wavelength_matching_method(Z_l, Z_0, f, e_r)
    
    # 2. Divide space: 3 parts text, 2 parts image
    col_chu, col_anh = st.columns([3, 2])
    
    # 3. Put text on the left
    with col_chu:
        st.write(ket_qua)
        
    # 4. Put image on the right
    with col_anh:
        st.image("quarter_wavelength_im.png", caption="Quarter-Wave Transformer Diagram", use_container_width=True)