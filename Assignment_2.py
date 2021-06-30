import numpy as np
from matplotlib import pyplot as pl
import matplotlib.colors
import math


#Reading raw iamge in bytes
with open("slice150.raw", 'rb') as data_reader:
    data_file = data_reader.read()
    #we read group of two bytes each from data_file and multiply the first value from each group with 16**2(to get 16 bit list) and combine them.
    data_list = [(data_file[i]+ data_file[i+1]*16**2) for i in range(0, len(data_file), 2)]

    # Convert to binary array of dimmension 512X512X
    data_array = np.array(data_list).reshape(-1, 512)
    print(data_array)

    # A part draw a profile line through line 256 of this 2D data set. Get size of rows and find the middle row that is 255 row and draw line
    data_size_col = int(len(data_array[0]))             #for total columns of 2d dataset
    data_size_row = int(len(data_array))                #for total rows of 2d dataset
    final_size = int(((data_size_row)/2)-1)

    # plot the graph in line style with color 'red'
    pl.figure(1)
    pl.title('Profile Line through 256')
    pl.plot(data_array[final_size], '-r')
    pl.xlabel("Pixel values", fontsize=10)
    pl.ylabel("Pixel count", fontsize=10)


    #B. Calculate the mean value and the variance value of this 2D data set
    # calculating mean without inbuilt function
    sum = 0
    for row in range (data_size_row):
        for col in range (data_size_col):
            sum += data_array[row][col]

    mean = (1 * sum)/(data_size_col * data_size_row)
    print("Mean is:", mean)


    # calculating Variance without using inbuilt function
    sum1 = 0
    for row_v in range(data_size_row):
        for col_v in range(data_size_col):
            sum1 += abs(((data_array[row_v][col_v] - mean)**2))

    variance_1 = round(1 * sum1/(data_size_col * data_size_row),5)
    print("Variance after rounding is: {variance}".format(variance=variance_1))


    # C. Display a histogram of this 2D data set (instead of bars you may use a line graph to link occurrences along
    # the x-axis).
    # took help from : https://stackoverflow.com/questions/8822370/plot-line-graph-from-histogram-data-in-matplotlib

    pl.figure(2)
    pl.title('Histogram as line graph ')
    histo, e_bin_cent = np.histogram(data_array, bins=150)
    pl.plot((0.5 * (e_bin_cent[1:] + e_bin_cent[:-1])), histo, '-', color='black')
    #pl.hist(data_array.flatten(), 130, histtype='step', color='orange')
    pl.xlabel("X axis", fontsize=10)
    pl.ylabel("Y axis", fontsize=10)


    #D. Rescale values to range between 0 and 255 using a linear transformation.
    # creating new copy of original array data_array
    b = []
    b[:] = data_array
    copy_array = np.array(b)

    #creating function to find maximum value in 2d dataset
    def max_value(arr):
        max_item = arr[0][0]
        for k in range(data_size_row):
            for l in range(data_size_col):
                if (arr[k][l] > max_item):
                    max_item = arr[k][l]
        return max_item

    p_max_val = max_value(copy_array)

    #Minimum value of array
    def min_value(arr):
        min_item = arr[0][0]
        for k in range(data_size_row):
            for l in range(data_size_col):
                if (arr[k][l] < min_item):
                    min_item = arr[k][l]
        return min_item


    q_min_val = min_value(copy_array)


    ##Following formula for linear transformation s = ((r-min)/(max-min)) * 255
    for i in range(len(copy_array)):
        for j in range(len(copy_array[0])):
            copy_array[i][j] = ((copy_array[i][j]-q_min_val)/ (p_max_val-q_min_val)) * 255

    pl.figure(3)
    pl.title('Linear Transformation')
    pl.imshow(copy_array, cmap='gist_gray', origin= 'lower')
    pl.xlabel("X axis", fontsize=10)
    pl.ylabel("Y axis", fontsize=10)



    #E. Rescale values to range between 0 and 255 using a different (e.g. non-linear) transformation.
    #Another copy of array for non-linear transformation
    another_copy = []
    another_copy[:] = data_array
    copy_array_2 = np.array(another_copy)

    #scaling in 0 to 11
    for m in range(0, len(copy_array_2)):
        for n in range(0, len(copy_array_2[0])):
            # Formula for finding Non-linear value is s = c*log(r+1) where c is constant
                copy_array_2[m][n] =  (math.log(copy_array_2[m][n]+1, 2.0))

    #find maximum and minimum value on scale of 0-11 for 0 to 255 scaling
    min_val = min_value(copy_array_2)
    max_val = max_value(copy_array_2)

    #for scaling from 0-11 to 0-255
    # Reference : https://stackoverflow.com/questions/49922460/scale-a-numpy-array-with-from-0-1-0-2-to-0-255
    c = (1/(max_val-min_val)) * 255
    for m in range(0, len(copy_array_2)):
        for n in range(0, len(copy_array_2[0])):
                copy_array_2[m][n] =  c * (copy_array_2[m][n] - min_val)

    #checking minimum and maximum value of new 2darray
    min_val = min_value(copy_array_2)
    max_val = max_value(copy_array_2)

    pl.figure(4)
    pl.title('Non-Linear Transformation')
    pl.imshow(copy_array_2, cmap='gist_gray', origin='lower')
    pl.xlabel("X axis", fontsize=10)
    pl.ylabel("Y axis", fontsize=10)




    #F. Use an 11x11 boxcar smoothing filter on the 2D data set.
    # function to calculate sum of 2d array
    def sum1(arr):
        sum_ar = 0
        for rs in range(len(arr)):
            for cs in range(len(arr[0])):
                sum_ar = sum_ar + arr[rs][cs]

        return sum_ar

    #creating another copy of original array
    another_copy_2 = []
    another_copy_2[:] = data_array
    copy_array_3 = np.array(another_copy_2)

    #for getting 11*11 boxcar filter
    for r_b in range(0, len(data_array)):
        for c_b in range(0, len(data_array[0])):
            sum_2 = (sum1(data_array[r_b:r_b + 11, c_b:c_b + 11]))/121
            copy_array_3[r_b:r_b+5, c_b:c_b+5] = sum_2

    pl.figure(5)
    pl.title('Using 11x11 Boxcar Filter')
    pl.imshow(copy_array_3, cmap='gist_gray', origin= 'lower')
    pl.xlabel("X axis", fontsize=10)
    pl.ylabel("Y axis", fontsize=10)


    #G. Use an 11x11 median filter on the 2D data set.
    #function for finding median in 2d array in rowsused.
    #Reference: https://github.com/vprusso/youtube_tutorials/blob/master/technical_interview/matrix_median.py

    def find_median(m_arr):
        new_l = []
        med = m_arr[0]
        for sort_row in range(len(m_arr)):
            new_l.extend(m_arr[sort_row])
        if len(m_arr) == 1:
            return med[len(med) // 2]
        else:
            new_l = sorted(new_l)

        return new_l[len(new_l) // 2]



    #creating another array copy of original array
    another_copy_3 = []
    another_copy_3[:] = data_array
    copy_array_4 = np.array(another_copy_3)

    #for getting 11*11 median filter
    for r_b in range(0, len(data_array)):
        for c_b in range(0, len(data_array[0])):
            sum_3 = (find_median(data_array[r_b:r_b + 11, c_b:c_b + 11])) / 121 #extracting mssk 11*11 by dividing by (11*11) after getting median of all elements
            copy_array_4[r_b:r_b + 5, c_b:c_b + 5] = sum_3      #putting values in middle position of new array that is at position 5

    pl.figure(6)
    pl.title('Using 11x11 median Filter')
    pl.imshow(copy_array_4, cmap='gist_gray', origin='lower')
    pl.xlabel("X axis", fontsize=10)
    pl.ylabel("Y axis", fontsize=10)
    pl.show()

    #I took help from net for the concept, but all the logic used is done by me.




