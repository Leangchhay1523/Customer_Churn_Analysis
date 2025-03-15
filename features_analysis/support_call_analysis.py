# Import abstract base class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Support Call Analysis Class
class SupportCallAnalysis(BaseAnalysis):
    # Constructor to initialize features
    def __init__(self, data_path):
        super().__init__(data_path)
        # Define the relevant features for analysis
        self.features = ['Support Calls', 'Churn']

    # Magic method for string representation
    def __str__(self):
        return f"SupportCallAnalysis with features: {', '.join(self.features)}"

    # Magic method for containment check (to check if feature exists in the class)
    def __contains__(self, item):
        return item in self.features

    # Perform support call analysis method
    def perform_analysis(self):
        # Load dataset
        df = self.load_data()
        
        # Caculate average value of support calls
        support_call_average = df["Support Calls"].mean()
        print(f"Average Support Calls: {round(support_call_average)} times.")
        
        # Correlation between support call and churn
        # Calcualte peason correlation between Churn and Support Calls
        support_churn_correlation = df["Churn"].corr(df["Support Calls"])
        print(f"Correlation between Support Calls and Churn: {support_churn_correlation:.2f}")
        
        # Visualization correlation
        self.correlation_visualiation(df)

    # # Helper method to create a visual representation of churn vs non-churn by support calls        
    def correlation_visualiation(self, df):
        # Set figure dimension of 8 inches by 5 inches
        plt.figure(figsize = (8, 5))

        # Count churned (1) and non-churned (0) customers for each 'Support Calls' category
        # Churned customers by support calls
        churn_by_support_calls = df[df["Churn"] == 1].groupby('Support Calls').size()
        # Non-churned customers by support calls
        not_churn_by_support_calls = df[df["Churn"] == 0].groupby('Support Calls').size()

        # Combine the churn and non-churn data into a DataFrame for visualization
        newDataFrame = pd.DataFrame({
            'Support Calls': churn_by_support_calls.index,
            'Churn': churn_by_support_calls.values,
            'Not Churn': not_churn_by_support_calls.reindex(churn_by_support_calls.index, fill_value=0).values
        })

        # Melt the DataFrame for use with seaborn's barplot (long format)
        newDataFrame = newDataFrame.melt(id_vars='Support Calls', value_vars=['Churn', 'Not Churn'],var_name='Churn Status', value_name='Count')

        # Create barplot to show the average churn rate by support calls
        sns.barplot(x='Support Calls', y='Count', hue='Churn Status', data=newDataFrame, palette="coolwarm")
        
        # Add title and labels
        plt.title('The amount of Churn and Not Churn by Support Calls')
        plt.xlabel('Support Calls')
        plt.ylabel('Count')

        # Show plot
        plt.show()
        

if __name__ == "__main__": # Testing in the module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv" # Data path
    support_call_obj = SupportCallAnalysis(path) 
    # __str__ to print the class instance
    print(support_call_obj)  

    # __contains__ to check if a feature is present
    print('Support Calls' in support_call_obj)  
    print('Usage Frequency' in support_call_obj) 
    support_call_obj.perform_analysis()