from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class ContractAnalysis(BaseAnalysis):
    # __str__ to provide a meaningful string representation of the object
    def __str__(self):
        return f"Contract Analysis with {len(self.df)} records"
    
    # Function to display all the performance analysis
    def perform_analysis(self):

        # Dislay the contract length distribution 
        print(f"\n Contract Length Distribution : \n{self.contract_ditribution()}")
        
        # Display a coutplot of contract length distribution
        self.visual_contract_distribution()

        # Display the churn rate which affect by Contract Length 
        print(f"\n Churn Rate by Contract Length :\n {self.contract_churn()}")

        # Display a barplot to show the contract length and churn rate
        self.visual_contract_churn()
    
    # Function the contract length distribution 
    def contract_ditribution(self):
        return self.df["Contract Length"].value_counts()
    
    def visual_contract_distribution(self):
        # Count the number of churned and not churned customers per contract length
        churn_counts = self.df[self.df["Churn"] == 1]["Contract Length"].value_counts()
        not_churn_counts = self.df[self.df["Churn"] == 0]["Contract Length"].value_counts()

        # Ensure all contract length categories are represented
        all_contracts = sorted(self.df["Contract Length"].unique())  # Get sorted contract lengths
        churn_counts = churn_counts.reindex(all_contracts, fill_value = 0)  # Fill missing categories with 0
        not_churn_counts = not_churn_counts.reindex(all_contracts, fill_value = 0)

        # Combine churn and not churn values into one list for pie chart
        values = []
        labels = []
        for length in all_contracts:
            total_customers = churn_counts[length] + not_churn_counts[length]
            values.append(total_customers)
            labels.append(length)

        # Define colors for each contract length category
        colors = ['#FF9999', '#66B2FF', '#FFCC99', '#99FF99', '#FFB3E6']  # Customize colors as needed

        # Plot pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels = labels, colors = colors, autopct = "%1.1f%%", startangle = 90, wedgeprops = {'edgecolor': 'black'})

        # Add title
        plt.title("Distribution of Customers by Contract Length")

        # Show chart
        plt.show()
    

     # Function to returns the contract length and churn as percentage   
    def contract_churn(self):
        return self.df.groupby("Contract Length")['Churn'].mean() * 100
    
    # Function to display the contract length and churn rate as a barplot
    def visual_contract_churn(self):
        # Get churn rate
        churn_rate = self.contract_churn()
        
        # Calculate not churn rate
        not_churn_rate = 100 - churn_rate  # Assuming churn_rate is in percentage
        
        # Prepare DataFrame for Seaborn
        churn_data = pd.DataFrame({
            "Contract Length": churn_rate.index.tolist() * 2,  # Repeat contract lengths
            "Rate": list(churn_rate) + list(not_churn_rate),  # Churn & Not Churn rates
            "Type": ["Churn"] * len(churn_rate) + ["Not Churn"] * len(not_churn_rate)  # Labels
        })
        
        # Create bar plot
        plt.figure(figsize=(8,6))
        sns.barplot(x = "Contract Length", y = "Rate", hue = "Type", data = churn_data, palette = ['skyblue', 'lightgreen'])
        
        # Add title and labels
        plt.title("Churn vs Not Churn Rate by Contract Length")
        plt.xlabel("Contract Length")
        plt.ylabel("Rate (%)")
        plt.ylim(0, 100)
        
        # Show the legend
        plt.legend(title = "Customer Status")
        
        # Display plot
        plt.show()


if __name__ == "__main__":
    data_path = "/data/data_500_rec.csv"
    contract_analysis = ContractAnalysis(data_path)
    print(contract_analysis)
    contract_analysis.perform_analysis()
    