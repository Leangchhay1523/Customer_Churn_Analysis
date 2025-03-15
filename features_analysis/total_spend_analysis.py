from base_analysis import BaseAnalysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Class for analyzing Total Spend and its relation to Churn
class TotalSpendAnalysis(BaseAnalysis):
    def __init__(self, file_path):
        # Initialize the class by calling the parent class constructor
        super().__init__(file_path)
    
    def perform_analysis(self):
        # Load the dataset and perform analysis on Total Spend and Churn
        df = self.load_data() 

        # Calculate and print the average total spend and its correlation with churn
        average_total_spend = df['Total Spend'].mean() 
        correlation_spend_churn = df['Total Spend'].corr(df['Churn'])

        print(f"Average Total Spend: {average_total_spend:.2f}")
        print(f"Correlation between Total Spend and Churn: {correlation_spend_churn:.2f}")

        # Visualize the relationship between Total Spend and Churn
        self.visualize_data(df)
        self.visualize_boxplot(df)


    def visualize_boxplot(self, df):
        # Convert Churn to categorical labels for better visualization
        df['Churn Label'] = df['Churn'].map({1: 'Churned', 0: 'Not Churned'})

        # Create boxplot using seaborn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Churn Label', y='Total Spend', data=df, palette='coolwarm')

        # Formatting the graph
        plt.title('Box Plot of Total Spend by Churn Status')
        plt.xlabel('Churn Status')
        plt.ylabel('Total Spend')
        plt.grid(axis='y', alpha=0.7)

        # Show the plot
        plt.show()




    def visualize_data(self, df):
        # Group by Total Spend ranges and Churn status, then calculate the count of customers
        spend_bins = [100, 200, 300, 400, 500,600,700,800,900,1000]
        spend_labels = ['100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000']
        df['Total Spend Range'] = pd.cut(df['Total Spend'], bins=spend_bins, labels=spend_labels)

        # Convert Churn to categorical values for better labeling (1 for Churned, 0 for Stayed)
        df['Churn Label'] = df['Churn'].map({1: 'Churned', 0: 'Stayed'})

        # Count the churn status for each Total Spend range and Churn label
        churn_counts = df.groupby(['Total Spend Range', 'Churn Label'], observed=False).size().unstack(fill_value=0)

        # Plotting the bars for Churned and Stayed customers
        churn_counts.plot(kind='bar', width=0.8, figsize=(10, 6), color=['#ff9999', '#66b3ff'])

        plt.title('Churn Distribution by Total Spend Range')  # Title of bar chart
        plt.xlabel('Total Spend Range')  # x-axis label
        plt.ylabel('Number of Customers')  # y-axis label
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.legend(title="Churn Status", labels=["Churned", "Not Churn"])  # Churn legend
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":
    file_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    analysis = TotalSpendAnalysis(file_path)
    analysis.perform_analysis()
