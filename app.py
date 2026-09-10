import streamlit as st
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

# 1. Mathematical Function (Backend)
def sir_model(y, t, N, beta, gamma):
    """
    Function that calculates the derivatives of S, I, R at a given time t.
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# 2. Interface Configuration (Frontend)
st.title("Population Dynamics Simulator (SIR Model)")
st.sidebar.header("Pathogen Parameters")

# Interactive controls in the sidebar
beta = st.sidebar.slider("Transmission Rate (beta)", 0.0, 1.0, 0.3)
gamma = st.sidebar.slider("Recovery Rate (gamma)", 0.0, 1.0, 0.1)
days = st.sidebar.slider("Simulation Days", 10, 365, 160)

# Dynamic calculation of the basic reproduction number (R0)
R0 = beta / gamma if gamma > 0 else float('inf')

# Visual separator in the sidebar
st.sidebar.markdown("---")

# Display the metric with a clean format
st.sidebar.metric(label="Basic Reproduction Number (R0)", value=f"{R0:.2f}")

# Add public health context based on R0
if R0 > 1:
    st.sidebar.warning("The outbreak is expanding (R0 > 1)")
else:
    st.sidebar.success("The disease is under control (R0 < 1)")

# 3. Numerical Resolution
N = 1000
y0 = (N - 1, 1, 0) # 999 Susceptible, 1 Infected, 0 Recovered
t = np.linspace(0, days, days)

# odeint integrates the ODE system
result = odeint(sir_model, y0, t, args=(N, beta, gamma))
S, I, R = result.T

# 4. Interactive Visualization
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=S, mode='lines', name='Susceptible', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infected', line=dict(color='red')))
fig.add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recovered', line=dict(color='green')))

fig.update_layout(title="Epidemiological Curves Over Time",
                  xaxis_title="Days",
                  yaxis_title="Number of Individuals")

# Display the chart in Streamlit
st.plotly_chart(fig)
