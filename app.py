import streamlit as st

st.title("Product Recommendation System")

def recommend_products():

    return [
        'B00GMTN96U',
        'B00HHRP11C',
        'B001NDYTKA',
        'B00IYXP9HE',
        'B0011Z6CWS'
    ]

user_id = st.number_input(
    "Enter User ID",
    min_value=0
)

if st.button("Recommend Products"):

    recommendations = recommend_products()

    st.write("Recommended Products:")

    for product in recommendations:
        st.write(product)