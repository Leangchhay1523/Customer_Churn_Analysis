# Improt Abstract Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Usage frequency analysis class
class UsageFrequencyAnalysis(BaseAnalysis):
    # Constructor to initialize features
    def __init__(self, data_path):
        super().__init__(data_path)
        self.features = ['Subscription Type', 'Churn']

    # Perform analysis method
    def perform_analysis(self):
        # Load dataset
        df = self.load_data()
        
        # Calculate usage frequency average
        usage_frequency_average = df["Usage Frequency"].mean()
        print(f"Usage Frequency Average: {round(usage_frequency_average)} times.")
        
        # Create usage rage group
        self.create_usage_rate_and_group(df)
        print(df["Usage Rate Group"].head())

        # Churn rate by group
        usage_churn_rate = self.churn_rate_by_group(df)
        print("\n", usage_churn_rate)
        
        # Usage Rate Visualization
        self.usage_churn_rate_visualization(usage_churn_rate)
        
    # Usage Rate group
    def create_usage_rate_and_group(self, df):
        # Calculate usage rate in a period (Tenure)
        df["Usage Rate"] = df["Usage Frequency"] / df["Tenure"]
        # Divide usage rate by group by apply function categorize_usage_rate
        df["Usage Rate Group"] = df["Usage Rate"].apply(self.categorize_usage_rate)
        
    # The usage rate in dataset is in range (0.016 - 30.0) so we need to group it 
    # [0.016 - 9.99] : Low Usage, [9.99 - 19.98] : Medium Usage, [19.98 - 30.0] : Active Usage
    def categorize_usage_rate(self, usage_rate):
        if 0.016 <= usage_rate <= 9.99:
            return "Low"
        elif 9.99 < usage_rate <= 19.98:
            return "Medium"
        elif 19.98 < usage_rate <= 30.0:
            return "Active"
    
    # Calculate churn rate by defined group        
    def churn_rate_by_group(self, df):
        return df.groupby("Usage Rate Group")["Churn"].mean() * 100
    
    # Churn rate group visualization
    def usage_churn_rate_visualization(self, usage_churn_rate):
        # Define figure size of 8 inches by 5 inches
        plt.figure(figsize = (8, 5))
        # Create barplot using sns 
            # x axis represent usage rate group index which are Low, Medium and Active
            # y axis represent values of each usage rate group
            # coolwarm as color pallete
            # Set color status based on usage churn rate
        sns.barplot(x = usage_churn_rate.index, y = usage_churn_rate.values, palette = "mako", hue = usage_churn_rate.index)
        plt.title("Churn Rate by Usage Rate Group") # Figure title
        plt.ylabel("Churn Rate (%)") # label for y axis
        plt.xlabel("Usage Rate Group") # label for x axis
        plt.ylim(0, 100) # Set value range of y to (0 - 100)
        plt.show() # Display the figure
    
if __name__ == "__main__": # Testing in the module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"  # Dataset oath
    usage_frequency_obj = UsageFrequencyAnalysis(path) # create usage freqeuncy analysis obj
    usage_frequency_obj.perform_analysis()
    