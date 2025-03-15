# Import Abstract Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Payment Delay Analysis Class
class PaymentDelayAnalysis(BaseAnalysis):
    # Magic method for string representation
    def __str__(self):
        return f"PaymentDelayAnalysis with features: {', '.join(self.features)}"

    # Magic method for containment check (to check if feature exists in the class)
    def __contains__(self, item):
        return item in self.features
    
    # Constructor to initialize features
    def __init__(self, data_path):
        super().__init__(data_path)
        # Define features for containment check
        self.features = ['Payment Delay', 'Churn']

    # Payment Delay Analysis Method
    def perform_analysis(self):
        # load data set
        df = self.load_data()
        
        # Calculate payment delay average
        payment_delay_average = df["Payment Delay"].mean()
        print(f"Payment Delay Average: {round(payment_delay_average)} months.")
        
        # Payment Delay and Churn correlation
        # Calculate correlation value between Payment Delay and Churn
        payment_churn_correlation = df["Payment Delay"].corr(df["Churn"])
        print(f"Correlation between Payment Dela and Churn: {payment_churn_correlation:.2f}")
        
        # Call Scatter plot visualization method
        self.correlation_visualiation(df)
        
    # Correlation Visualiaztion Method
    def correlation_visualiation(self, df):
        # Group by Payment Delay and Churn, then count the occurrences
        payment_delay_churn_count = df.groupby(['Payment Delay', 'Churn']).size().unstack(fill_value=0)

        # Plot a histogram with bars next to each other for each Payment Delay value
        payment_delay_churn_count.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen'], edgecolor='black', width=0.8)

        plt.title('Count of Customers with Payment Delay vs. Churn')
        plt.xlabel('Payment Delay (months)')
        plt.ylabel('Customer Count')
        plt.xticks(rotation=0)
        plt.legend(['Not Churn', 'Churn'])
        plt.show()
        
        


if __name__ == "__main__": # Testing in the module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    obj = PaymentDelayAnalysis(path)
    # __str__ to print the class instance
    print(obj) 
    # __contains__ to check if a feature is present
    print('Payment Delay' in obj)  
    print('Usage Frequency' in obj) 
    obj.perform_analysis()

     