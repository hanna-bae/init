import streamlit as st 

# button 
if st.button('Click button'):
    st.write('Data Loading ..')
    # Data loading function 

# checkbox 
checkboxb = st.checkbox('Checkbox Button')
# if you want to check the default
# st.checkbox('Checkbox Button', value=True)
if checkboxb:
    st.write('Check !')

# radio button
selected_item = st.radio('Radio Part', ("1", "2", "3"))
if selected_item == '1':
    st.write('First!')
elif selected_item == '2':
    st.write('Second!')
elif selected_item == '3':
    st.write('Third!')
    