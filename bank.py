import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import streamlit as st


def question_1(df):
  total_roi_by_bank = df.groupby('Bank_Name')['Return_on_Investment'].mean().idxmax()
  st.write("Bank with Highest Average Return on Investment (ROI):")
  st.write(total_roi_by_bank)

def question_2(df):
  roi_by_investment_type = df.groupby('Investment_Type')['Return_on_Investment'].mean().sort_values(ascending=False)
  st.write("Average Interest Rate Variation Among banks:")
  st.write(roi_by_investment_type)

def question_3(df):
  plt.figure(figsize=(8, 6))
  sns.scatterplot(x="Capital_Invested", y="Current_Value_of_Investment", data=df)
  plt.xlabel("Capital Invested")
  plt.ylabel("Current Value of Investment")
  plt.title("Correlation between Capital Invested and Current Value")
  st.pyplot()

  correlation_coefficient = df["Capital_Invested"].corr(df["Current_Value_of_Investment"])
  st.write("Correlation Coefficient between Capital Invested and Current Value:")
  st.write(correlation_coefficient)

def question_4(df):
  investment_type_counts = df.pivot_table(index="Bank_Name", columns="Investment_Type", values="Customer_ID", aggfunc="count")
  st.write("Investment Type Counts by Bank:")
  st.write(investment_type_counts)

  most_popular_investment_by_bank = investment_type_counts.idxmax(axis=1)
  st.write("Most Popular Investment Type in Each Bank:")
  st.write(most_popular_investment_by_bank)


def question_5(df):
  sns.set_style("white")
  plt.figure(figsize=(10, 6))
  sns.lineplot(x="Investment_Year", y="Interest_Rate", hue="Bank_Name", data=df)
  plt.xlabel("Investment Year")
  plt.ylabel("Interest Rate")
  plt.title("Trend in Interest Rates over the Years for Each Bank")
  plt.legend(title='Bank Name', bbox_to_anchor=(1.05, 1), loc='upper left')
  plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
  st.pyplot()

def question_6(df):
  bins = [0, 10000, 20000, 40000, 60000, 80000, 100000, float('inf')]
  labels = ['<10k', '10k-20k', '20k-40k', '40k-60k', '60k-80k', '80k-100k', '100k+']
  df['Capital_Investment_Group'] = pd.cut(df['Capital_Invested'], bins=bins, labels=labels)
  average_interest_rate = df.groupby('Capital_Investment_Group')['Interest_Rate'].mean()
  plt.figure(figsize=(8, 6))
  average_interest_rate.plot(kind='bar', color='skyblue')
  plt.xlabel("Capital Invested")
  plt.ylabel("Average Interest Rate")
  plt.title("Average Interest Rate for Different Capital Investment Groups")
  plt.grid(axis='y')
  st.pyplot()

def question_7(df):
  volatility_by_investment_type = df.groupby('Investment_Type')['Return_on_Investment'].std()
  highest_volatility_investment_type = volatility_by_investment_type.idxmax()
  highest_volatility_std_dev = volatility_by_investment_type.max().round(3)
  st.write(f"The investment type with the highest volatility in returns is: {highest_volatility_investment_type}")
  st.write(f"The standard deviation of returns for this investment type is: {highest_volatility_std_dev}")


def main():
    st.title("Data Analysis Report")

    # File uploader to upload the data file
    st.subheader("Step 1: Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Show a sample of the data
        st.subheader("Sample Data")
        st.dataframe(df.head())

        st.subheader("Questions")
        st.write("1. Which bank has the average overall return on investment (ROI) across all years?")
        st.write("2. What is the trend in interest rates over the years for each bank?")
        st.write("3. Which investment type is the most popular among customers in each bank?")
        st.write("4. Which investment type has shown the highest volatility in returns?")

        # Get user input for questions selection
        st.subheader("Step 2: Select Questions")
        questions = st.multiselect(
            "Select the questions to answer:",
            [1, 2, 3, 4, 5, 6, 7],
            format_func=lambda q: f"Question {q}",
        )

        # Call the functions based on the user input
        if 1 in questions:
            question_1(df)
        if 2 in questions:
            question_2(df)
        if 3 in questions:
            question_3(df)
        if 4 in questions:
            question_4(df)

if __name__ == "__main__":
    main()




