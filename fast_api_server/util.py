import json
import pickle
import sklearn
import numpy as np

locations = None
data_columns = None
model = None

def get_location_names():
    load_saved_artifacts()
    return locations

def load_saved_artifacts():
    global locations, data_columns, model

    with open("artifacts/columns.json", 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]

    with open("artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        model = pickle.load(f)


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1


    return round(model.predict([x])[0], 2)

if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
