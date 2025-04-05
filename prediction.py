import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import uuid
import re
import pandas as pd
import joblib
import numpy as np


def app():
    
    def create_st_button(link_text, link_url, hover_color="#e78ac3", st_col=None):

        button_uuid = str(uuid.uuid4()).replace("-", "")
        button_id = re.sub("\d+", "", button_uuid)

        button_css = f"""
            <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }}
            #{button_id}:hover {{
                border-color: {hover_color};
                color: {hover_color};
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: {hover_color};
                color: white;
                }}
        </style> """

        html_str = f'<a href="{link_url}" target="_blank" id="{button_id}";>{link_text}</a><br></br>'
        
        if st_col is None:
            st.markdown(button_css + html_str, unsafe_allow_html=True)
        else:
            st_col.markdown(button_css + html_str, unsafe_allow_html=True)

    
    database_link_dict = {
        "PubChem": "https://pubchem.ncbi.nlm.nih.gov/", "Materials Project": "https://next-gen.materialsproject.org/",
        "wikipedia": "https://en.wikipedia.org/",
    }

    st.sidebar.markdown("## Molten salt performance-Related Links")
    for link_text, link_url in database_link_dict.items():
        create_st_button(link_text, link_url, st_col=st.sidebar)
        
      
    st.title('PCM-TP Predictor')
   
    st.divider()
    
    st.markdown('### Phase change materials')
    st.markdown('##### _Composition --- The following are the components of phase change materials._')
    col1, col2, col3 = st.columns(3)
    
    data=pd.read_excel('t.xlsx')
    
    option_1 = col1.selectbox(
        '##### :green[Molten salt 1]'
        ,data['Molten salt']
        ,index=44
        )
    option_2 = col2.selectbox(
        '##### :green[Molten salt 2]'
        ,data['Molten salt']
        ,index=24
        )
    option_3 = col3.selectbox(
        '##### :green[Molten salt 3]'
        ,data['Molten salt']
        )
        
    for i in data['Molten salt']:
        if option_1 == i:
            tpsa_1 = data[data['Molten salt'] == i].iloc[:,1].to_frame()
            tpsa_1 = tpsa_1.iloc[:,-1].values
            c_1 = data[data['Molten salt'] == i].iloc[:,2].to_frame()
            c_1 = c_1.iloc[:,-1].values
            cb_1 = data[data['Molten salt'] == i].iloc[:,3].to_frame()
            cb_1 = cb_1.iloc[:,-1].values
            bg_1 = data[data['Molten salt'] == i].iloc[:,4].to_frame()
            bg_1 = bg_1.iloc[:,-1].values
            pfe_1 = data[data['Molten salt'] == i].iloc[:,5].to_frame()
            pfe_1 = pfe_1.iloc[:,-1].values
            eah_1 = data[data['Molten salt'] == i].iloc[:,6].to_frame()
            eah_1 = eah_1.iloc[:,-1].values
            cv_1 = data[data['Molten salt'] == i].iloc[:,7].to_frame()
            cv_1 = cv_1.iloc[:,-1].values
            noa_1 = data[data['Molten salt'] == i].iloc[:,8].to_frame()
            noa_1 = noa_1.iloc[:,-1].values
            cr_1 = data[data['Molten salt'] == i].iloc[:,9].to_frame()
            cr_1 = cr_1.iloc[:,-1].values
            ar_1 = data[data['Molten salt'] == i].iloc[:,10].to_frame()
            ar_1 = ar_1.iloc[:,-1].values
            mp_1 = data[data['Molten salt'] == i].iloc[:,11].to_frame()
            mp_1 = mp_1.iloc[:,-1].values
            bp_1 = data[data['Molten salt'] == i].iloc[:,12].to_frame()
            bp_1 = bp_1.iloc[:,-1].values
            d_1 = data[data['Molten salt'] == i].iloc[:,13].to_frame()
            d_1 = d_1.iloc[:,-1].values
            hof_1 = data[data['Molten salt'] == i].iloc[:,14].to_frame()
            hof_1 = hof_1.iloc[:,-1].values
            mw_1 = data[data['Molten salt'] == i].iloc[:,15].to_frame()
            mw_1 = mw_1.iloc[:,-1].values
            cvs_1 = data[data['Molten salt'] == i].iloc[:,16].to_frame()
            cvs_1 = cvs_1.iloc[:,-1].values
    
    for a in data['Molten salt']:
        if option_2 == a:
            tpsa_2 = data[data['Molten salt'] == i].iloc[:,1].to_frame()
            tpsa_2 = tpsa_2.iloc[:,-1].values
            c_2 = data[data['Molten salt'] == i].iloc[:,2].to_frame()
            c_2 = c_2.iloc[:,-1].values
            cb_2 = data[data['Molten salt'] == i].iloc[:,3].to_frame()
            cb_2 = cb_2.iloc[:,-1].values
            bg_2 = data[data['Molten salt'] == i].iloc[:,4].to_frame()
            bg_2 = bg_2.iloc[:,-1].values
            pfe_2 = data[data['Molten salt'] == i].iloc[:,5].to_frame()
            pfe_2 = pfe_2.iloc[:,-1].values
            eah_2 = data[data['Molten salt'] == i].iloc[:,6].to_frame()
            eah_2 = eah_2.iloc[:,-1].values
            cv_2 = data[data['Molten salt'] == i].iloc[:,7].to_frame()
            cv_2 = cv_2.iloc[:,-1].values
            noa_2 = data[data['Molten salt'] == i].iloc[:,8].to_frame()
            noa_2 = noa_2.iloc[:,-1].values
            cr_2 = data[data['Molten salt'] == i].iloc[:,9].to_frame()
            cr_2 = cr_2.iloc[:,-1].values
            ar_2 = data[data['Molten salt'] == i].iloc[:,10].to_frame()
            ar_2 = ar_2.iloc[:,-1].values
            mp_2 = data[data['Molten salt'] == i].iloc[:,11].to_frame()
            mp_2 = mp_2.iloc[:,-1].values
            bp_2 = data[data['Molten salt'] == i].iloc[:,12].to_frame()
            bp_2 = bp_2.iloc[:,-1].values
            d_2 = data[data['Molten salt'] == i].iloc[:,13].to_frame()
            d_2 = d_2.iloc[:,-1].values
            hof_2 = data[data['Molten salt'] == i].iloc[:,14].to_frame()
            hof_2 = hof_2.iloc[:,-1].values
            mw_2 = data[data['Molten salt'] == i].iloc[:,15].to_frame()
            mw_2 = mw_2.iloc[:,-1].values
            cvs_2 = data[data['Molten salt'] == i].iloc[:,16].to_frame()
            cvs_2 = cvs_2.iloc[:,-1].values
           
    for b in data['Molten salt']:
        if option_3 == b:
            tpsa_3 = data[data['Molten salt'] == i].iloc[:,1].to_frame()
            tpsa_3 = tpsa_3.iloc[:,-1].values
            c_3 = data[data['Molten salt'] == i].iloc[:,2].to_frame()
            c_3 = c_3.iloc[:,-1].values
            cb_3 = data[data['Molten salt'] == i].iloc[:,3].to_frame()
            cb_3 = cb_3.iloc[:,-1].values
            bg_3 = data[data['Molten salt'] == i].iloc[:,4].to_frame()
            bg_3 = bg_3.iloc[:,-1].values
            pfe_3 = data[data['Molten salt'] == i].iloc[:,5].to_frame()
            pfe_3 = pfe_3.iloc[:,-1].values
            eah_3 = data[data['Molten salt'] == i].iloc[:,6].to_frame()
            eah_3 = eah_3.iloc[:,-1].values
            cv_3 = data[data['Molten salt'] == i].iloc[:,7].to_frame()
            cv_3 = cv_3.iloc[:,-1].values
            noa_3 = data[data['Molten salt'] == i].iloc[:,8].to_frame()
            noa_3 = noa_3.iloc[:,-1].values
            cr_3 = data[data['Molten salt'] == i].iloc[:,9].to_frame()
            cr_3 = cr_3.iloc[:,-1].values
            ar_3 = data[data['Molten salt'] == i].iloc[:,10].to_frame()
            ar_3 = ar_3.iloc[:,-1].values
            mp_3 = data[data['Molten salt'] == i].iloc[:,11].to_frame()
            mp_3 = mp_3.iloc[:,-1].values
            bp_3 = data[data['Molten salt'] == i].iloc[:,12].to_frame()
            bp_3 = bp_3.iloc[:,-1].values
            d_3 = data[data['Molten salt'] == i].iloc[:,13].to_frame()
            d_3 = d_3.iloc[:,-1].values
            hof_3 = data[data['Molten salt'] == i].iloc[:,14].to_frame()
            hof_3 = hof_3.iloc[:,-1].values
            mw_3 = data[data['Molten salt'] == i].iloc[:,15].to_frame()
            mw_3 = mw_3.iloc[:,-1].values
            cvs_3 = data[data['Molten salt'] == i].iloc[:,16].to_frame()
            cvs_3 = cvs_3.iloc[:,-1].values
   
        
            
    
    co1, co2 ,co3= st.columns(3)
    with co1.expander("Please enter the properties of molten salt 1"):
        tab1, tab2, tab3, tab4 = st.tabs(['Physical','Thermodynamic','Microscopic','Structure'])
        with tab1:
            y13=st.number_input(
            'Density of molten salt 1(g/cm3)'
            ,min_value=1.0
            ,max_value=10.0
            ,value=2.257
            ,step=1.0
            )
            y15=st.number_input(
            'Molecular weight of molten salt 1(g/mol)'
            ,min_value=20.0
            ,max_value=500.0
            ,value=84.9947
            ,step=100.0
            )
        with tab2:
            y11=st.number_input(
            'Melting point of molten salt 1(℃)'
            ,min_value=200.0
            ,max_value=1800.0
            ,value=306.8
            ,step=100.0
            )
            y12=st.number_input(
            'Boiling point of molten salt 1(℃)'
            ,min_value=100.0
            ,max_value=3000.0
            ,value=380.0
            ,step=100.0
            )
            y14=st.number_input(
            'Heat of fusion of molten salt 1(J/g)'
            ,min_value=30.0
            ,max_value=1200.0
            ,value=162.5
            ,step=100.0
            )
        with tab3:
            y2=st.number_input(
            'Complexity of molten salt 1'
            ,min_value=0.0
            ,max_value=100.0
            ,value=18.8
            ,step=10.0
            )
            y7=st.number_input(
            'Crystal volume of molten salt 1(Å³)'
            ,min_value=20.0
            ,max_value=1500.0
            ,value=360.02
            ,step=50.0
            )
            y8=st.number_input(
            'Number of atoms of molten salt 1'
            ,min_value=0
            ,max_value=100
            ,value=30
            ,step=10
            )
            y9=st.number_input(
            'Cationic radius of molten salt 1(nm)'
            ,min_value=0.0
            ,max_value=0.2
            ,value=0.102
            ,step=0.05
            )
            y10=st.number_input(
            'Anion radius of molten salt 1(nm)'
            ,min_value=0.0
            ,max_value=0.5
            ,value=0.189
            ,step=0.05
            )
            y16=st.number_input(
            'Cation valence state of molten salt 1'
            ,min_value=1
            ,max_value=5
            ,value=1
            ,step=1
            )
        with tab4:
            y1=st.number_input(
            'Topological polar surface area of molten salt 1(Å²)'
            ,min_value=0.0
            ,max_value=200.0              
            ,value=62.9
            ,step=10.0
            )
            
            y3=st.number_input(
            'Covalently-bonded unit count of molten salt 1'
            ,min_value=0
            ,max_value=10
            ,value=2
            ,step=1
            )
            y4=st.number_input(
            'Band gap of molten salt 1(eV)'
            ,min_value=0.0
            ,max_value=10.0
            ,value=2.95
            ,step=0.1
            )
            y5=st.number_input(
            'Predicted formation energy of molten salt 1(eV/atom)'
            ,min_value=-10.0
            ,max_value=10.0
            ,value=-1.361
            ,step=1.0
            )
            y6=st.number_input(
            'Energy above hull of molten salt 1(eV/atom)'
            ,min_value=0.0
            ,max_value=5.0
            ,value=0.0
            ,step=1.0
            )
            
            
            
    with co2.expander("Please enter the properties of molten salt 2"):
        tab1, tab2, tab3, tab4 = st.tabs(['Physical','Thermodynamic','Microscopic','Structure'])
        with tab1:
            e13=st.number_input(
            'Density of molten salt 2(g/cm3)'
            ,min_value=1.0
            ,max_value=10.0
            ,value=2.016
            ,step=1.0
            )
            e15=st.number_input(
            'Molecular weight of molten salt 2(g/mol)'
            ,min_value=20.0
            ,max_value=500.0
            ,value=101.1032
            ,step=100.0
            )
        with tab2:
            e11=st.number_input(
            'Melting point of molten salt 2(℃)'
            ,min_value=200.0
            ,max_value=1800.0
            ,value=337.0
            ,step=100.0
            )
            e12=st.number_input(
            'Boiling point of molten salt 2(℃)'
            ,min_value=100.0
            ,max_value=3000.0
            ,value=400.0
            ,step=100.0
            )
            e14=st.number_input(
            'Heat of fusion of molten salt 2(J/g)'
            ,min_value=30.0
            ,max_value=1200.0
            ,value=99.64
            ,step=100.0
            )
        with tab3:
            e2=st.number_input(
            'Complexity of molten salt 2'
            ,min_value=0.0
            ,max_value=100.0
            ,value=18.8
            ,step=10.0
            )
            e7=st.number_input(
            'Crystal volume of molten salt 2(Å³)'
            ,min_value=20.0
            ,max_value=1500.0
            ,value=306.25
            ,step=50.0
            )
            e8=st.number_input(
            'Number of atoms of molten salt 2'
            ,min_value=0
            ,max_value=100
            ,value=20
            ,step=10
            )
            e9=st.number_input(
            'Cationic radius of molten salt 2(nm)'
            ,min_value=0.0
            ,max_value=0.2
            ,value=0.138
            ,step=0.05
            )
            e10=st.number_input(
            'Anion radius of molten salt 2(nm)'
            ,min_value=0.0
            ,max_value=0.5
            ,value=0.189
            ,step=0.05
            )
            e16=st.number_input(
            'Cation valence state of molten salt 2'
            ,min_value=1
            ,max_value=5
            ,value=1
            ,step=1
            )
        with tab4:
            e1=st.number_input(
            'Topological polar surface area of molten salt 2(Å²)'
            ,min_value=0.0
            ,max_value=200.0
            ,value=62.9
            ,step=10.0
            )
            e3=st.number_input(
            'Covalently-bonded unit count of molten salt 2'
            ,min_value=0
            ,max_value=10
            ,value=2
            ,step=1
            )
            e4=st.number_input(
            'Band gap of molten salt 2(eV)'
            ,min_value=0.0
            ,max_value=10.0
            ,value=2.94
            ,step=0.1
            )
            e5=st.number_input(
            'Predicted formation energy of molten salt 2(eV/atom)'
            ,min_value=-10.0
            ,max_value=10.0
            ,value=-1.42
            ,step=1.0
            )
            e6=st.number_input(
            'Energy above hull of molten salt 2(eV/atom)'
            ,min_value=0.0
            ,max_value=5.0
            ,value=0.0
            ,step=1.0
            )
        
        
        
    with co3.expander("Please enter the properties of molten salt 3"):
        tab1, tab2, tab3, tab4 = st.tabs(['Physical','Thermodynamic','Microscopic','Structure'])
        with tab1:
            s13=st.number_input(
            'Density of molten salt 3(g/cm3)'
            ,min_value=1.0
            ,max_value=10.0
            ,step=1.0
            )
            s15=st.number_input(
            'Molecular weight of molten salt 3(g/mol)'
            ,min_value=20.0
            ,max_value=500.0
            ,step=100.0
            )
        with tab2:
            s11=st.number_input(
            'Melting point of molten salt 3(℃)'
            ,min_value=200.0
            ,max_value=1800.0
            ,step=100.0
            )
            s12=st.number_input(
            'Boiling point of molten salt 3(℃)'
            ,min_value=100.0
            ,max_value=3000.0
            ,step=100.0
            )
            s14=st.number_input(
            'Heat of fusion of molten salt 3(J/g)'
            ,min_value=30.0
            ,max_value=1200.0
            ,step=100.0
            )
        with tab3:
            s2=st.number_input(
            'Complexity of molten salt 3'
            ,min_value=0.0
            ,max_value=100.0
            ,step=10.0
            )
            s7=st.number_input(
            'Crystal volume of molten salt 3(Å³)'
            ,min_value=20.0
            ,max_value=1500.0
            ,step=50.0
            )
            s8=st.number_input(
            'Number of atoms of molten salt 3'
            ,min_value=0
            ,max_value=100
            ,step=10
            )
            s9=st.number_input(
            'Cationic radius of molten salt 3(nm)'
            ,min_value=0.0
            ,max_value=0.2
            ,step=0.05
            )
            s10=st.number_input(
            'Anion radius of molten salt 3(nm)'
            ,min_value=0.0
            ,max_value=0.5
            ,step=0.05
            )
            s16=st.number_input(
            'Cation valence state of molten salt 3'
            ,min_value=1
            ,max_value=5
            ,step=1
            )
        with tab4:
            s1=st.number_input(
            'Topological polar surface area of molten salt 3(Å²)'
            ,min_value=0.0
            ,max_value=200.0
            ,step=10.0
            )
            s3=st.number_input(
            'Covalently-bonded unit count of molten salt 3'
            ,min_value=0
            ,max_value=10
            ,step=1
            )
            s4=st.number_input(
            'Band gap of molten salt 3(eV)'
            ,min_value=0.0
            ,max_value=10.0
            ,step=0.1
            )
            s5=st.number_input(
            'Predicted formation energy of molten salt 3(eV/atom)'
            ,min_value=-10.0
            ,max_value=10.0
            ,step=1.0
            )
            s6=st.number_input(
            'Energy above hull of molten salt 3(eV/atom)'
            ,min_value=0.0
            ,max_value=5.0
            ,step=1.0
            )
          
   
    
    st.markdown('##### _Content --- The following are the contents of each component of phase change materials._')
    col4, col5, col6 = st.columns(3)
    values_1 = col4.slider(
        'Molten salt 1 content'
        ,min_value=0.0
        ,max_value=1.0
        ,value=0.54
    )
    values_2 = col5.slider(
        'Molten salt 2 content'
        ,min_value=0.0
        ,max_value=1.0
        ,value=0.36
    )
    values_3 = col6.slider(
        'Molten salt 3 content'
        ,min_value=0.0
        ,max_value=1.0
        ,value=0.00
    )
    
    yes = st.checkbox('**:red[If you manually input features, please check it, otherwise an error will be reported!]**')
    if yes:
    #热导率归一化    
        t1 = values_1 * y1 + values_2 * e1 + values_3 * s1-1
        t2 = (values_1 * y2 + values_2 * e2 + values_3 * s2)/62.2
        t3 = values_1 * y3 + values_2 * e3 + values_3 * s3-2
        t4 = (values_1 * y4 + values_2 * e4 + values_3 * s4)/7.47
        t5 = (values_1 * y5 + values_2 * e5 + values_3 * s5 + 4.189)/6.451
        t6 = (values_1 * y6 + values_2 * e6 + values_3 * s6)/2.161
        t7 = (values_1 * y7 + values_2 * e7 + values_3 * s7 -38.29)/988.48
        t8 = (values_1 * y8 + values_2 * e8 + values_3 * s8-2)/58
        t9 = (values_1 * y9 + values_2 * e9 + values_3 * s9-0.072)/0.095
        t10 =(values_1 * y10 + values_2 * e10 + values_3 * s10-0.133)/0.147
        t11 = (values_1 * y11 + values_2 * e11 + values_3 * s11-253)/1427
        t12 = (values_1 * y12 + values_2 * e12 + values_3 * s12-132)/2768
        t13 = (values_1 * y13 + values_2 * e13 + values_3 * s13-1.98)/3.17
        t14 = (values_1 * y14 + values_2 * e14 + values_3 * s14-31)/1010
        t15 = (values_1 * y15+ values_2 * e15 + values_3 * s15-25.939)/365.197
        t16 = values_1 * y16 + values_2 * e16 + values_3 * s16-1
    #熔点标准化    
        f1 = (values_1 * y1 + values_2 * e1 + values_3 * s1-38.18)/31.86
        f2 = (values_1 * y2 + values_2 * e2 + values_3 * s2-13.35)/12.03
        f3 = (values_1 * y3 + values_2 * e3 + values_3 * s3-2.22)/0.48
        f4 = (values_1 * y4 + values_2 * e4 + values_3 * s4-3.57)/1.44
        f5 = (values_1 * y5 + values_2 * e5 + values_3 * s5 + 1.65)/0.82
        f6 = (values_1 * y6 + values_2 * e6 + values_3 * s6-0.17)/0.39
        f7 = (values_1 * y7 + values_2 * e7 + values_3 * s7 -229.95)/125.25
        f8 = (values_1 * y8 + values_2 * e8 + values_3 * s8-15.83)/9.25
        f9 = (values_1 * y9 + values_2 * e9 + values_3 * s9-0.10)/0.02
        f10 =(values_1 * y10 + values_2 * e10 + values_3 * s10-0.17)/0.03
        f11 = (values_1 * y11 + values_2 * e11 + values_3 * s11-592.19)/280.63
        f12 = (values_1 * y12 + values_2 * e12 + values_3 * s12-919.21)/565.81
        f13 = (values_1 * y13 + values_2 * e13 + values_3 * s13-2.32)/0.59
        f14 = (values_1 * y14 + values_2 * e14 + values_3 * s14-287.13)/193.19
        f15 = (values_1 * y15+ values_2 * e15 + values_3 * s15-95.04)/47.87
        f16 = (values_1 * y16 + values_2 * e16 + values_3 * s16-1.13)/0.34
    #熔化热标准化
        g1 = (values_1 * y1 + values_2 * e1 + values_3 * s1-41.07)/29.95
        g2 = (values_1 * y2 + values_2 * e2 + values_3 * s2-14.09)/11.24
        g3 = (values_1 * y3 + values_2 * e3 + values_3 * s3-2.16)/0.51
        g4 = (values_1 * y4 + values_2 * e4 + values_3 * s4-3.39)/1.41
        g5 = (values_1 * y5 + values_2 * e5 + values_3 * s5 + 1.58)/0.81
        g6 = (values_1 * y6 + values_2 * e6 + values_3 * s6-1.17)/0.4
        g7 = (values_1 * y7 + values_2 * e7 + values_3 * s7 -235.22)/121.75
        g8 = (values_1 * y8 + values_2 * e8 + values_3 * s8-16.53)/8.94
        g9 = (values_1 * y9 + values_2 * e9 + values_3 * s9-0.1)/0.02
        g10 =(values_1 * y10 + values_2 * e10 + values_3 * s10-0.17)/0.03
        g11 = (values_1 * y11 + values_2 * e11 + values_3 * s11-555.36)/287.49
        g12 = (values_1 * y12 + values_2 * e12 + values_3 * s12-837.2)/559.07
        g13 = (values_1 * y13 + values_2 * e13 + values_3 * s13-2.27)/0.59
        g14 = (values_1 * y14 + values_2 * e14 + values_3 * s14-262.26)/183.23
        g15 = (values_1 * y15+ values_2 * e15 + values_3 * s15-93.61)/46.19
        g16 = (values_1 * y16 + values_2 * e16 + values_3 * s16-1.09)/0.34
           
    else:
     #热导率归一化 
        t1 = values_1 * tpsa_1 + values_2 * tpsa_2 + values_3 * tpsa_3-1
        t2 = (values_1 * c_1 + values_2 * c_2 + values_3 * c_3)/62.2
        t3 = values_1 * cb_1 + values_2 * cb_2 + values_3 * cb_3-2
        t4 = (values_1 * bg_1 + values_2 * bg_2 + values_3 * bg_3)/7.47
        t5 = (values_1 * pfe_1 + values_2 * pfe_2 + values_3 * pfe_3+ 4.189)/6.451
        t6 = (values_1 * eah_1 + values_2 * eah_2 + values_3 * eah_3)/2.161
        t7 = (values_1 * cv_1 + values_2 * cv_2 + values_3 * cv_3-38.29)/988.48
        t8 = (values_1 * noa_1 + values_2 * noa_2 + values_3 * noa_3-2)/58
        t9 = (values_1 * cr_1 + values_2 * cr_2 + values_3 * cr_3-0.072)/0.095
        t10 =(values_1 * ar_1 + values_2 * ar_2 + values_3 * ar_3-0.133)/0.147
        t11 = (values_1 * mp_1 + values_2 * mp_2 + values_3 * mp_3-253)/1427
        t12 = (values_1 * bp_1 + values_2 * bp_2 + values_3 * bp_3-132)/2768
        t13 = (values_1 * d_1 + values_2 * d_2 + values_3 * d_3-1.98)/3.17
        t14 = (values_1 * hof_1 + values_2 * hof_2 + values_3 * hof_3-31)/1010
        t15 = (values_1 * mw_1 + values_2 * mw_2 + values_3 * mw_3-25.939)/365.197
        t16 = values_1 * cvs_1 + values_2 * cvs_2 + values_3 * cv_3-1
      #熔点标准化  
        f1 = (values_1 * tpsa_1 + values_2 * tpsa_2 + values_3 * tpsa_3-38.18)/31.86
        f2 = (values_1 * c_1 + values_2 * c_2 + values_3 * c_3-13.35)/12.03
        f3 = (values_1 * cb_1 + values_2 * cb_2 + values_3 * cb_3-2.22)/0.48
        f4 = (values_1 * bg_1 + values_2 * bg_2 + values_3 * bg_3-3.57)/1.44
        f5 = (values_1 * pfe_1 + values_2 * pfe_2 + values_3 * pfe_3 + 1.65)/0.82
        f6 = (values_1 * eah_1 + values_2 * eah_2 + values_3 * eah_3-0.17)/0.39
        f7 = (values_1 * cv_1 + values_2 * cv_2 + values_3 * cv_3 -229.95)/125.25
        f8 = (values_1 * noa_1 + values_2 * noa_2 + values_3 * noa_3-15.83)/9.25
        f9 = (values_1 * cr_1 + values_2 * cr_2 + values_3 * cr_3-0.10)/0.02
        f10 =(values_1 * ar_1 + values_2 * ar_2 + values_3 * ar_3-0.17)/0.03
        f11 = (values_1 * mp_1 + values_2 * mp_2 + values_3 * mp_3-592.19)/280.63
        f12 = (values_1 * bp_1 + values_2 * bp_2 + values_3 * bp_3-919.21)/565.81
        f13 = (values_1 * d_1 + values_2 * d_2 + values_3 * d_3-2.32)/0.59
        f14 = (values_1 * hof_1 + values_2 * hof_2 + values_3 * hof_3-287.13)/193.19
        f15 = (values_1 * mw_1 + values_2 * mw_2 + values_3 * mw_3-95.04)/47.87
        f16 = (values_1 * cvs_1 + values_2 * cvs_2 + values_3 * cv_3-1.13)/0.34
      #熔化热标准化  
        g1 = (values_1 * tpsa_1 + values_2 * tpsa_2 + values_3 * tpsa_3-41.07)/29.95
        g2 = (values_1 * c_1 + values_2 * c_2 + values_3 * c_3-14.09)/11.24
        g3 = (values_1 * cb_1 + values_2 * cb_2 + values_3 * cb_3-2.16)/0.51
        g4 = (values_1 * bg_1 + values_2 * bg_2 + values_3 * bg_3-3.39)/1.41
        g5 = (values_1 * pfe_1 + values_2 * pfe_2 + values_3 * pfe_3 + 1.58)/0.81
        g6 = (values_1 * eah_1 + values_2 * eah_2 + values_3 * eah_3-1.17)/0.4
        g7 = (values_1 * cv_1 + values_2 * cv_2 + values_3 * cv_3 -235.22)/121.75
        g8 = (values_1 * noa_1 + values_2 * noa_2 + values_3 * noa_3-16.53)/8.94
        g9 = (values_1 * cr_1 + values_2 * cr_2 + values_3 * cr_3-0.1)/0.02
        g10 =(values_1 * ar_1 + values_2 * ar_2 + values_3 * ar_3-0.17)/0.03
        g11 = (values_1 * mp_1 + values_2 * mp_2 + values_3 * mp_3-555.36)/287.49
        g12 = (values_1 * bp_1 + values_2 * bp_2 + values_3 * bp_3-837.2)/559.07
        g13 = (values_1 * d_1 + values_2 * d_2 + values_3 * d_3-2.27)/0.59
        g14 = (values_1 * hof_1 + values_2 * hof_2 + values_3 * hof_3-262.26)/183.23
        g15 = (values_1 * mw_1 + values_2 * mw_2 + values_3 * mw_3-93.61)/46.19
        g16 = (values_1 * cvs_1 + values_2 * cvs_2 + values_3 * cv_3-1.09)/0.34
    st.divider()
    
    st.markdown('### Support material')
    col10, col11 = st.columns(2)
    values_4 = col10.slider(
        '**EG content**'
        ,min_value=0.0
        ,max_value=1.0
        ,value=0.1
    )
    tcEG = col11.number_input(
      '**Thermal conductivity of EG**'
        ,min_value=0.00
        ,max_value=9.00
        ,value=7.91
        ,step=0.05
    )
    
    col7, col8, col9 = st.columns(3)
    nm = col7.number_input(
        '**Number of EG mesh**'
        ,min_value=0
        ,max_value=100
        ,value=80
        ,step=10
    )
    sa = col8.number_input(
        '**EG aperture(μm)**'
        ,min_value=0.0
        ,max_value=1500.0
        ,value=187.5
        ,step=100.0
    )
    er = col9.number_input(
        '**Expansion rate of EG(ml/g)**'
        ,min_value=0
        ,max_value=400
        ,value=300
        ,step=100
    )
    
    
    if values_1 + values_2 + values_3 + values_4 !=1:
        st.error('Please check if the input of molten salt and supporting material content is correct, and ensure that the sum is 1.0!')
    st.divider()
    
    
    st.markdown('### Mixing process')
    T = st.number_input(
        '**Mixed heating temperature(℃)**'
        ,min_value=0
        ,max_value=800
        ,value=0
        ,step=100
    )
    t =st.number_input(
        '**Heating time(h)**'
        ,min_value=0.0
        ,max_value=24.0
        ,value=0.0
        ,step=5.0
    ) 
    st.divider()
    
    
    #热导率归一化 
    t17 = values_4*100/60
    t18 = (nm-32)/68
    t19 = (sa-150)/123
    t20 = (er-150)/150
    t21 = tcEG/16.7
    t22 = T/120
    t23 = (t-0.5)/23.5
    #熔点标准化
    f17 = (values_4*100-4.45)/9.07
    f18 = (nm-27.1)/64.91
    f19 = (sa-63.15)/108.08
    f20 = (er-63.25)/111.1
    f21 = (tcEG-2.09)/3.5
    f22 = (T-70.24)/173.65
    f23 = (t-0.73)/2.97
    #熔化热标准化
    g17 = (values_4*100-5.75)/10.87
    g18 = (nm-28.22)/53.04
    g19 = (sa-65.5)/105.57
    g20 = (er-67.77)/112.44
    g21 = (tcEG-2.27)/3.55
    g22 = (T-57.49)/154.52
    g23 = (t-0.63)/2.84
          
    if st.button("Start Prediction"):
        ETR_1 = joblib.load("ETR_1.pkl")
        ETR_2 = joblib.load("ETR_2.pkl")
        ETR_3 = joblib.load("ETR_3.pkl")

        
        X1 = pd.DataFrame(
             [[f1,f3,f4,f5,f6,f8,f9,f11,f12,f13,f14,f16]]
              ,columns = ['TPSA of PCM, Å²','CBUC of PCM','BG of PCM, eV','FE of PCM, eV/atom','Ehull of PCM, eV/atom','AN of PCM','CR of PCM, nm'
                         ,'MP of PCM, ℃','BP of PCM, ℃','D of PCM, g/cm³','HoF of PCM, J/g','CVS of PCM']
        )
        prediction_1 = np.exp(ETR_1.predict(X1)[0])
        
        
        X2 = pd.DataFrame(
             [[g4,g5,g6,g7,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18]]
            ,columns = ['BG of PCM, eV','FE of PCM, eV/atom','Ehull of PCM, eV/atom','CV of PCM, Å³','CR of PCM, nm','AR of PCM, nm',
                        'MP of PCM, ℃','BP of PCM, ℃','D of PCM, g/cm³','HoF of PCM, J/g','MW of PCM, g/mol','CVS of PCM','SMC, %','No. of SMM']
        )
        prediction_2 = np.exp(ETR_2.predict(X2)[0])
        
        
        X3 = pd.DataFrame(
            [[t4,t5,t6,t9,t10,t14,t17,t19,t20,t21,t22,t23]]
            ,columns = ['BG of PCM, eV','FE of PCM, eV/atom','Ehull of PCM, eV/atom','CR of PCM, nm','AR of PCM, nm'
                        ,'HoF of PCM, J/g','SMC, %','SMA, μm','ER of SM, ml/g','TC of SM, W/(m·K)','T, ℃','t, h']
        )
        prediction_3 = np.exp(ETR_3.predict(X3)[0])
        
        
        c1, c2 ,c3= st.columns(3)
        plt.rcParams["font.sans-serif"]=["SimHei"]
        plt.rcParams['axes.unicode_minus'] = False
        d=pd.read_excel('data.xlsx')
        sns.displot(
            d
            ,x='mp'
            ,kind='kde'
            ,fill=True
        )
        plt.axvline(
            x=prediction_1
            ,color='r'
        )
        plt.xlabel('Melting point, ℃')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        c1.pyplot()
        
        sns.displot(
            d
            ,x='hf'
            ,kind='kde'
            ,fill=True
        )
        plt.axvline(
            x=prediction_2
            ,color='r'
        )
        plt.xlabel('Heat of fusion, J/g')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        c2.pyplot()
       
        sns.displot(
            d
            ,x='tc'
            ,kind='kde'
            ,fill=True
        )
        plt.axvline(
            x=prediction_3
            ,color='r'
        )
        plt.xlabel('Thermal conductivity, W/(m·K)')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        c3.pyplot()
        
        st.markdown(f"#### The predicted results are as follows:\n\n- Melting point: **:green[{'%.2f'%prediction_1}]** ℃\n- Heat of husion: **:green[{'%.2f'%prediction_2}]** J/g\n- Thermal conductivity: **:green[{'%.2f'%prediction_3}]** W/(m·K)")
        
