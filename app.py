import streamlit as st
from multiapp import MultiApp
from apps import home, deployment, exp, arcade, machinelearning# import your app modules here

st.set_page_config(layout='wide')
app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Skills, Experience & Education", exp.app)
app.add_app("Arcade Machine", arcade.app)
app.add_app("Machine Learning", machinelearning.app)
app.add_app("Deploying This Website", deployment.app)


# The main app
app.run()