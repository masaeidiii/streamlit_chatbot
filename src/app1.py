import streamlit as st
import utils
st.title('OFFLINE CHATBOT')

#prompt =  st.chat_input('Enter your question')

#==========================

#msg= st.chat_message('user').write('who is messi')
#msg= st.chat_message('ai').write('who is messi')

#==========================
#count = 1
#if st.button('add'):
    #count +=1
    #st.write(f"count:{count}") #just one time work


#==========================

#st.write(st.session_state)
#st.session_state["count"] = 0 

#if st.button('add'):
    #st.session_state['count'] += 1 
    #st.write(f"count:{st.session_state['count']}") # for seeing history of my speach with ai 

    #==========================

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai', 'content':'How Can I Help YOU?'}]

for msg in st.session_state['messages']:# for history
    st.chat_message(msg['role']).write(msg['content'])

model = 'qwen2.5-coder:7b'
prompt = st.chat_input('Ask Your Question')
if prompt:

    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user', 'content':prompt})

    with st.spinner('Generatintg Awnser...'):
        response = utils.call_ollama_model(prompt, model) #just for beauty 
    
    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai', 'content':response})