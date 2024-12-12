import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Power BI Dashboard Integration", layout="wide")

# Title of the Streamlit app
st.title("Stock market analysis 2023 - 2024")

# Power BI Embed
st.subheader("Dashboard")
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYmNhOTljZGQtNTk4MC00ZjU5LTgyMjQtM2Y1YTY2YjViZTk3IiwidCI6IjBhNjM5NzcwLTA3YWItNGJlMy1hNWY4LTNkN2Y5YjU1YjJkNiJ9"  # Replace with your embed URL

# Embed Power BI report in an iframe
st.markdown(f"""
    <iframe title="Power BI Report" width="100%" height="550" 
    src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

# Additional interactivity (optional visualization using Streamlit)
st.subheader("Additional Insights")
st.write("page 1: overall market information like average price , average volume. You have top 10 volatile stock, top 10 stock over the year, top 5 best return stocks of the year and sector wise performance.")
st.write("page 2: Top 10 gainers and losers of the year")
st.write("page 3: Top 5 gainers and losers month wise. select the month to see the top 5 gainers and losers of that month")
