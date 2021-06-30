import numpy as np
from matplotlib import pyplot as pl
import matplotlib.colors


# Open the Data file field.irreg.txt for reading
with open('field2.irreg.txt', 'r') as data_reader:

    # reading data from data set line and return all lines as a list using readlines
    data_list = data_reader.readlines()

    # removing first 6 elements of the data_list
    del data_list[0:6]
    info = []
    data_ar = []

    # replacing newline from all elements of list and splitting the strings into a list
    for row_line in data_list:
        row_line = row_line.strip()
        info.append(row_line.split(" , "))

    # Now converting List info into array by splitting columnwise and converting into float each element of list
    for r in info:
        for item in r:
            data_ar += [[float(a) for a in item.split()]]
    final_float_array = np.asarray(data_ar)
    # print(final_float_array)

    # splitting to 6 different columns(x,y,z,u,v) and plotting
    x, y, z, u, v, w = final_float_array[:,0], final_float_array[:,1], final_float_array[:,2], final_float_array[:,3], final_float_array[:,4], final_float_array[:,5]
    hypoth = np.hypot(u, v)

    #Scalaring data for rgba color mapping by using data normalization and using colormap(cmap) to map normalized data into rgba pattern
    # reference (https://matplotlib.org/3.1.1/api/cm_api.html), (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html)
    clr_arrow = matplotlib.colors.LinearSegmentedColormap.from_list("", ["Black", "purple", "red", "orange"])
    normalize_axis = pl.Normalize()
    pl.quiver(x, y, u, v, scale=15, color=clr_arrow(normalize_axis(y)))
    colourbar = pl.colorbar(matplotlib.cm.ScalarMappable(cmap=clr_arrow, norm=normalize_axis))
    colourbar.set_label("Flow Velocity", fontsize=20)
    colourbar.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    colourbar.set_ticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    pl.title("Vector Field Visualization", fontsize=15)
    pl.xlabel("X Equivalent of Vectors", fontsize=10)
    pl.ylabel("Y Equivalent of Vectors", fontsize=10)
    pl.show()









