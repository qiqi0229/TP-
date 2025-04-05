import streamlit as st

def app():
    st.title('Authors')
    st.divider()
    
    st.markdown('#### Please feel free to contact us with any issues, comments, or questions.')
    
    col1, col2, col3 = st.columns(3)
    col1.success('##### Fengqi Li\n Email: 1435247956@qq.com')
    col2.success('##### Tingli Liu\n Email: tingliliu@lnu.edu.cn')
    col3.success('##### Xiangdong Zhang\n Email: xdzhang@lnu.edu.cn')