import streamlit as st
from tipi import calculate_scores
import json

def submit_survey():
    st.session_state["survey_completed"] = True
    st.session_state["tipi_scores"] = calculate_scores(st.session_state["survey"])
    st.session_state["page"] = "chat"

def survey():
    if "survey" not in st.session_state:
        st.session_state["survey"] = {}

    file_path = "questionarre/deutsch_questionarre_slider.json"

    st.title("Umfrage")

   # st.markdown("Bitte geben Sie Ihre ID ein")
   # name = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))

    questions = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            questions = json.load(file)  # Read JSON file
    except FileNotFoundError:
        st.error("❌ Die Datei wurde nicht gefunden. Bitte überprüfen Sie den Pfad.")
        return 
    except json.JSONDecodeError:
        st.error("❌ Fehler beim Laden der JSON-Datei. Bitte überprüfen Sie das Format.")
        return

    # Store responses
    if "responses" not in st.session_state:
        st.session_state["survey"]["responses"] = {}

    options_final = [
      "Starke Ablehnung",  "Ablehnung", "Neutral",  "Zustimmung", "Starke Zustimmung"

             ]

    #st.subheader("Fragebogen", divider='gray')
    
    responses= {}
    # with st.form(key="my_form"):
    #     for idx, q in enumerate(questions):
    #         q_key = f"q{idx + 1}"
    #         selected_option = st.select_slider( q["question"], options = options, key= q_key, value = st.session_state["survey"].get(q_key,options[3]))
    #         st.session_state["survey"]["responses"][q_key] = selected_option
    #         st.subheader("",divider='gray')
    #         responses[q_key]=selected_option

    with st.form(key="my_form"):
        name = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))

        st.subheader("",divider='gray')
        # Abfrage nach Hautfarbe
        st.markdown("Lesen Sie bitte jede dieser Aussagen aufmerksam durch und überlegen Sie, ob diese Aussage auf Sie persönlich für die letzten 6 Monate zutrifft oder nicht")

        for idx, q in enumerate(questions):
            q_key = f"q{idx + 1}"
            st.markdown(q["question"])
            selected_option = st.radio( q["question"],  options_final, key= q_key,index=2, label_visibility="collapsed")
            st.session_state["survey"]["responses"][q_key] = selected_option
            st.subheader("",divider='gray')
            responses[q_key]=selected_option

        # Submit button
        submit_button = st.form_submit_button("Absenden")

    if submit_button:
        
        if name == "":
            st.error("Bitte geben Sie Ihre ID ein.")
        
        else:
            st.success("Vielen Dank für Ihre Antworten!")
            st.write("### Ihre Auswahl:")
        

       

            for idx, q in enumerate(questions):
                selected_options = st.session_state["survey"]["responses"].get(f"q{idx}", [])
                st.write(f"**Q{idx}:** {', '.join(selected_options) if selected_options else 'Keine Auswahl'}")

            st.session_state["page"] = "chat"
            print('Survey Data: ',st.session_state["survey"] )
            st.rerun()
