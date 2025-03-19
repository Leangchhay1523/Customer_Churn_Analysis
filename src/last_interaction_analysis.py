from base_analysis import BaseAnalysis
import pandas as pd
import matplotlib.pyplot as plt  

# Class for analyzing the impact of last customer interaction on churn
class LastInteractionAnalysis(BaseAnalysis):
    # __str__ method to provide a string representation of the object
    def __str__(self):
        return f"Analysis of customer churn based on Last Interaction with dataset of {len(self.df)} rows and {len(self.df.columns)} columns."

    # __contains__ method to check if a column exists in the dataset
    def __contains__(self, column_name):
        return column_name in self.df.columns

    def __init__(self, file_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(file_path)

    def perform_analysis(self):
        # Load the dataset and perform analysis on Total Spend and Churn
        df = self.load_data()

        # Find the most recent and longest last interaction times
        min_last_interaction = df["Last Interaction"].min()
        max_last_interaction = df["Last Interaction"].max()
        # Calculate correlation between last interaction and churn
        correlation_last_interaction_churn = df["Last Interaction"].corr(df["Churn"])

        print(f"Most recent customer interaction: {min_last_interaction}")
        print(f"Longest time since customer interaction: {max_last_interaction}")
        print(f"Correlation between Last Interaction and Churn: {correlation_last_interaction_churn:.2f}")

        # Visualize the relationship between last interaction and churn
        self.visualize_data(df)

    def visualize_data(self, df):
        # Create a bar chart to show the relationship between Last Interaction and Churn
        # Count the occurrences of each unique Last Interaction time with respect to Churn
        interaction_churn_counts = df.groupby(["Last Interaction", "Churn"]).size().reset_index(name="Counts")

        # Pivot the data to create separate columns for Churned and Not Churned
        pivot = interaction_churn_counts.pivot(index="Last Interaction", columns="Churn", values="Counts").fillna(0)
        
        # Plotting the bar chart with two bars for each "Last Interaction" category
        pivot.plot(kind='bar', figsize=(10, 6), color=['#ff9999', '#66b3ff'], width=0.8)

        # Adding labels and title
        plt.title("Impact of Last Interaction on Churn")
        plt.xlabel("Last Interaction Time")
        plt.ylabel("Number of Customers")
        plt.xticks(rotation=45)
        plt.legend(title="Churn Status", labels=[f"Churn: {col}" for col in pivot.columns])
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    analysis = LastInteractionAnalysis(file_path)

     # __str__ method
    print(analysis) 
    
    # __contains__ method to check if 'Last Interaction' column exists
    print("\nChecking if 'Last Interaction' column exists:", 'Last Interaction' in analysis) 
    

    analysis.perform_analysis()
