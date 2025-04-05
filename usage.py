import streamlit as st



def app():
    st.sidebar.info('Please carefully review the usage instructions!')
    st.title('Users Guide')
    st.divider()
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['#### Step :one:', "#### Step :two:", "#### Step :three:", '#### Step :four:', '#### Step :five:', '#### Step :six:'])
    with tab1:
        #st.markdown('#### 1. After logging in, select :blue[PCM-TP Predictor] to enter the prediction interface.')
        st.markdown('#### 1. Firstly, log in and enter your username and password. If you do not have an account, click on the dropdown menu at the top of the page and select "Register".')
        st.image(
            'Usage 1.png'
            ,width=900
        )
    
    with tab2:
        st.markdown('#### 2. Select the corresponding molten salts for the composite phase change material from the dropdown menu (up to three types). If the desired salt is not available in the dropdown menu, enter the relevant properties of the new salt in the input box below. Note: Please refer to the website provided in the sidebar to access information about salt properties.')
        st.image(
            'Usage 2.jpg'
            ,width=900
        )
        
    with tab3:
        st.markdown('#### 3. Use the slider to adjust the content of each salt.')
        st.image(
            'Usage 3.png'
            ,width=900
        )
    with tab4:
        st.markdown('#### 4. Enter the structural parameters of expanded graphite (EG), including layer number, pore size, and volume expansion rate, in the input field. Also, use the slider to select the content of EG in the composite phase change material.')
        st.image(
            'Usage 4.png'
            ,width=900
        )
    with tab5:
        st.markdown('#### 5. Enter the processing parameters, including mixed heating temperature and heating time, in the input field.')
        st.image(
            'Usage 5.png'
            ,width=900
        )
    with tab6:
        st.markdown('#### 6. Click the "Start Prediction" button to initiate the prediction process and obtain the predicted results.')
        st.image(
            'Usage 6.png'
            ,width=900
        )
      

