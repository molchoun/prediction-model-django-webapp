import pandas as pd
import pickle
import os
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from sklearn.compose import ColumnTransformer


def get_coordinates(address):
    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    if location is not None:
        return location.latitude, location.longitude
    else:
        return None, None


def calculate_distance(lat, long):
    center = (40.1825599, 44.5115911)
    coords = (lat, long)
    distance = geodesic(coords, center).km
    return distance


def process_data(data):
    columns = ['construction_type', 'new_construction', 'elevator', 'floors_in_the_building',
               'floor_area', 'number_of_rooms', 'number_of_bathrooms', 'ceiling_height', 'floor', 'balcony',
               'furniture', 'renovation', 'Latitude', 'Longitude', 'distance']
    categorical_features = ["construction_type", "balcony", "renovation", "furniture"]

    prediction_dict = {key: value for key, value in data.items() if key in columns}
    prediction_dict['Latitude'], prediction_dict['Longitude'] = get_coordinates(data['address'])
    prediction_dict['distance'] = calculate_distance(prediction_dict['Latitude'], prediction_dict['Longitude'])

    with open(os.path.join(os.path.dirname(__file__), 'encoder.pkl'), 'rb') as t:
        encoder = pickle.load(t)

    df_from_dict = pd.DataFrame.from_dict([prediction_dict])
    transformer = ColumnTransformer(
        [
            ("one_hot",
             encoder,
             categorical_features)
        ],
        remainder="passthrough")
    transformed_df = transformer.fit_transform(df_from_dict)
    df = pd.DataFrame(transformed_df)

    return df


def get_model():
    with open(os.path.join(os.path.dirname(__file__), 'gbr-prediction-model.pkl'), 'rb') as f:
        model = pickle.load(f)
    return model
