"""
Description:
The RasterConverter module provides a set of functions for efficient data conversion and manipulation of raster datasets.
"""

import numpy as np
import rasterio

def raster_list(file_path):
    """
    Read raster data from a file, convert NoData values to None, and convert the data into a Python list.

    Args:
        file_path (str): Path to the raster file.

    Returns:
        list: Raster data as a Python list with NoData values converted to None.
    """
    # Open the raster file
    dataset = rasterio.open(file_path)

    # Check if the dataset was opened successfully
    if dataset is None:
        raise Exception("Failed to open the raster file.")

    # Get the raster band
    band = dataset.read(1)

    # Get the NoData value
    nodata_value = dataset.nodata

    # Get the number of rows and columns of raster data
    rows, cols = band.shape

    # Convert raster data to matrix
    raster_matrix = band.reshape(rows, cols)

    # Converts data types to object types to support storing None
    raster_matrix = raster_matrix.astype(object)

    # Convert NoData values to None
    raster_matrix[raster_matrix == nodata_value] = None

    # Convert NumPy array to a Python list
    raster_list = [[raster_matrix[row][col] for col in range(cols)] for row in range(rows)]

    return raster_list


def process_raster_data(input_raster_path, output_raster_path, new_data, nodata_value):
    """
    Create a single-band raster template based on the input raster, process the raster data by replacing pixel values with the new data.

    Args:
        input_raster_path (str): Path to the original raster file.
        output_raster_path (str): Path to save the output raster file.
        new_data (list): New data in the form of a 2D list.
        nodata_value (num): NoData value in new_data.

    Returns:
        None
    """
    # Open the original raster dataset
    input_raster = rasterio.open(input_raster_path)

    # Create a new raster from the original raster dataset
    output_raster = rasterio.open(output_raster_path, "w", driver="GTiff",
                                  height=input_raster.height, width=input_raster.width, count=1,
                                  dtype=input_raster.dtypes[0], crs=input_raster.crs, transform=input_raster.transform,
                                  nodata=input_raster.nodata)

    # Replace pixel values with new data，and set the NoData value
    masked_array = new_data == nodata_value
    output_raster.write(np.array(new_data), 1, masked=masked_array)

    print(f"Processed raster data saved to {output_raster_path}.")

    # Close datasets
    input_raster.close()
    output_raster.close()
