from dataclasses import dataclass
import os
import joblib
import logging
import pandas

from model.transformers import BasicTransformer, StatusValues, MapFloorValues


@dataclass
class Model:
    name: str
    output: str

def _load_pipeline(path):
    if not os.path.exists(path):
        logging.error(f"The path {path} does not exist")
        return
    return joblib.load(path)


def evaluate_model(dataframe, model):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, model.name)
    pipeline = _load_pipeline(path)

    dataframe_transformed = BasicTransformer().fit_transform(dataframe)
    predictions = pipeline.predict(dataframe_transformed)
    predictions_full = pandas.Series(pandas.NA, index=dataframe.index)
    predictions_full[dataframe_transformed.index] = predictions.reshape(-1, 1).flatten()
    dataframe[model.output] = predictions_full
    return dataframe

def evaluate_models(list, models):
    dataframe = pandas.DataFrame(list)
    for model in models:
        evaluate_model(dataframe, model)
    return dataframe.to_dict(orient="records")

if __name__ == "__main__":
    df = pandas.read_csv("output/sales/output.csv", sep='\t')
    data = evaluate_models(df, [Model("sales_model.pkl", "y_pred"), Model("rents_model.pkl", "pred_rents")])
    data = pandas.DataFrame(data)
    data.to_csv("test_model.csv")