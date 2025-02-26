import streamlit as st
import time
from images import show_images,show_upload_images
from styling import decision_page_styling,image_container_styling
from icecream import ic


def decision():
    # TODO: Format that buttons are "more beautiful"
    IMAGE_WIDTH = 350
    IMAGE_HEIGHT = 200

    if 'button_clicked' not in st.session_state:
        st.session_state["button_clicked"] = None


#st.markdown('<div class="image-column">', unsafe_allow_html=True)

        #image = show_images()
    image_container=st.container()
        
    with image_container:

        
        image=show_upload_images() #new updated upload image module
        resized_image = image.resize((IMAGE_WIDTH,IMAGE_HEIGHT))
        st.image(resized_image, caption="Zufallsbild")




    #st.markdown(set_title_styling(), unsafe_allow_html=True)

    if st.session_state["button_clicked"]:
        print("Button Clicked")
        print(f"You decided for: {st.session_state['button_clicked']}")
        st.write(f"You decided for: {st.session_state['button_clicked']}")
        time.sleep(1)
        st.session_state["page"] = "thanks"
        # had to add rerun() to make the page change. Otherwise it only worked after clicking a button twice -> TODO: find out why and fix
        st.experimental_rerun()



