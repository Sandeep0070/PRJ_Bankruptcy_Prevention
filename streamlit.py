# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:34:44 2022

@author: rupesh
"""

# -*- coding: utf-8 -*-


import numpy as np
import pickle
import pandas as pd

from sklearn.linear_model import LogisticRegression
import streamlit as st

from PIL import Image

pickle_in = open("SVM.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome"
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
    st.title("Bankruptcy Detector")
    html_temp = """
    <div style="background-color:tomato;padding:5px">
    <h2 style="color:white;text-align:center;">Streamlit Bankruptcy Detector </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    industrial_risk = st.text_input("industrial_risk")
    management_risk = st.text_input("management_risk")
    financial_flexibility = st.text_input("financial_flexibility")
    credibility = st.text_input("credibility")
    competitiveness = st.text_input("competitiveness")
    operating_risk = st.text_input("operating_risk")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
    st.text("Bankruptcy=0          Non-Bankruptcy=1")
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()


