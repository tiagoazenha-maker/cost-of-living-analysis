from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

os.makedirs("images", exist_ok=True)

path = Path(__file__).parent / "cost_of_living.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.strip()

df["income_to_cost_ratio"] = df["monthly_income"] / df["cost_index"]

df["cost_category"] = pd.cut(
    df["cost_index"],
    bins=[0, 70, 120, float("inf")],
    labels=["Low", "Medium", "High"]
)

password = quote_plus("Telemovel27!")
engine = create_engine(f"postgresql://postgres:{password}@localhost:5433/postgres")

df.to_sql("cost_of_living", engine, if_exists="replace", index=False)

print("Dados enviados para PostgreSQL!")

high_cost_low_power = df[
    (df["cost_index"] > 120) &
    (df["purchasing_power_index"] < 60)
]

plt.figure()
plt.hist(df["cost_index"])
plt.title("Cost Index Distribution")
plt.savefig("images/distribution.png")

plt.figure()
plt.scatter(df["cost_index"], df["monthly_income"])
plt.xlabel("Cost Index")
plt.ylabel("Monthly Income")
plt.title("Cost vs Income")
plt.savefig("images/scatter.png")

print("Projeto executado com sucesso!")
