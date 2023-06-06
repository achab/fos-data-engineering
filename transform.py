import glob
import json

import pandas as pd


def get_all_filenames():
    files = glob.glob("raw_data_*.json")
    return files

def transform_one_file(filename):
    output = []
    with open(filename, "r") as f:
        data = json.load(f)
        for city, d in data.items():
            res = {
                "city": city,
                "latitude": d["latitude"],
                "longitude": d["longitude"],
                "temperature": d["current_weather"]["temperature"],
                "time": d["current_weather"]["time"]
            }
            output.append(res)
    return output

def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
    df = pd.DataFrame(output)
    return df

def drop_duplicates(df_):
    return df_.drop_duplicates()

def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)


main()