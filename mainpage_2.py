import streamlit as st 
import openai 
import os 

# OpenAI API key 
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_samhengsi(keyword):
    try: 
        # 삼행시 생성 
        response = openai.Completion.create(
                  model = 'text-davinci-003',
                  prompt =f'{keyword}에 대한 삼행시를 만들어주세요.',
                  max_tokens = 60
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