import numpy as np
from matplotlib import pyplot as pl
import math

# Open the Data file field.irreg.txt for reading
with open('i170b1h0_t0.txt', 'r') as data_reader_1:
    with open('i170b2h0_t0.txt', 'r') as data_reader_2:
        with open('i170b3h0_t0.txt', 'r') as data_reader_3:
            with open('i170b4h0_t0.txt', 'r') as data_reader_4:

                # Reading i170b2h0_t0.txt file and split the data
                info_1 = []
                info_2 = []
                info_3 = []
                info_4 = []

                band_1 = [[0] * 500 for x in range(0, 500)]
                band_2 = [[0] * 500 for x in range(0, 500)]
                band_3 = [[0] * 500 for x in range(0, 500)]
                band_4 = [[0] * 500 for x in range(0, 500)]

                # replacing newline from all elements of list and splitting the strings into a list
                #for Band 1
                for row_line_1 in data_reader_1:
                    row_line1 = row_line_1.replace('"', '').replace("\n", "").split(',')
                    info_1.append(row_line1)

                # For band 2
                for row_line_2 in data_reader_2:
                    row_line2 = row_line_2.replace('"', '').replace("\n", "").split(',')
                    info_2.append(row_line2)

                # For band 3
                for row_line_3 in data_reader_3:
                    row_line3 = row_line_3.replace('"', '').replace("\n", "").split(',')
                    info_3.append(row_line3)

                # For band 4
                for row_line_4 in data_reader_4:
                    row_line4 = row_line_4.replace('"', '').replace("\n", "").split(',')
                    info_4.append(row_line4)



                # first value in a file is the value with coordinates (500, 1), the second with coordinates (500, 2), to (500, 500) and then (499, 1) and so on.
                # For band 1 array
                for row in range(0, 500):
                    for col in range(0, 500):
                        band_1[row][col] = float(info_1[499 - row][col])

                band_1_array = np.array(band_1)

                # for band 2 array
                for row2 in range(0, 500):
                    for col2 in range(0, 500):
                        band_2[row2][col2] = float(info_2[499 - row2][col2])

                band_2_array = np.array(band_2)

                # for band 3 array
                for row3 in range(0, 500):
                    for col3 in range(0, 500):
                        band_3[row3][col3] = float(info_3[499 - row3][col3])

                band_3_array = np.array(band_3)

                # for band 4 array
                for row4 in range(0, 500):
                    for col4 in range(0, 500):
                        band_4[row4][col4] = float(info_4[499 - row4][col4])

                band_4_array = np.array(band_4)



                # A. Min, Max , Mean , Variance for BAnd 2
                data_size_row = int(len(band_2_array))
                data_size_col = int(len(band_2_array[0]))


                # Maximum value
                def max_value(arr):
                    max_item = arr[0][0]
                    for k in range(data_size_row):
                        for l in range(data_size_col):
                            if (arr[k][l] > max_item):
                                max_item = arr[k][l]
                    return max_item


                p_max_val = max_value(band_2_array)
                print("Maximum value(for band 2)", p_max_val)


                # Minimum value of array
                def min_value(arr):
                    min_item = arr[0][0]
                    for k in range(data_size_row):
                        for l in range(data_size_col):
                            if (arr[k][l] < min_item):
                                min_item = arr[k][l]
                    return min_item


                q_min_val = min_value(band_2_array)
                print("Minimum value(for band 2)", q_min_val)

                # Calculating mean without inbuilt function
                sum = 0
                for row in range(data_size_row):
                    for col in range(data_size_col):
                        sum += band_2_array[row][col]

                mean = round((1 * sum) / (data_size_col * data_size_row), 11)
                print("Mean after rounding is(for band 2):{mean}".format(mean= mean))

                # Calculating Variance without using inbuilt function
                sum1 = 0
                for row_v in range(data_size_row):
                    for col_v in range(data_size_col):
                        sum1 += abs(((band_2_array[row_v][col_v] - mean) ** 2))

                variance_1 = round(1 * sum1 / (data_size_col * data_size_row), 8)
                print("Variance after rounding is(for band 2): {variance}".format(variance=variance_1))


                # B. Profile line through the line with the maximum value of 2D data set
                # Reference: https://stackoverflow.com/questions/55284090/how-to-find-max-value-in-2d-array-with-index
                pl.figure(1)
                pl.title('Profile Line through max value')
                # finding maximum value with index
                max_val_for_line = np.where(band_2_array == max_value(band_2_array))
                #print("profile line maximum value", (max_val_for_line))
                plot_ax = pl.plot(band_2_array[max_val_for_line[0][0]], '-r')
                pl.yscale('log')
                pl.xlabel("Pixel values", fontsize=10)
                pl.ylabel("Pixel count", fontsize=10)



                #C. Histogram of the 2D data set
                #took help from: https://stackoverflow.com/questions/8822370/plot-line-graph-from-histogram-data-in-matplotlib

                pl.figure(2)
                pl.title('Histogram as line graph ')
                histo, e_bin_cent = np.histogram(band_2_array, bins=50)
                pl.plot((0.5 * (e_bin_cent[1:] + e_bin_cent[:-1])), histo, '-', color='black')
                pl.xlabel("X axis", fontsize=10)
                pl.ylabel("Y axis", fontsize=10)


                #D.Rescale values to range between 0 and 255 using your own transformation and display on your screen. Add a legend showing the new maximum and minimum value.
                # Reference : https://stackoverflow.com/questions/49922460/scale-a-numpy-array-with-from-0-1-0-2-to-0-255
                another_copy = []
                another_copy[:] = band_2_array
                copy_array_2 = np.array(another_copy)
                # scaling in 0 to 11
                for m in range(0, len(copy_array_2)):
                    for n in range(0, len(copy_array_2[0])):
                        # Formula for finding Non-linear value is s = c*log(r+1) where c is constant
                        copy_array_2[m][n] = (math.log(copy_array_2[m][n]+1, 2.0))

                # find maximum and minimum value on scale of 0-11 for 0 to 255 scaling
                min_val = min_value(copy_array_2)
                max_val = max_value(copy_array_2)

                # for scaling from 0-11 to 0-255
                c = (1 / (max_val - min_val)) * 255
                for m in range(0, len(copy_array_2)):
                    for n in range(0, len(copy_array_2[0])):
                        copy_array_2[m][n] = c * (copy_array_2[m][n] - min_val)

                pl.figure(3)
                pl.title('Rescaling using Non-Linear Transformation')
                pl.imshow(copy_array_2, cmap='gist_gray')
                pl.xlabel("X axis", fontsize=10)
                pl.ylabel("Y axis", fontsize=10)
                colourbar = pl.colorbar()

                colourbar.set_label("Range", fontsize=10)


                # E. Carry out a Histogram equalization on each of the four bands and display on your screen.
                # Function to count occurances of each elements using dictionary and calculating Cumulative Distribution Frequency

                def histogram_equalizaion(arr):
                #reference: https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray-in-python
                    unique_data_counts = {}
                    probability_key_list = {}
                    total_num_elements = 250000
                    unique_data_counts = dict(zip(*np.unique(arr, return_counts=True)))

                    # Finding probability of each element in the dictionary[keys, values]
                    for key in unique_data_counts:
                        probability_key_list[key] = unique_data_counts[key] / total_num_elements

                    # Getting a list of all uniques occurances of elements from dictionary[keys, values]
                    probability_of_occurances = []
                    data_list = []
                    for k, v in probability_key_list.items():
                        key = k
                        value = v
                        probability_of_occurances.append(value)
                        data_list.append(key)

                    # Sum for Cumulative Distribution Frequency and
                    # Performing Cumulative Distribution Frequency * 255
                    cumulative_distribution = [0]
                    for i in range(1, len(probability_of_occurances)):
                        probability_of_occurances[i] += probability_of_occurances[i - 1]
                        cumulative_distribution.append(int(np.round(probability_of_occurances[i] * 255)))
                    cumulative_distribution[0] * probability_of_occurances[0] * 255

                    # Replace key values with cdf
                    oneDarray = arr.ravel()
                    for i in range(len(oneDarray)):
                        for j in range(len(data_list)):
                            if oneDarray[i] == data_list[j]:
                                oneDarray[i] = cumulative_distribution[j]

                    return np.reshape(oneDarray, (500, 500))


                # Histogram Equalization plotting

                band_equalization_1 = histogram_equalizaion(band_1_array)
                band_equalization_2 = histogram_equalizaion(band_2_array)
                band_equalization_3 = histogram_equalizaion(band_3_array)
                band_equalization_4 = histogram_equalizaion(band_4_array)

                pl.figure(4)

                pl.subplot(2,2,1)
                pl.title('Band 1 image')
                pl.imshow(band_equalization_1, cmap='gray')
                bar1= pl.colorbar()
                bar1.set_label("Range", rotation=270, fontsize=10)
                pl.tight_layout()
                pl.xlabel("RA", fontsize=10)
                pl.ylabel("DEC", fontsize=10)


                pl.subplot(2, 2, 2)
                pl.title('Band 2 image')
                pl.imshow(band_equalization_2, cmap='gray')
                bar2= pl.colorbar()
                bar2.set_label("Range", rotation=270, fontsize=10)
                pl.tight_layout()
                pl.xlabel("RA", fontsize=10)
                pl.ylabel("DEC", fontsize=10)
                
                

                pl.subplot(2, 2, 3)
                pl.title('Band 3 image')
                pl.imshow(band_equalization_3, cmap='gray')
                bar3 = pl.colorbar()
                bar3.set_label("Range", rotation=270, fontsize=10)
                pl.tight_layout()
                pl.xlabel("RA", fontsize=10)
                pl.ylabel("DEC", fontsize=10)
              

                pl.subplot(2, 2, 4)
                pl.title('Band 4 image')
                pl.imshow(band_equalization_4, cmap='gray')
                bar4 = pl.colorbar()
                bar4.set_label("Range", rotation=270, fontsize=10)
                pl.tight_layout()
                pl.xlabel("RA", fontsize=10)
                pl.ylabel("DEC", fontsize=10)
                
                

                # F. Combine the histo-equalized data set to an RGB-image (b4=r, b3=g, b1=b)

                # to merge all files(band 4, band 3, band 1)

                merge_bands = np.zeros((500, 500, 3), 'uint8')
                for i in range(0, 500):
                    for j in range(0, 500):
                        merge_bands[i][j][0] = band_equalization_4[i][j]
                        merge_bands[i][j][1] = band_equalization_3[i][j]
                        merge_bands[i][j][2] = band_equalization_1[i][j]

                pl.figure(5)
                pl.title('RGB image by combining the equalized data of band 4, band 3, band 1')
                pl.imshow(merge_bands)
                b = pl.colorbar()#b, orientation='vertical')
                b.set_label("Range", fontsize=10)
                pl.show()





