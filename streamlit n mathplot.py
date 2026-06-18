import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Future Value & Interest Calculator")
st.write("See how your money grows over time with compound interest!")

st.sidebar.header("Investment Settings")

principal = st.sidebar.number_input("Initial Deposit ($)", min_value=0.0, value=1000.0, step=100.0)

interest_rate = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.5)

years = st.sidebar.slider("Investment Timeline (Years)", min_value=1, max_value=40, value=10)

rate = interest_rate / 100

years_range = np.arange(0, years + 1)
balances = [principal * ((1 + rate) ** t) for t in years_range]

future_value = balances[-1]
total_interest = future_value - principal

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Future Value", value=f"${future_value:,.2f}")
with col2:
    st.metric(label="Total Interest Earned", value=f"${total_interest:,.2f}")

st.write("---")

st.subheader("Growth Over Time")

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(years_range, balances, color="#2ecc71", edgecolor="#27ae60", alpha=0.8, label="Total Balance")

ax.set_title("Year-by-Year Account Balance", fontsize=14, fontweight='bold')
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Amount ($)", fontsize=12)
ax.set_xticks(years_range if years <= 15 else np.arange(0, years + 1, 5)) # keep x-axis clean if years are high
ax.grid(axis='y', linestyle='--', alpha=0.5)

ax.text(years, future_value, f"  ${future_value:,.0f}", va='center', ha='left', fontweight='bold', color='#27ae60')

st.pyplot(fig)

