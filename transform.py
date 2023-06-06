import glob
import json

import pandas as pd


def get_all_filenames():
    # this function should return a list of filenames
    # you should look at glob library
    # Example: it should return ["raw_data_1686027160.json", "raw_data_1686027165.json", "raw_data_1686027170.json"]
    pass

def transform_one_file(filename):
    # this function should return a list of dictionaries
    # each dictionnary should look like that: { "city": city, "latitude": latitude, "longitude": longitude , "temperature": tempature, "time": time}
    pass

def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
    df = pd.DataFrame(output)
    return df

def drop_duplicates(df_):
    # drop duplicated rows using a function of pandas.DataFrame
    pass

def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)


main()