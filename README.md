# Population Dynamics Simulator (SIR Model)

## Overview
This project is an interactive web application that simulates the spread of an infectious disease or genetic trait through a population over time. By numerically solving the ordinary differential equations (ODEs) of the SIR (Susceptible, Infected, Recovered) compartmental model, it provides a real-time visualization of population dynamics.

This repository serves as a practical demonstration of translating theoretical dynamical systems into visual tools, making it an excellent addition to your CV Projects.

## Features
- **Interactive Dashboard:** Built with Streamlit for a seamless, user-friendly experience.
- **Real-Time Simulation:** Adjust parameters like the Transmission Rate (beta) and Recovery Rate (gamma) to instantly see how the epidemiological curves flatten or spike.
- **Dynamic R0 Calculation:** Automatically computes the Basic Reproduction Number (R0) and provides public health context (whether the outbreak is expanding or under control).
- **Rigorous Mathematical Backend:** Uses `scipy.integrate.odeint` to accurately solve the underlying differential equations.
- **High-Quality Visualization:** Leverages Plotly for interactive, hoverable charts.

## Installation
To run this project locally, you need Python installed on your system. 

1. Clone this repository or download the source code.
2. Install the required dependencies using pip:

```bash
pip install streamlit numpy scipy plotly
```

## Usage
Navigate to the directory containing the `app.py` file in your terminal, and run the following command:

```bash
streamlit run app.py
```
This will start a local server and automatically open the application in your default web browser.

## Mathematical Background
The simulation is based on the classic SIR compartmental model, dividing a constant population into three distinct states:
- **Susceptible (S):** Individuals who are healthy but can contract the disease.
- **Infected (I):** Individuals who are currently infected and can transmit the pathogen.
- **Recovered (R):** Individuals who have recovered and acquired immunity (or are otherwise removed from the transmission chain).

The flow between these compartments is governed by the following system of ODEs:
* dS/dt = -beta * S * I / N
* dI/dt = (beta * S * I / N) - (gamma * I)
* dR/dt = gamma * I

## References
* Kermack, W. O., & McKendrick, A. G. (1927). *A Contribution to the Mathematical Theory of Epidemics*. Proceedings of the Royal Society of London.
* Murray, J. D. (2002). *Mathematical Biology I: An Introduction*. Springer.
