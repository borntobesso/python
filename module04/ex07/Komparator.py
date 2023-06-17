import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np

class Komparator:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def compare_box_plots(self, categorical_var, numerical_var):
        if isinstance(numerical_var, str):
            numerical_var = [numerical_var]
        data = self.data[[categorical_var] + numerical_var].dropna()
        plt.figure(figsize=(10, 6))
        num_plots = len(numerical_var)
        
        for i, var in enumerate(numerical_var):
            plt.subplot(num_plots, 1, i+1)
            sns.boxplot(x=categorical_var, y=var, data=data)

        plt.tight_layout()
        plt.show()
        
    def density(self, categorical_var, numerical_var):
        if isinstance(numerical_var, str):
            numerical_var = [numerical_var]
        data = self.data[[categorical_var] + numerical_var].dropna()
        plt.figure(figsize=(10, 6))
        num_plots = len(numerical_var)
        
        for i, var in enumerate(numerical_var):
            plt.subplot(num_plots, 1, i+1)
            
            for category in data[categorical_var].unique():
                subset = data[data[categorical_var] == category]
                sns.kdeplot(subset[var], label=category)
                
            plt.xlabel(var)
            plt.legend()
        
        plt.tight_layout()
        plt.show()
        
    def compare_histograms(self, categorical_var, numerical_vars):
        if isinstance(numerical_vars, str):
            numerical_vars = [numerical_vars]
        data = self.data[[categorical_var] + numerical_vars].dropna()
        plt.figure(figsize=(12, 8))
        num_plots = len(numerical_vars)
        colors = sns.color_palette('pastel', len(data[categorical_var].unique()))
                                                         
        for i, var in enumerate(numerical_vars):
            plt.subplot(num_plots, 1, i+1)
            
            for j, category in enumerate(data[categorical_var].unique()):
                subset = data[data[categorical_var] == category]
                plt.hist(subset[var], bins=20, alpha=0.5, color=colors[j % len(colors)], label=category)
            
            plt.xlabel(var)
            plt.legend()
        
        plt.tight_layout()
        plt.show()
        
if __name__ == "__main__":
    data = pd.read_csv('../ex01/data/athlete_events.csv')
    komparator = Komparator(data)
    # Single numerical variable test
    komparator.compare_box_plots('Sex', 'Height')
    komparator.density('Sex', 'Weight')
    komparator.compare_histograms('Sex', 'Height')
    # Multiple numerical variables test
    komparator.compare_box_plots('Season', ['Height', 'Weight'])
    komparator.density('Medal', ['Height', 'Weight'])
    komparator.compare_histograms('Medal', ['Height', 'Weight'])