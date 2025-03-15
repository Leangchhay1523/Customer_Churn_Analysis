# Import Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Gender Analysis Class
class GenderAnalysis(BaseAnalysis):
    # __str__ method to provide a string representation of the object
    def __str__(self):
        return f"Gender Analysis with {len(self.df)} records."

    # __contains__ method to check if a gender is present in the dataset
    def __contains__(self, gender):
        return gender in self.df["Gender"].values

    # Method to perform gender analysis
    def perform_analysis(self):
        # Load dataset
        df = self.load_data()
        
        # Count number of males and females
        gender_counts = df["Gender"].value_counts()
        print("Gender Count: ")
        print(f"Male: {gender_counts["Male"]}")
        print(f"Female: {gender_counts["Female"]}")
        
        # Visualization number of males and females
        self.gender_count_visualization(df)
        
        
        # Calculate churn rate groupby gender
        gender_churn_rate = df.groupby("Gender")["Churn"].mean() * 100
        print("\nGender Churn Rate: ")
        print(f"Male: {gender_churn_rate["Male"]:.2f}%")    # Display Male churn rate
        print(f"Female: {gender_churn_rate["Female"]:.2f}%")    # Display Female churn rate
        
        # Churn rate visualization for each gender group
        self.gender_churn_rate_visualization(gender_churn_rate)
    
    # Visualization method for number of males and females
    def gender_count_visualization(self, df):
        # Create figure size of 6 inches by 4 inches
        plt.figure(figsize = (6, 4))
        
        # Create a bar plot with seaborn library
            # Specifying x axis as gender
            # df as source of data
            # pastel as color pattern
            # hue specify the colored differently based on Churn status
        sns.countplot(x = "Gender", data = df, palette = "pastel", hue = "Gender")
        plt.title("Gender Distribution of Customers") # Title of figure
        plt.xlabel("Gender") # Label for x axis
        plt.ylabel("Count") # Label for y axis
        plt.show() # Display the figure
    
    # Churn rate visualization
    def gender_churn_rate_visualization(self, gender_churn_rate):
        # Create figure size of 8 inches by 5 inches
        plt.figure(figsize = (8, 5))
        
        # Create a barplot
            # x axis represent index of gender churn rate which is male and femlae
            # y axis represent value of churn rate for male and female
            # hue specify the figure will colored differently based on gender churn rate index
            # coolwarm as color pallete
            # Dispaly the legend
        sns.barplot(x = gender_churn_rate.index, y = gender_churn_rate.values, hue = gender_churn_rate.index , palette = "coolwarm", legend = True)
        plt.title("Churn Rate by Tenure Group") # Title of figure
        plt.ylabel("Churn Rate (%)") # Label for y axis
        plt.xlabel("Gender Group") # Label 
        plt.ylim(0, 100) # Set value range for y from 0 to 100 (0% to 100%)
        plt.show() # Dispaly figure

if __name__ == "__main__": # Testing in module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv" # Path to dataset
    gender_analysis = GenderAnalysis(path)  # Create Gender analysis object
     # __str__ method
    print(gender_analysis) 
    
    # __contains__ method to check if 'Male' and 'Gay' exist in the dataset
    print("\nChecking if 'Male' is in the dataset:", 'Male' in gender_analysis)  
    print("Checking if 'Gay' is in the dataset:", 'Gay' in gender_analysis) 
    
    gender_analysis.perform_analysis() # Call perform analysis method