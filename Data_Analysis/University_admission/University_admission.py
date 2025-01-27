import pandas as pd
from plotnine import ggplot, aes, geom_point, stat_smooth
import os
import matplotlib.pyplot as plt
import seaborn as sns

class BasicAnalysis:
    
    def __init__(self):
        self.csv_data = 'data.csv'
        self.normalized_data = 'normalized_data.csv'     
        return
    
# =============================================================================
#     def download_to_csv(self):
#         # download data
#         df = pd.read_csv(self.csv_data)
#             
#         return
# =============================================================================
    
    def scatter_plot(self):
        # load the data to a df
        data = pd.read_csv(self.csv_data)
        
        # make folder to put plots
        if not os.path.exists("Plots"):
            os.mkdir("Plots")
        
        for column in data.iloc[:, 1:].columns:
            print(column)
            gg = (ggplot(data, aes(x= data[column], y=data.columns[-1])) + geom_point() + stat_smooth(method = 'lm'))
            plot_name = column + ".jpg"
            # save plots in Plots directory
            gg.save(filename = plot_name, path = "Plots")
            
        return
    
    def normalize_data(self, data):       

         for column in data.columns:
             data[column] = (data[column]-data[column].min())/(data[column].max()-data[column].min()) 

         return
        
    def box_plot(self):

         # load the data to a df
         data = pd.read_csv(self.csv_data)
         # copy the data to normalize
         normalization = data.copy().iloc[:, 1:]
         
         # normalize data
         self.normalize_data(normalization)
 
         # save new data to csv file
         normalization.to_csv(self.normalized_data)
         
         # make folder to put plots
         if not os.path.exists("Plots"):
             os.mkdir("Plots")
             
         normalization.plot(kind='box', subplots=False, sharey=False, figsize=(20,10))
         # save plot in Plots directory
         plt.savefig('Plots\Data_normalization_plot.jpg')

         return
     
    def bivariate_boxplot(self):
        # load the data to a df
        data = pd.read_csv(self.csv_data)
        
        # make folder to put plots
        if not os.path.exists("Plots"):
            os.mkdir("Plots")
        
        col = ['University Rating']

        for column in col:        
            sns.boxplot(x=column, y=data.columns[-1], data=data)
            # save plot
            plt.savefig('Plots\\bivariate_boxplot_'+column +'.jpg')        
            
        return    
     
    def heatmap_plot(self):
         # load the data to a df
         data = pd.read_csv(self.csv_data)
         new_data = data.iloc[:, 1:]
         fig, ax = plt.subplots(figsize=(15,10))
         sns.heatmap(data = new_data.corr(), annot=True, cmap='RdYlBu_r')
         
         # make folder to put plots
         if not os.path.exists("Plots"):
             os.mkdir("Plots")
         # save plots in Plots directory
         plt.savefig('Plots\Data_heatmap_plot.jpg')
         
         return    

    def find_missing_values(self):
        # load the data to a df
        data = pd.read_csv(self.csv_data)
        
        # make dictionary
        missings = {}
        values = []

        for item in data.columns:
            for i in data.index:
                if data.isnull()[item][i] == True:
                   values.append(i)
                   # add key, value in a dict
                   missings[item] = values
            # reset list
            values = []

        print(missings)        
       
        return
    
if __name__ == "__main__":
    ba = BasicAnalysis()
    #ba.scatter_plot()
    #ba.box_plot()
    ba.bivariate_boxplot()
    #ba.heatmap_plot()
    ba.find_missing_values()
    
    