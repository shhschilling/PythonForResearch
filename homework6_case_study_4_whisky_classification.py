#------------------------------------------------
# Homework 6 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
# Whisky classification
#------------------------------------------------

#Exercise 1--------------------------------------
from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Let's plot a simple 5x5 grid of squares, alternating in color as red and blue.
plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# How do we tell Bokeh to plot each point in a grid?  Let's use a function that
# finds each combination of values from 1-5.
from itertools import product

grid = list(product(plot_values, plot_values))
# The first value is the x coordinate, and the second value is the y coordinate.
# Let's store these in separate lists.

#zip(*zipped) means "feed each element of zipped as an argument to zip"
xs, ys = zip(*grid) #*indicates to UNZIP a list



# Now we will make a list of colors, alternating between red and blue.

colors = [plot_colors[i%2] for i in range(len(grid))]

# Finally, let's determine the strength of transparency (alpha) for each point,
# where 0 is completely transparent.

alphas = np.linspace(0, 1, len(grid))

# Bokeh likes each of these to be stored in a special dataframe, called
# ColumnDataSource.  Let's store our coordinates, colors, and alpha values.
source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    })


#Exercise 2--------------------------------------
cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]


#Create a dictionary region_colors with regions as keys and cluster_colors as values.
#dictionary = dict(zip(keys, values))
# https://docs.python.org/3/library/stdtypes.html#dict
#region_colors is a dictionary with keys regions and values cluster colors
region_colors= dict(zip(regions, cluster_colors))
print(region_colors)


#Exercise 3--------------------------------------
import pandas as pd
import numpy as np

#create whisky and correlations
whisky=pd.read_csv("whiskies.txt")
whisky["region"]=pd.read_csv("regions.txt")
whisky['Group']=pd.Series(model.row_labels_,index=whisky.index)
flavours=whisky.iloc[:,2:14]
corr_flavours=pd.DataFrame.corr(flavours) #correation between flavours
test=flavours.transpose()
correlations=pd.DataFrame.corr(test) #flavour correlation between distilleries


from sklearn.cluster.bicluster import SpectralCoclustering
model=SpectralCoclustering(n_clusters=6,random_state=0)
model.fit(correlations)

#add "Group" resulting from spectral clustering to whisky data frame
whisky['Group']=pd.Series(model.row_labels_,index=whisky.index)
whisky=whisky.ix[np.argsort(model.row_labels_)]#order the rows by group label
whisky=whisky.reset_index(drop=True)


type(correlations)
#Transform pandas data frame to numpy array
correlations=np.array(correlations)
type(correlations)

len(whisky.Distillery)
distilleries=whisky.Distillery
correlation_colors = [] #Initialize list
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i,j]<0.7 :                    # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if  whisky.loc[whisky.index[i], 'Group'] ==  whisky.loc[whisky.index[j], 'Group']:           # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.



#Exercise 4--------------------------------------
from bokeh.models import HoverTool, ColumnDataSource
source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "correlations": correlations.flatten() #transforms numpy array to list
    })



#Exercise 6--------------------------------------
#

#give each region a number
#regin_colors is a dictionary with keys regions and values plot_colors
#here we loop over the keys (the regions) and write out the values

whiskyregions=list(whisky["region"])


#i is key and is a string!!!!
region_cols = [region_colors[i] for i in whiskyregions]

#Exercise 7--------------------------------------
whiskygroup=list(whisky["Group"])
classification_cols = [cluster_colors[i] for i in whiskygroup]
