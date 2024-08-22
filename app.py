import streamlit as st

st.title("QUERY SEARCH")

query = st.text_input("Enter your query:")

option = st.selectbox(
    "Choose an option:",
    ("YouTube Query", "Instagram Query", "Facebook Query")
)

# Placeholder for dynamic content
download_placeholder = st.empty()

# Read the content of the CSV file
csv_file_path = "orders .csv"
with open(csv_file_path, "r") as file:
    csv_file = file.read()

with download_placeholder:
    st.write("Sample Processed Data:")
    
    st.download_button(
        label="Download Sample Data as CSV",
        data=csv_file,
        file_name='sample_data.csv',
        mime='text/csv'
    )
