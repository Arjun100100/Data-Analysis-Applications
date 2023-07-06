import pandas as pd
import streamlit as st

def question_1(df):
  total_roi_by_bank = df.groupby('Bank_Name')['Return_on_Investment'].mean().idxmac()
  st.write("Bank with Highest Average Return on Investment (ROI):")
  st.write(total_roi_by_bank)

def question_2(df):
  roi_by_investment_type = df.groupby('Investment_Type')['Return_on_Investment'].mean().sort_values(ascending=False)
  st.write("Average Interest Rate Variation Among banks:")
  st.write(roi_by_investment_type)


def question_3(df):
  investment_type_counts = df.pivot_table(index="Bank_Name", columns="Investment_Type", values="Customer_ID", aggfunc="count")
  st.write("Investment Type Counts by Bank:")
  st.write(investment_type_counts)

  most_popular_investment_by_bank = investment_type_counts.idxmax(axis=1)
  st.write("Most Popular Investment Type in Each Bank:")
  st.write(most_popular_investment_by_bank)


def question_4(df):
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

        # Get user input for questions selection
        st.subheader("Step 2: Select Questions")
        questions = st.multiselect(
            "Select the questions to answer:",
            [1, 2, 3, 4],
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




