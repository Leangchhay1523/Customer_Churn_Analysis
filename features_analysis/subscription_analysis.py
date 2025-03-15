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
        plt.title('Churn Rate and Not Churn Rate per Subscription Type')
        plt.xlabel('Subscription Type')
        plt.ylabel('Percentage (%)')
        plt.xticks(rotation=45)
        plt.legend(['Churn Rate', 'Not Churn Rate'])
        plt.ylim(0, 100)
        plt.show()


    # Function to return the percentage of subscription type
    def subscription_churn(self):
        return self.df.groupby("Subscription Type")["Churn"].mean() * 100
    
    # Function to display churn rate which affected by subscription type as a barplot
    def visual_subscription_churn(self):
        # Group data by Subscription Type and Churn to get the counts
        churn_counts = self.df.groupby(["Subscription Type", "Churn"]).size().unstack(fill_value=0)
        
        # Create a single pie chart for all subscription types
        plt.figure(figsize=(8, 8))  # Set the size of the pie chart
        
        # Flatten the data and get the counts for churn and not churn
        labels = []
        sizes = []
        colors = []  # Define different colors for each segment
        color_palette = ['#FFB3B3', '#FFCC99', '#CCFFCC', '#99CCFF', '#FF99FF', '#FFEB99']  # Add more colors if necessary
        
        for i, (sub_type, counts) in enumerate(churn_counts.iterrows()):
            labels.append(f"{sub_type} - Churn")
            labels.append(f"{sub_type} - Not Churn")
            sizes.append(counts[1])  # Churn count
            sizes.append(counts[0])  # Not Churn count
            colors.append(color_palette[2*i])  # Churn color
            colors.append(color_palette[2*i+1])  # Not Churn color
        
        # Plot the combined pie chart with different colors
        plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140, wedgeprops={'edgecolor': 'black'})
        plt.title('Churn Distribution for All Subscription Types')
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