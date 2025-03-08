from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt 
class LastInteractionAnalysis(BaseAnalysis):
    def __init__(self, file_path):
        super().__init__(file_path)

    def perform_analysis(self):
        df = self.load_data()

        min_last_interaction = df["Last Interaction"].min()
        max_last_interaction = df["Last Interaction"].max()
        correlation_last_interaction_churn = df["Last Interaction"].corr(df["Churn"])

        print(f"Most recent customer interaction: {min_last_interaction}")
        print(f"Longest time since customer interaction: {max_last_interaction}")
        print(f"Correlation between Last Interaction and Churn: {correlation_last_interaction_churn:.2f}")

        self.visualize_data(df)

    def visualize_data(self, df):
        plt.scatter(df["Last Interaction"], df["Churn"], alpha=0.2)
        plt.title("Correlation Last Interaction & Churn")
        plt.xlabel("Last Interaction")
        plt.ylabel("Churn")
        plt.show()

analysis = LastInteractionAnalysis("d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv")
analysis.perform_analysis()
