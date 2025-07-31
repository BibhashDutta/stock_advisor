import streamlit as st
from data_fetcher import fetch_market_data, format_data_as_text
from gpt_advisory import get_advice_from_gpt
import time

# 🔁 Set auto-refresh interval (in seconds)
AUTO_REFRESH_INTERVAL = 30

# Inject JavaScript to refresh the page after n seconds
def auto_refresh(interval_sec=30):
    refresh_code = f"""
        <script>
            function autoRefresh() {{
                window.location.reload();
            }}
            setTimeout(autoRefresh, {interval_sec * 1000});
        </script>
    """
    st.components.v1.html(refresh_code, height=0)

auto_refresh(AUTO_REFRESH_INTERVAL)

st.title("📈 AI Stock Advisor - NIFTY/SENSEX")

# Fetch simulated real-time data
df = fetch_market_data()
st.subheader("🔍 Market Data (First Hour)")
st.dataframe(df.style.format({
    "Opening Price": "{:.2f}",
    "Current Price": "{:.2f}",
    "Volume": "{:,}"
}))

# Format for GPT input
formatted_data = format_data_as_text(df)

# Button to get GPT advice
if st.button("💡 Get Stock Advice from GPT"):
    with st.spinner("Analyzing..."):
        advice = get_advice_from_gpt(formatted_data)
    st.subheader("🧠 GPT Stock Advice")
    st.markdown(advice)
