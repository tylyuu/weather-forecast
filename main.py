import streamlit as st
import plotly.express as px
from backend import get_data
from send_email import send_email

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.image("images/clear.png")
with col2:
   st.image("images/cloud.png")
with col3:
   st.image("images/rain.png")
with col4:
   st.image("images/snow.png")

# Ass title, text input, slider, selectbox and subheader
st.title("Smart Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
    # Get the temperature sky data/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [(dict["main"]["temp"] - 273.15 )  for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

except KeyError:
    st.write("Invalid place name, please enter another place.")

st.write("Remind your loved ones to put on clothes...")

st.empty()

with st.form(key="form"):
    user_email = st.text_input("His/Her email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Send!")
    if button:
        send_email(message)
        st.info("Your email was sent succesfully!")


