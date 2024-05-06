import streamlit as st 
from streamlit_option_menu import option_menu

main_title = 'AI Interviewer'
main_introduction = 'Welcom to AI Interviewer'
with st.sidebar: 
    st.markdown('AI Interviewer')
    st.markdown('''
    This is guidline ~~ 
                ''')
    st.markdown(f"""# {main_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")


selected = option_menu(
    menu_title = 'AI Interview',
    options = ['Professional', 'Resume', 'Behavioral', 'Customize'],
    icons = ['cast', 'cloud-upload', 'cast'],
    default_index = 0,
    orientation = 'horizontal',
)

if selected == 'Professional':
    st.info('dd')
    if st.button('Start Interview!'):
        st.write('Loading the interview page...')

elif selected == 'Resume':
    st.info('dd')
    if st.button('Start Experiment!'):
        st.write('Loading the experiment page...')

elif selected == 'Behavioral':
    st.info('dd')
    if st.button('Start Interview!'):
        st.write('Loading the interview page...')

elif selected == 'Customize':
    st.info('dd')
    if st.button('Strat Customize!'):
        st.write('Loading the Customize page...')