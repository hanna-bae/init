import streamlit as st 
from openai import OpenAI
import os 

# OpenAI API key 
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY')
)
def generate_samhengsi(keyword):
    try: 
        # 삼행시 생성 
        response = client.chat.completions.create(
                  messages = [
                      {
                          'role': 'user',
                          'content': f"{keyword}로 삼행시를 생성해주세요",
                      }
                  ],
                  model='gpt-3.5-turbo',
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f'에러가 발생했습니다: {str(e)}'

# title
st.title('삼행시 제조기')
st.markdown('단어를 입력하여 삼행시를 만들어보세요.')
# input the text 
input_keyword = st.text_input('단어 입력', '')
# enter the button 
if st.button('Generate!'):
    # generate the 삼행시 
    result = generate_samhengsi(input_keyword)
    # print result
    st.subheader('Generate samhengsi completed successfully')
    st.write(result)