
import streamlit as st
import requests

st.title("Streamlit + FastAPI Demo")

BASE_URL = "http://127.0.0.1:8000"

st.subheader("GET Request")

if st.button("Say Hello"):
    res = requests.get(f"{BASE_URL}/hello")
    st.success(res.json()["message"])

st.subheader("Post request")

name = st.text_input("Enter your name : ")
age = st.number_input("Enter your age : ",min_value = 1, max_value=100 )

if st.button ("Send to backend"):
    payload = {
        "name":name, 
        "age" :age
            }

    res = requests.post(f"{BASE_URL}/greet",json= payload)

    st.success(res.json()["response"])
    ##########################
# import streamlit as st
# import requests

# BASE_URL = "http://127.0.0.1:8000"

# st.title("Streamlit + FastAPI Demo")

# st.subheader("GET Request")

# if st.button("Say Hello"):
#     res = requests.get(f"{BASE_URL}/hello")
#     st.success(res.json()["message"])

# st.subheader("POST Request")

# name = st.text_input("Enter your name")
# age = st.number_input("Enter your age", min_value=1, max_value=100)

# if st.button("Send to backend"):
#     payload = {"name": name, "age": age}
#     res = requests.post(f"{BASE_URL}/greet", json=payload)
#     st.success(res.json()["response"])
