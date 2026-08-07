import matplotlib.pyplot as plt
import os

# -----------------------------
# Data
# -----------------------------
years = [
    "FY06","FY07","FY08","FY09","FY10","FY11","FY12",
    "FY13","FY14","FY15","FY16","FY17","FY18","FY19",
    "FY20","FY21","FY22","FY23","FY24","FY25","FY26"
]

it_services = [
    0.56,0.66,0.78,0.87,0.98,1.09,1.19,
    1.29,1.39,1.49,1.59,1.70,1.81,1.93,
    2.03,2.16,2.41,2.65,2.79,2.80,2.88
]

gcc = [
    0.11,0.13,0.16,0.18,0.21,0.25,0.29,
    0.34,0.39,0.45,0.52,0.60,0.68,0.77,
    0.84,0.92,1.02,1.12,1.22,1.30,1.42
]

faang = [
    0.005,0.006,0.008,0.010,0.013,0.016,0.020,
    0.024,0.029,0.035,0.042,0.049,0.056,0.063,
    0.068,0.072,0.075,0.078,0.080,0.082,0.085
]

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(13,7))

plt.plot(
    years,
    it_services,
    marker='o',
    linewidth=3,
    markersize=6,
    label='Indian IT Services'
)

plt.plot(
    years,
    gcc,
    marker='s',
    linewidth=3,
    markersize=6,
    label='GCC'
)

plt.plot(
    years,
    faang,
    marker='^',
    linewidth=3,
    markersize=6,
    label='FAANG / MAAMA'
)

plt.title(
    "Engineering Workforce in India's Technology Sector",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Fiscal Year", fontsize=13)
plt.ylabel("Engineering Employees (Millions)", fontsize=13)

plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

os.makedirs("assets", exist_ok=True)
plt.savefig(
    "assets/india_tech_engineering_workforce.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()