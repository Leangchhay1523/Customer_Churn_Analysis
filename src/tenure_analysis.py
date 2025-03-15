from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tenure analysis class
class TenureAnalysis(BaseAnalysis):
    # Magic method for string representation
    def __str__(self):
        return f"TenureAnalysis: {len(self.df)} records, Average Tenure: {round(self.df['Tenure'].mean())} months"

    # Perform tenure analysis method
    def perform_analysis(self):
        # Constructor: Initializes the path and data
        def __init__(self, data_path):
            super().__init__(data_path)
            

        # Load dataset
        df = self.load_data()
        
        
        # Tenure Distribution
        self.tenure_group_distribution(df)
        print("Creating Tenure Distribution: ")
        print(df["Tenure Group"].head())
        
        # Tenure Churn Rate by Group
        tenure_churn_rate = self.churn_rate_by_group(df)
        print("\nCalculate churn rate by Tenure Group: ")
        print(tenure_churn_rate)
        
        # Tenure churn rate by group visualization
        self.churn_rate_visualization(tenure_churn_rate)
        
    # The range of tenure in the dataset is (1 - 60) so we need to group age
    # [1 - 12] : New Customer
    # [12 - 36] : Engage User
    # [36 - 60] : Loyal User
    def categorize_tenure(self, tenure):
        if tenure <= 12:
            return "New Customer"
        elif tenure >= 13 and tenure <= 36:
            return "Engage"
        elif tenure >= 37:
            return "Loyal" 
    
    # Create tenure group by applying categorize_tenure method
    def tenure_group_distribution(self, df):
        df["Tenure Group"] = df["Tenure"].apply(self.categorize_tenure)
    
    # Calculate churn rate by tenure group
    def churn_rate_by_group(self, df):
        return df.groupby("Tenure Group")["Churn"].mean() * 100
    
    # Visualization of churn rate by group
    def churn_rate_visualization(self, tenure_churn_rate):
        # Create figure with size of 8 inches by 5 inches
        plt.figure(figsize=(8, 5))
        # Create barplot
            # x axis represent index of tenure churn rate which are New Customer, Engage and Loyal
            # y axis represent values of churn rate for each tenure group
            # coolwarm as color pallete
            # color status by tenure_churn_rate index
        sns.barplot(x = tenure_churn_rate.index, y = tenure_churn_rate.values, palette = "coolwarm", hue = tenure_churn_rate.index)
        plt.title("Churn Rate by Tenure Group") # Title of figure
        plt.ylabel("Churn Rate (%)") # Label of y axis
        plt.xlabel("Tenure Group") # Label of x axis
        plt.ylim(0, 100) # Limit value of y axis (0 to 100)
        plt.show() # Show figure

    # Display number of customers in each tenure group
    def display_customers_by_group(self, df):
        tenure_counts = df["Tenure Group"].value_counts()
        print("\nNumber of customers in each Tenure Group:")
        print(tenure_counts)
        
if __name__ == "__main__": # Testing in the module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv" # Data path
    tenure_analysis_obj = TenureAnalysis(path) # Tenure analysis feature
    print(tenure_analysis_obj) 
    tenure_analysis_obj.perform_analysis() # Perform tenure analysis
    
        