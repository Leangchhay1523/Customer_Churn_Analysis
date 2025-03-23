# Abstract Base Class
# OOP Concept Usage: Abstraction

"""

BaseAnalysis is the Abstract Base Class that provide contract for each subclass. Each subclass must perform the
perform_analysis() method.

"""

import pandas as pd
from abc import ABC, abstractmethod

class BaseAnalysis(ABC):
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = self.load_data()
    def load_data(self):
        try:
            df = pd.read_csv(self.data_path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Dataset not found at path {self.data_path}") from e
        else:
            return df
    
    @abstractmethod
    def perform_analysis(self):
        # Don't forget to call load_data() method
        pass