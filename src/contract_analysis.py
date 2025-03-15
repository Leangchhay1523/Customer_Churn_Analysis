from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class ContractAnalysis(BaseAnalysis):
    # __str__ to provide a meaningful string representation of the object
    def __str__(self):
        return f"Contract Analysis with {len(self.df)} records"
    
    # Function the contract length distribution 
    def contract_ditribution(self):
        return self.df["Contract Length"].value_counts()
    
    # Function to display contract length distribution as countplot
    def visual_contract_distribution(self):
        # Count the number of churned and not churned customers per contract length
        churn_counts = self.df[self.df["Churn"] == 1]["Contract Length"].value_counts()
        not_churn_counts = self.df[self.df["Churn"] == 0]["Contract Length"].value_counts()

        # Ensure all contract length categories are represented
        all_contracts = sorted(self.df["Contract Length"].unique())  # Get sorted contract lengths
        churn_counts = churn_counts.reindex(all_contracts, fill_value=0)  # Fill missing categories with 0
        not_churn_counts = not_churn_counts.reindex(all_contracts, fill_value=0)

        # Combine churn and not churn values into one list
        values = []
        labels = []
        for length in all_contracts:
            values.append(not_churn_counts[length])  # First: Not Churned customers
            labels.append(f"{length} - Not Churn ({not_churn_counts[length]})")
            values.append(churn_counts[length])  # Second: Churned customers
            labels.append(f"{length} - Churn ({churn_counts[length]})")

        # Define colors
        colors = ['#FFB3B3', '#FFCC99', '#CCFFCC', '#99CCFF', '#FF99FF', '#FFEB99']  # Alternate colors for each category

        # Plot pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140, wedgeprops={'edgecolor': 'black'})

        # Add title
        plt.title("Contract Length Distribution (Churn vs Not Churn)")

        # Show chart
        plt.show()

     # Functino to returns the contract length and churn as percentage   
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
        sns.barplot(x="Contract Length", y="Rate", hue="Type", data=churn_data, palette=['skyblue', 'lightgreen'])
        
        # Add title and labels
        plt.title("Churn vs Not Churn Rate by Contract Length")
        plt.xlabel("Contract Length")
        plt.ylabel("Rate (%)")
        plt.ylim(0, 100)
        
        # Show the legend
        plt.legend(title="Customer Status")
        
        # Display plot
        plt.show()
        
        
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


if __name__ == "__main__":
    data_path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    contract_analysis = ContractAnalysis(data_path)
    print(contract_analysis)
    contract_analysis.perform_analysis()
    


