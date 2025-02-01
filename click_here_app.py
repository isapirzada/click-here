import streamlit as st

def main():
    st.set_page_config(page_title="Click Here", page_icon="🔘", layout="centered")
    
    st.markdown("# Click Here")
    
    # Centering the button using markdown and HTML
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Click Here"):
            st.write("You are a Guju")

if __name__ == "__main__":
    main()
