import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import minionsModule as mm


while(1):
    
    maxIdx, data = mm.minionsMaxChannel()
    fArray = mm.minionsMakeArray(data)
    
    plt.close()
    fig, ax = plt.subplots(figsize = (12, 7))
    df = np.array(fArray) # maximum 25, 25
    sns.heatmap(df, cmap ='jet', vmin=-15000)
    
    plt.draw()
    plt.pause(0.01)
    ax.clear()
    
 


