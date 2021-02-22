import pandas as pd
import glob
import os
import sys

# use the script to generate counts stops. Path to model train data and trip files need to be provided
#enter path to trip files here
data_path=""
#enter path to path_model_data(train/test).csv
path_model_data=""

#function to count stops and turns
def count_turns_stops(df):
    try:
        deg = 45
        bins = 10
        df["present"] = df["heading_degrees"]
        df = df.apply(pd.to_numeric)
        df.fillna(0, inplace=True)
        # Considering every event within 3 seconds to be same - taking (3)average and selecting every 3rd row
        df = df.rolling(bins).mean()
        df = df.iloc[::bins, :]
        df = df.apply(pd.to_numeric)
        df.fillna(0, inplace=True)
        df = df[list(df.columns)].astype(int)
        # Considering every event within 3 seconds to be same
        df.fillna(0, inplace=True)
        # Left & right turns
        df['turn_count'] = ((df.present.shift(1) - df.present).abs() > deg) & (df.present.shift(-1) == df.present)
        df['turn_count'] |= ((df.present.shift(-1) - df.present).abs() > deg) & (df.present.shift(1) == df.present)
        # peak turns
        df['turn_count'] |= ((df.present.shift(-1) - df.present).abs() > deg) & (
                (df.present.shift(1) - df.present).abs() > deg)
        # count_stops
        df["stop_count"] = (df.speed_meters_per_second.shift(-1) == df.speed_meters_per_second) & (
                df.speed_meters_per_second.shift(1) == df.speed_meters_per_second)
        return len(df[df.turn_count == True]), len(df[df.speed_meters_per_second == True]), df
    except Exception as e:
        print(e)
        return 0, 0, None

# for all files in train dat count turns and stops
def generate_features(feature_matrix_path):
    data = pd.read_csv(feature_matrix_path)
    nturns = []
    nstops = []
    for fl in data["filename"]:
        df = pd.read_csv(os.path.get_cwd() + "trip_data_test/" + fl)
        nt, ns, df2 = count_turns_stops(df)
        df2.to_csv(data_path + "trip_data_test/" + "parsed_" + fl)
        nturns.append(nt)
        nstops.append(ns)

    data["nturns"] = nturns
    data["nstops"] = nstops
    data.to_csv(feature_matrix_path[:-4] + "_features.csv")

if __name__ == "__main__":
    # Check if the path to files are filled before calling the function
    pass
    #generate_features(path_model_data)
