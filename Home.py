import streamlit as st

# .... set webpage a wide display .....
st.set_page_config(page_title='Home', page_icon='tada:', layout="wide")
# ...... sidebar success .......
#st.sidebar.success("Select a simulation above.")


# Header
st.header("My Streamlit App")

# Create a layout with two columns
col1, col2 = st.columns(2)

# Content for the first column
with col1:
    st.subheader("Column 1")
    st.write("Content for the first column goes here.")

# Content for the second column
with col2:
    st.subheader("Column 2")
    st.write("Content for the second column goes here.")




#..... Header .......
#st.header('Hello, I am Youti Franklin Wan :wave:', divider='rainbow')
#st.markdown(
    """
   coming soon
"""
#)


