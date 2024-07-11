import streamlit as st

# Define BOP categories and explanations
def get_bop_glossary():
    return {
        "D Overall Balance (A-B+C)": "This represents the net flow of transactions, summarizing the balance of the current account and the capital & financial account, adjusted for net errors and omissions.",
        "A Current Account Balance": "This measures the difference between a country's savings and its investment, representing the balance of trade, net primary income, and net cash transfers.",
        "B Capital & Financial Account Balance": "This shows the net change in ownership of national assets, including foreign investments and loans.",
        "C Net Errors & Omissions": "This is a balancing item to account for any discrepancies or unrecorded transactions in the balance of payments."
    }

# Define main CPI categories with descriptions
def get_cpi_categories():
    return {
        "Food": "Includes items such as bread, rice, meat, fish, milk, cheese, eggs, oils, fats, fruits, and vegetables.",
        "Food Excl Food Serving Services": "Includes food items consumed at home, such as cereals, meat, fish, dairy products, fruits, and vegetables.",
        "Food Serving Services": "Includes food items consumed away from home, such as in restaurants, fast food outlets, hawker centers, and catered food.",
        "Clothing & Footwear": "Includes men's, women's, and children's clothing and footwear, as well as other articles and related services.",
        "Health Care": "Includes medicines, health products, outpatient services, hospital services, and health insurance.",
        "Transport": "Includes private and public transport, as well as other transport services like airfares.",
        "Communication": "Includes postage, courier services, telecommunication equipment, and telecommunication services.",
        "Recreation & Culture": "Includes recreational and cultural goods and services, newspapers, books, stationery, and holiday expenses.",
        "Education": "Includes tuition and other fees, as well as textbooks and study guides.",
        "Miscellaneous Goods & Services": "Includes personal care items, alcoholic drinks, tobacco, personal effects, social services, and other miscellaneous services."
    }

# Glossary page content
st.title("Glossary of Terms 📔")

# BOP Section
st.header("Balance of Payments (BOP) Categories")
bop_glossary = get_bop_glossary()
for category, description in bop_glossary.items():
    st.subheader(category)
    st.write(description)

# CPI Section
st.header("Consumer Price Index (CPI) Main Categories")
cpi_categories = get_cpi_categories()
for category, description in cpi_categories.items():
    st.subheader(category)
    st.write(description)
