import streamlit as st 
# Import the required modules for OpenAI and environment variables
from openai import OpenAI
import os 

# Streamlit page configuration 
st.set_page_config(page_title='삼행시 제조기', page_icon=':pencil:')

# OpenAI API key 
# client = OpenAI(
#     api_key = os.environ.get('OPENAI_API_KEY')
# )
# def generate_samhengsi(keyword):
#     try: 
#         # 삼행시 생성 
#         response = client.chat.completions.create(
#                   messages = [
#                       {
#                           'role': 'user',
#                           'content': f"{keyword}로 삼행시를 생성해주세요",
#                       }
#                   ],
#                   model='gpt-3.5-turbo',
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return f'에러가 발생했습니다: {str(e)}'
    
def mock_generate_samhengsi(keyword):
    '''Mock function to simulate poem generation'''
    if len(keyword) != 3:
        raise ValueError('keyword must be 3 characters')
    return [
        f"<span style='background-color:#add8e6; font-weight: bold;'>{keyword[0]}</span> - 부모님의 훈계는 자녀를 귀하게 키운다",
        f"<span style='background-color:#add8e6; font-weight: bold;'>{keyword[1]}</span> - 동화의 나라에서는 부모의 훈계를 듣는 자가 마지막 길 토끼를 만난다",
        f"<span style='background-color:#add8e6; font-weight: bold;'>{keyword[2]}</span> - 산다는 것은 부모가 되는 것이다"
    ]

# Streamlit custom styles (CSS styles)
st.markdown('''
    <style>
    .big-font{
        font-size:50px !important;
        font-weight: bold;
        color: #00800;
        text-align: center;
        margin-bottom: 0px;
    }
    .stTextInput > label {
        font-size: 25px;
        display: block;
    }
    .stTextInput > div > div > input {
        font-size: 20px;
        width: 100%;
    }
    .stButton > button {
        font-size: 20px;
        border-radius: 10px;
        background-color: blue;
        color: white;
        dispaly: block;
        margin: auto;
    }
    </style>
    ''', unsafe_allow_html=True)  
  

# title
st.markdown('<p class="big-font">📝 삼행시 제조기</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">단어를 입력하여 삼행시를 만들어보세요.</p>', unsafe_allow_html=True)
# input the text 
input_keyword = st.text_input('단어 입력 (세 글자)', '',placeholder='예: 부동산')
# enter the button 
if st.button('Generate!'):
    try:
        with st.spinner('Generating...'):
            # generate the 삼행시 
            results = mock_generate_samhengsi(input_keyword)
        # print result
        st.subheader('📜 삼행시 결과')
        for result in results:
            st.markdown("<div style='background-color:#f1f1f1; color:#000000; "
                        "padding: 10px; border-radius: 5px; margin: 5px 0;'>"
                        f"{result}</div>", unsafe_allow_html=True)
    except ValueError as e:
        st.error(str(e))
# Footer 
st.markdown('---')
st.caption('Developed with using Streamlit and OpenAI')