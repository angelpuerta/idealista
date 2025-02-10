from dataclasses import dataclass
import os
import numpy as np
from sklearn import clone
from sklearn.compose import ColumnTransformer
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
import logging
import pandas

from model.transformers import BasicTransformer, MapFloorValues, StatusValues

categorical_features = ['district', 'neighborhood', 'propertyType']
binary_features = ['newDevelopment', 'exterior', 'hasLift', 'garage', 'storage_room']
numerical_features = ['bathrooms', 'size', 'rooms']


preprocessor = ColumnTransformer(
    transformers=[
        ('bin', 'passthrough', binary_features),  # Keep numerical features as they are
        ('num', 'passthrough', numerical_features),
        ('status', StatusValues(), ['status']),
        ('floor', MapFloorValues(), ['floor']),
        ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=np.nan), categorical_features)  # One-hot encode categorical features
    ]
)

pipeline = Pipeline(
        steps=[
        ('basic_transformation', BasicTransformer()),
        ('preprocessor', preprocessor),
        ]
    )

@dataclass
class Model:
    name: str
    output: str

def _load_regressor(path):
    if not os.path.exists(path):
        logging.error(f"The path {path} does not exist")
        return
    return joblib.load(path)


def evaluate_model(dataframe, model):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, model.name)
    model_pipeline = clone(pipeline)
    model_pipeline.fit(dataframe)
    model_pipeline.steps.append(('regressor', _load_regressor(path)))

    predictions = model_pipeline.predict(dataframe) 
    dataframe[model.output] = predictions
    return dataframe

def evaluate_models(list, models):
    dataframe = pandas.DataFrame(list)
    for model in models:
        evaluate_model(dataframe, model)
    return iter(dataframe.to_dict(orient="records"))
