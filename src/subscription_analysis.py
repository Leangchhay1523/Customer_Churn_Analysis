from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class SubscriptionAnalysis(BaseAnalysis):
    # Constructor to initialize features
    def __init__(self, data_path):
        super().__init__(data_path)
        # Define features for containment check
        self.features = ['Subscription Type', 'Churn']

    # Magic method for string representation
    def __str__(self):
        return f"SubscriptionAnalysis with features: {', '.join(self.features)}"

    # Magic method for containment check (to check if feature exists in the class)
    def __contains__(self, item):
        return item in self.features
    
    # Function to return the subscription distribution 
    def subscription_distribution(self):
        return self.df["Subscription Type"].value_counts()
    
    # Function to display the subscription type distribution as a countplot
    def visual_subscription_distribution(self):
        # Calculate the churn rate and not churn rate for each subscription type
        churn_rate = self.df.groupby("Subscription Type")["Churn"].mean() * 100
        not_churn_rate = 100 - churn_rate
        
        # Create a DataFrame for the rates
        churn_not_churn = pd.DataFrame({
            "Churn Rate": churn_rate,
            "Not Churn Rate": not_churn_rate
        })
        
        # Plot the churn rate and not churn rate side by side in a histogram
        churn_not_churn.plot(kind='bar', figsize=(8,6), width=0.8, color=['skyblue', 'lightgreen'])
        
        # Add title and labels
        plt.title('Churn Rate and Not Churn Rate of Subscription Type')
        plt.xlabel('Subscription Type')
        plt.ylabel('Percentage (%)')
        plt.xticks(rotation=0)
        plt.legend(['Churn Rate', 'Not Churn Rate'])
        plt.ylim(0, 100)
        plt.show()


    # Function to return the percentage of subscription type
    def subscription_churn(self):
        return self.df.groupby("Subscription Type")["Churn"].mean() * 100
    
    # Function to display a pie chart for subscription types distribution
    def visual_subscription_distribution(self):
        # Get the count of each subscription type (combined for churn and non-churn)
        subscription_counts = self.df["Subscription Type"].value_counts()
        
        # Plot the pie chart for Subscription Type distribution
        plt.figure(figsize=(8, 8))
        plt.pie(subscription_counts, labels=subscription_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
        plt.title('Distribution of Subscription Types')
        plt.show()

    # Display all the analysis performance 
    def perform_analysis(self):
        # Display the subscription type distrinbution
        print(f"\n Subscription Type Distribution : \n{self.subscription_distribution()}")
        # Display a countplot to show the subscription type distribution
        self.visual_subscription_distribution()
        # Display Churn rate which affected by subscription type
        print(f"\n Churn Rate by Subscription Type :\n {self.subscription_churn()}")
        self.visual_subscription_churn()

        plt.show()


if __name__ == "__main__":
    data_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    subscriptionType_analysis = SubscriptionAnalysis(data_path)
    subscriptionType_analysis.perform_analysis()

    # __str__ to print the class instance
    print(subscriptionType_analysis) 

    # __contains__ to check if a feature is present
    print('Subscription Type' in subscriptionType_analysis)  
    print('Usage Frequency' in subscriptionType_analysis)  