# Import Abstract Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd

# Initial Analysis Class
class InitialAnalysis(BaseAnalysis):
    # __str__ method to provide a string representation of the object
    def __str__(self):
        return f"Initial Analysis of dataset with {len(self.df)} rows and {len(self.df.columns)} columns."

    # __contains__ method to check if a column exists in the dataset
    def __contains__(self, column_name):
        return column_name in self.df.columns

    # Initial Analysis Method
    def perform_analysis(self):
        # Load Data
        df = self.load_data()
        
        # Data columns and rows
        shape = df.shape
        print(f"Rows: {shape[0]}") # Row of dataset
        print(f"Columns: {shape[1]}") # Column of dataset

        
        # Inspect Data Head
        print(f"\nInspect Data Head:\n {df.head()}")
        
        # Inspect Data Tail
        print(f"\nInspect Data Tail:\n {df.tail()}")
        
        # Inspect Dataset Columns
        print(f"\nDataset Columns: {list(df.columns)}")
        
        # Datatype
        # print(f"\nData Types:\n {df.dtypes}")
        
        # Data info
        print("\nData Info:")
        print(df.info())
        
        # Statistic Summarize of Nnumeric Data
        print(f"\nStatistical Summarize:\n {df.describe().T}")
        
        # Find Null Values
        print(f"\nNull Values:\n {df.isnull().sum()}")
    
    
if __name__ == "__main__": # Testing in the module
    path = "d:/year2/term2/python/Project/Customer_Churn_Analysis/data/data_500_rec.csv"
    initial_analysis_obj = InitialAnalysis(path)

    # __str__ method
    print(initial_analysis_obj)  # Will call the __str__ method
    
    # __contains__ method to check if a column exists
    print("\nChecking if 'Gender' column exists:", 'Gender' in initial_analysis_obj) 

    initial_analysis_obj.perform_analysis()