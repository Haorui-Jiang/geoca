"""
Description:
The RasterConverter module provides a set of functions for efficient data conversion and manipulation of raster datasets.
"""

import numpy as np
from osgeo import gdal

def raster_list(file_path):
    """
    Read raster data from a file, convert NoData values to None, and convert the data into a Python list.

    Args:
        file_path (str): Path to the raster file.

    Returns:
        list: Raster data as a Python list with NoData values converted to None.
    """
    # Open the raster file
    dataset = gdal.Open(file_path)

    # Check if the dataset was opened successfully
    if dataset is None:
        raise Exception("Failed to open the raster file.")

    # Get the raster band
    band = dataset.GetRasterBand(1)

    # Get the NoData value
    nodata_value = band.GetNoDataValue()

    # Read the raster data as a NumPy array
    raster_data = band.ReadAsArray()

    # Convert NoData values to None
    raster_data = np.where(raster_data == nodata_value, None, raster_data)

    # Convert NumPy array to a Python list
    data_list = raster_data.tolist()

    return data_list

def process_raster_data(input_raster_path, output_raster_path, new_data):
    """
    Create a raster template based on the input raster, process the raster data by replacing pixel values with the new data.

    Args:
        input_raster_path (str): Path to the original raster file.
        output_raster_path (str): Path to save the output raster file.
        new_data (List): New data in the form of a 2D list.

    Returns:
        None
    """
    # Open the original raster dataset
    input_raster = gdal.Open(input_raster_path, gdal.GA_ReadOnly)

    # Read basic information from the original raster dataset
    projection = input_raster.GetProjection()
    geotransform = input_raster.GetGeoTransform()
    band_count = input_raster.RasterCount
    data_type = input_raster.GetRasterBand(1).DataType

    # Create a new raster dataset
    driver = gdal.GetDriverByName("GTiff")
    output_raster = driver.Create(output_raster_path, input_raster.RasterXSize, input_raster.RasterYSize, band_count, data_type)

    # Set the projection and geotransform parameters
    output_raster.SetProjection(projection)
    output_raster.SetGeoTransform(geotransform)

    input_band = input_raster.GetRasterBand(1)
    output_band = output_raster.GetRasterBand(1)
    array = input_band.ReadAsArray()

    # Replace pixel values with new data
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i, j] = new_data[i][j]
    
    # output_array = output_array.astype(int)   # 将矩阵数据格式转换为整数
    output_band.WriteArray(array)

    # Set specific values to NoData
    no_data_value = 0
    output_raster.GetRasterBand(1).SetNoDataValue(no_data_value)

    print(f"Processed raster data saved to {output_raster_path}.")

    # Close the datasets
    input_raster = None
    output_raster = None
