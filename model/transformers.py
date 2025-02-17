from datetime import datetime
from sklearn.base import BaseEstimator, TransformerMixin
import re
import pandas as  pd
import numpy as np

class StatusValues(BaseEstimator, TransformerMixin):
    def __init__(self):
        # Define the mapping of values to integers
        self.mapping = {
            'renew': 1,
            'unknown': 0,
            'newdevelopment': 3,
            'good': 2
        }

    def get_feature_names_out(self, input_features=None):
        return input_features

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            return X.replace(self.mapping)
        else:
            raise ValueError("Input should be a pandas DataFrame.")
    
class MapFloorValues(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self  # Nothing to fit here
    
    def get_feature_names_out(self, input_features=None):
        return input_features
    
    def _map_values(self, x):
        if isinstance(x, str) and x.isdigit():
            return int(x) 
        if pd.isna(x):
            return np.nan
        match x: 
            case 'bj':
                return -1
            case 'en':
                return 0
            case 'ss':
                return -1
            case 'st':
                return -1
            case '-1':
                return -1
            case '-2':
                return -2
            case '':
                return 0
            case _:
                assert False, f"The value {x} of type {type(x)} does not comply"

    def transform(self, X):
        return X.map(self._map_values)

class BasicTransformer(TransformerMixin, BaseEstimator):
    def __init__(self, training=False):
        super().__init__()
        self.training = training

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X = self._transform_hasLift(X)
        X = self._transformed_floor(X)
        X = self._add_is_bassement(X)
        X = self._add_garage(X)
        X = self._add_storage_room(X)
        X = self._add_suite_bathroom(X)
        X = self._add_janitor(X)
        X = self._add_pool(X)
        X = self._add_animal(X)
        X = self._date_to_unix(X)
        X = self._add_bare_title(X)
        X = self._remove_terms(X, ['okupada', 'subasta', 'ocup'])

        if not self.training:
            drop_indices = set(
            X.index[X['bare_tittle'] == 1].tolist() + 
            X.index[X['remove_by_term'] == 1].tolist() 
            )
            X = X.drop(index=drop_indices)
        return X

    def _transform_hasLift(self, df):
        df.loc[((df['propertyType'].isin(['flat', 'penthouse', 'studio'])) & df['hasLift'].isna()), 'hasLift'] = False
        return df

    def _transformed_floor(self, df):
        df.loc[((df['propertyType'].isin(['flat', 'penthouse', 'studio'])) & df['floor'].isna()), 'floor'] = '-1'
        return df

    def _add_bare_title(self, df):
        df['bare_tittle'] = df['description'].fillna('').str.contains('nuda', case=False).astype(int)
        return df

    def _add_garage(self, df):
        df['garage'] = df['description'].fillna('').str.contains('garaje', case=False).astype(int)
        return df

    def _add_storage_room(self, df):
        df['storage_room'] = df['description'].fillna('').str.contains('trastero', case=False).astype(int)
        return df

    def _add_suite_bathroom(self, df):
        df['suite_bath'] = df['description'].fillna('').str.contains('suite', case=False).astype(int)
        return df

    def _add_janitor(self, df):
        df['janitor'] = df['description'].fillna('').str.contains('portero', case=False).astype(int)
        return df

    def _add_pool(self, df):
        df['pool'] = df['description'].fillna('').str.contains('piscina', case=False).astype(int)
        return df

    def _add_animal(self, df):
        df['animal'] = df['description'].fillna('').str.contains('animal', case=False).astype(int)
        return df

    def _remove_terms(self, df, terms):
        pattern = '|'.join(map(re.escape, terms))
        df['remove_by_term'] = df['description'].str.contains(pattern, case=False, na=False)
        return df

    def _add_is_bassement(self, df):
        df['isBassement'] = df['floor'].fillna('None').isin(['bj', 'ss', 'st', '-1', '-2', 'en']).astype(int)
        return df

    def _date_to_unix(self, df):
        df['created'] = df['created'].map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timestamp())
        return df

def remove_index(X, y):
    drop_indices = set(
            X.index[X['bare_tittle'] == 1].tolist() + 
            X.index[X['remove_by_term'] == 1].tolist()
        )
    return X.drop(index=drop_indices), y.drop(index=drop_indices)