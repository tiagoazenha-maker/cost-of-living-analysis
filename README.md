# cost-of-living-analysis
🌍 Cost of Living Analysis
📊 Project Overview

This project analyzes global cost of living data to explore the relationship between:

Cost of living

Monthly income

Purchasing power

The goal is to identify economic patterns and potential imbalances across countries.

📁 Dataset

The dataset contains information for 107 countries, including:

cost_index → Cost of living indicator

monthly_income → Average monthly income

purchasing_power_index → Relative purchasing power

🔍 Key Questions

This analysis aims to answer:

Do countries with higher cost of living also have higher income?

Are there countries with high cost but low purchasing power?

How can countries be categorized based on cost levels?

🧪 Data Analysis Process
1. Data Loading & Cleaning

Loaded dataset using Pandas

Cleaned column names

Checked for missing values

2. Feature Engineering

Created new variable:

income_to_cost_ratio = monthly_income / cost_index

Segmented countries into categories:

Low cost (<70)

Medium cost (70–120)

High cost (>120)

3. Data Filtering

Example:

df[
    (df["cost_index"] > 120) &
    (df["purchasing_power_index"] < 60)
]

Used to identify countries with economic imbalance.

4. Analysis & Insights

Key findings:

Countries with higher cost of living often have higher income

Purchasing power does not always scale with income

Some countries show high cost but low purchasing power, indicating economic pressure

📈 Example Visualization

(Add your plots here later)

🛠️ Technologies Used

Python (Pandas, Matplotlib)

PostgreSQL

SQL

Jupyter Notebook

Git & GitHub

🗄️ SQL Analysis

Example query:

SELECT country, cost_index
FROM cost_of_living
ORDER BY cost_index DESC
LIMIT 5;
🚀 How to Run
pip install -r requirements.txt
jupyter notebook
📌 Future Improvements

Build a machine learning model to predict purchasing power

Create an interactive dashboard (Streamlit / Power BI)

Add more datasets for deeper analysis

👨‍💻 Author

Tiago Azenha
GitHub: https://github.com/tiagoazenha-maker
