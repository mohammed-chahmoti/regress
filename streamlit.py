import streamlit as st
import numpy as np

def linreg_prediction(var1, var2, var3, var4):
    # Ici, vous devez mettre en place votre modèle de régression linéaire
    # et effectuer la prédiction en utilisant les variables d'entrée

    # Exemple factice de prédiction
    prediction = 0.5 * var1 + 0.3 * var2 + 0.2 * var3 + 0.1 * var4

    return prediction

def show_predict_page():
    st.markdown("""
    ![Logo](https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/logo.png)
    """)
    st.title('Exam Score OLS')

    var1 = st.number_input('Reading Score')
    var2 = st.number_input('P-Grad')
    var3 = st.number_input('sex', min_value=0, max_value=1, value=0)
    var4 = st.number_input('lunch grad')

    pred =''
    if st.button('Predict'):
        pred = linreg_prediction(var1,var2,var3,var4)
    st.success("The predicted score is {}".format(pred))

if __name__ == '__main__':
    show_predict_page()
  