import streamlit as st
st.title("Resturant Menu Generator")
cuisine = st.sidebar.selectbox("Pick a option", ("Indian", 'Mexican',"Italian", "Spanish", "French", "Duch"))

def generate_resturant_name_and_item(cuisine):
    return{
        'resturant_name':"Bengali Dhaba",
        'menu_item':'Samosa, Paneer Tikka, Nun'
    }
    
if cuisine:
    response = generate_resturant_name_and_item(cuisine)
    st.header(response['resturant_name'])
    menu_items = response['menu_item'].split(",")
    
    for item in menu_items:
        st.write("-", item)