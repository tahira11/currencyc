import streamlit as st
from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Streamlit App Title
st.title("💸 Currency Converter")

# App subtitle
st.markdown("### Convert currencies easily with real-time rates 🌍💱")

# Sidebar configuration for user input
st.sidebar.header("Currency Converter Settings")

# Input from user: Amount, From Currency, To Currency
amount = st.sidebar.number_input("Enter amount", min_value=0.0, value=100.0)
from_currency = st.sidebar.text_input("From Currency (e.g., USD)", value="USD").upper()
to_currency = st.sidebar.text_input("To Currency (e.g., EUR)", value="EUR").upper()

# Currency conversion logic
if st.sidebar.button("Convert"):
    try:
        # Get the conversion rate
        conversion_rate = c.get_rate(from_currency, to_currency)
        converted_amount = conversion_rate * amount

        # Displaying the result
        st.success(f"💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        st.write(f"Exchange Rate: 1 {from_currency} = {conversion_rate:.4f} {to_currency}")

    except Exception as e:
        st.error(f"Error: {str(e)}")
