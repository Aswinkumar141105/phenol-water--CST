import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phenol-Water CST Experiment", layout="centered")

st.title("🌡️ Determination of Critical Solution Temperature for Phenol-Water System")

# A. AIM
st.header("AIM")
st.markdown("To determine the critical solution temperature (CST) for the phenol-water system and to find out the percentage of phenol in the given sample.")

# B. APPARATUS
st.header("APPARATUS")
st.markdown("Burette, boiling tube, thermometer, water bath, etc.")

# C. PRINCIPLE
st.header("PRINCIPLE")
st.markdown('''
Phenol and water are partially miscible at ordinary temperatures. On shaking two liquids,
2 saturated solutions of different compositions (phenol in water and water in phenol) are obtained.
With increased temperature, mutual solubility increases until a critical temperature is reached
where they form a homogeneous solution.
''')

# D. PROCEDURE
st.header("PROCEDURE")
st.markdown('''
1. Add 5 ml of phenol in a boiling tube.
2. Add measured volumes of distilled water.
3. Heat with constant stirring.
4. Record temperature where turbidity disappears.
5. Cool and note when turbidity reappears.
6. Repeat for increasing water volumes.
''')

# E. OBSERVATIONS
st.header("OBSERVATIONS")

# Simulated observation data
data = {
    "Vol. of phenol (ml)": [5]*15,
    "Vol. of water (ml)": list(range(3, 33, 2)),
    "Vol. % of phenol": [round(5 / (5 + v) * 100, 2) for v in range(3, 33, 2)],
    "Temp. of disappearance (°C)": np.random.randint(60, 80, size=15),
    "Temp. of appearance (°C)": np.random.randint(55, 75, size=15),
}

df = pd.DataFrame(data)
df["Mean Temp. (°C)"] = df[["Temp. of disappearance (°C)", "Temp. of appearance (°C)"]].mean(axis=1).round(2)

st.dataframe(df)

# F. MODEL GRAPH
st.header("MODEL GRAPH")

fig, ax = plt.subplots()
ax.plot(df["Vol. % of phenol"], df["Mean Temp. (°C)"], marker='o', color='green')
ax.set_xlabel("Volume % of Phenol")
ax.set_ylabel("Mean Miscibility Temperature (°C)")
ax.set_title("Critical Solution Temperature Graph")
st.pyplot(fig)

# G. FORMULA
st.header("FORMULA")
st.latex(r"\text{Vol. \% of Phenol} = \frac{5}{5 + V_w} \times 100")

# H. RESULT
st.header("RESULT")
cst_index = df["Mean Temp. (°C)"].idxmax()
cst_temp = df.loc[cst_index, "Mean Temp. (°C)"]
cst_comp = df.loc[cst_index, "Vol. % of phenol"]

st.markdown(f"**CST of phenol-water system = {cst_temp} °C**")
st.markdown(f"**Critical solution composition = {cst_comp}% phenol by volume**")

# I. VIDEO SIMULATION
st.header("EXPERIMENT SIMULATION")
video_path = "Untitled design.mp4"
st.video(video_path)

# J. DOWNLOADABLE CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download Observation Table", data=csv, file_name='cst_observations.csv', mime='text/csv')
