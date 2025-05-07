import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phenol-Water CST Experiment", layout="centered")

st.title("🌡️ Determination of Critical Solution Temperature for Phenol-Water System")

# AIM
st.header("AIM")
st.markdown("To determine the critical solution temperature (CST) for the phenol-water system and to find out the percentage of phenol in the given sample.")

# APPARATUS
st.header("APPARATUS")
st.markdown("Burette, boiling tube, thermometer, water bath, etc.")

# PRINCIPLE
st.header("PRINCIPLE")
st.markdown('''
Phenol and water are partially miscible at ordinary temperatures. On shaking two liquids,
2 saturated solutions of different compositions (phenol in water and water in phenol) are obtained.
With increased temperature, mutual solubility increases until a critical temperature is reached
where they form a homogeneous solution.
''')

# PROCEDURE
st.header("PROCEDURE")
st.markdown('''
1. Add 5 ml of phenol in a boiling tube.
2. Add measured volumes of distilled water.
3. Heat with constant stirring.
4. Record temperature where turbidity disappears.
5. Cool and note when turbidity reappears.
6. Repeat for increasing water volumes.
''')

# OBSERVATIONS
st.header("OBSERVATIONS")

# User input: Number of observations
num_points = st.slider("Select number of observations", min_value=5, max_value=20, value=10, step=1)

# Simulate data
water_volumes = list(range(3, 3 + 2 * num_points, 2))
phenol_volumes = [5] * len(water_volumes)
phenol_percent = [round(5 / (5 + v) * 100, 2) for v in water_volumes]
disappear_temps = np.random.randint(60, 80, size=len(water_volumes))
appear_temps = np.random.randint(55, 75, size=len(water_volumes))

df = pd.DataFrame({
    "Vol. of phenol (ml)": phenol_volumes,
    "Vol. of water (ml)": water_volumes,
    "Vol. % of phenol": phenol_percent,
    "Temp. of disappearance (°C)": disappear_temps,
    "Temp. of appearance (°C)": appear_temps,
})

df["Mean Temp. (°C)"] = df[["Temp. of disappearance (°C)", "Temp. of appearance (°C)"]].mean(axis=1).round(2)

st.dataframe(df)

# MODEL GRAPH
st.header("MODEL GRAPH")
fig, ax = plt.subplots()
ax.plot(df["Vol. % of phenol"], df["Mean Temp. (°C)"], marker='o', color='green')
ax.set_xlabel("Volume % of Phenol")
ax.set_ylabel("Mean Miscibility Temperature (°C)")
ax.set_title("Critical Solution Temperature Graph")
st.pyplot(fig)

# FORMULA
st.header("FORMULA")
st.latex(r"\text{Vol. \% of Phenol} = \frac{5}{5 + V_w} \times 100")

# RESULT
st.header("RESULT")
cst_index = df["Mean Temp. (°C)"].idxmax()
cst_temp = df.loc[cst_index, "Mean Temp. (°C)"]
cst_comp = df.loc[cst_index, "Vol. % of phenol"]

st.markdown(f"**CST of phenol-water system = {cst_temp} °C**")
st.markdown(f"**Critical solution composition = {cst_comp}% phenol by volume**")

# DOWNLOAD
st.header("DOWNLOAD OBSERVATIONS")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", data=csv, file_name='cst_observations.csv', mime='text/csv')
