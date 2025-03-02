import streamlit as st    
from icecream import ic


def create_appointment_bttns(): 
        with st.popover('Möchten Sie einen Termin vereinbaren??',use_container_width=True):
            st.button("Ja", key="btn1",
                            on_click=lambda: st.session_state.update(button_clicked="Termin vereinbaren"),use_container_width=True)
            st.button("Nein", key="btn2",
                            on_click=lambda: st.session_state.update(button_clicked="Do not make appointment"),use_container_width=True)

def get_assistant_response():
    msg = st.session_state.assistant.messages[-1]
    response = st.session_state.assistant.chat(msg["content"])
    return response

def chat_page(): 
    if "messages" not in st.session_state:
        # st.session_state.assistant = XAIAssistant()
        st.session_state.messages = st.session_state.assistant.messages
    st.subheader("Chat mit Assistentin",divider="gray")
    st.markdown("Schildern Sie dem Assistenten Ihre Situation. Sie können auch einen Termin bei unserem Arzt buchen")

    # Display chat messages
    for msg in st.session_state.assistant.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    #create_appointment_bttns()  # Show appointment buttons
        # Chat input box
   
    if prompt:=st.chat_input("Wie kann ich helfen?"):

        a=st.chat_message("user")
        a.write(prompt)

            #Append user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("Bin gleich wieder da..."):
            response = get_assistant_response()  # Get assistant response

            # Append assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})

        b = st.chat_message("assistant")
        b.write(response)
    with st.container():
        if  st.session_state.messages:
            create_appointment_bttns()

        



  