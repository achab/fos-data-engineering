import glob
import json

import pandas as pd


def get_all_filenames():
    pass

def transform_one_file(filename):
    pass

def merge_all_files_in_pandas_df(files):
    pass

def drop_duplicates(df_):
    pass

def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)


main()