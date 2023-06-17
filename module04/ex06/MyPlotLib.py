import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    def histogram(self, data, features):
        fig, axs = plt.subplots(1, len(features))
        for i, feature in enumerate(features):
            axs[i].set_title(feature)
            axs[i].hist(data[feature].dropna())
            axs[i].grid()
        plt.show()
    
    def density(self, data, features):
        data[features].dropna().plot(kind='density')
        plt.show()
                
    def pair_plot(self, data, features):
        pd.plotting.scatter_matrix(data[features].dropna(), diagonal='hist')
        plt.show()
            
    def box_plot(self, data, features):
        fig, ax = plt.subplots()
        ax.boxplot(data[features].dropna(), labels=features)
        plt.show()
                
if __name__ == "__main__":
    data = pd.read_csv("../ex01/data/athlete_events.csv")
    plotter = MyPlotLib()
    
    plotter.histogram(data, ["Height", "Weight"])
    plotter.density(data, ["Height", "Weight"])
    plotter.pair_plot(data, ["Height", "Weight"])
    plotter.box_plot(data, ["Height", "Weight"])
    
    plotter.histogram(data, ["Age", "Year"])
    plotter.density(data, ["Age", "Year"])
    plotter.pair_plot(data, ["Age", "Year"])
    plotter.box_plot(data, ["Age", "Year"])