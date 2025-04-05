import streamlit as st
import pandas as pd
import re
import uuid
import json



def app():

    
    st.sidebar.warning('#### Version\n 1.3.0\n #### Last Updated\n 2024-01-11')
    st.title('PCM-TP: Thermal Properties Predictor of Molten Salts Composite Phase Change Materials')
   
    st.divider()
    
    st.subheader(':book: Introduction')
    st.write('PCM-TP is a web app framework specifically designed for querying and predicting the thermophysical properties of molten salt composite phase change materials (PCM). The PCM-TP database primarily focuses on multicomponent inorganic molten salts, such as nitrate, sulfate, carbonate, halide and more. It provides comprehensive information on the composition, chemical and physical properties of the molten salts, properties of supporting materials, preparation processes, and key performance indicators of PCM. This PCM-TP app enables users to access a prediction tool for the purpose of designing novel materials. ')
    st.subheader(':exclamation: :red[Note]')
    st.markdown('Only by logging in to your account can you view the :red[**PCM-TP Predictor**] pages!')
    st.divider()
    
    st.subheader(':mag: Database Overview')
    c1, c2, c3, c4 = st.columns(4)
    c1.info('##### PCMs\n 3')
    c2.info('##### Salts\n 5')
    c3.info('##### Records\n 574')
    c4.info('##### Literatures\n 48')
    st.write('\n- The database includes phase change materials composed of unary, binary, and ternary mixtures of molten salts. It covers 60 common salt species, primarily categorized into five major classes: nitrate, carbonate, sulfate, and halide (mainly chloride salt and fluoride salt). The supporting material of these phase change materials is expended graphite (EG).')
    
    co1, co2, co3 = st.columns(3)
    if co1.button('Unary'):
        df1=pd.read_excel('Unary.xlsx')
        st.dataframe(df1)
    if co2.button('Binary'):
        df2=pd.read_excel('Binary.xlsx')
        st.dataframe(df2)
    if co3.button('Ternary'):
        df3=pd.read_excel('Ternary.xlsx')
        st.dataframe(df3)
    
    st.divider()
    
    st.subheader(':bulb: Thermal Properties Predictor')
    st.write('Leveraging the PCM-TP database, we have employed advanced machine learning techniques to construct predictive models. These model are specifically designed to provide precise forecasts of the core thermodynamic properties for composite phase change materials. Rigorous validation procedures have been conducted to guarantee the accuracy and robustness of the model. With this tool, users can engage in online formulation design and process optimization, enabling them to access performance data for developing new materials.\n The predictive models provide insights into the following key thermodynamic properties:\n\n- Melting Point(Tm, ℃): The temperature at which substances transition from a solid to a liquid state.\n- Heat of Fusion(Hf, J/g): The amount of heat absorbed by a unit mass of crystalline material to convert it into a liquid state at its melting point.\n- Thermal Conductivity(k, W/m·K): A measure of the ability to conduct heat smoothly and effectively.')