import pandas as pd
import numpy as np
import xgboost as xgb

def transform(items):
    df = pd.DataFrame(items, index=[0])
    dummies_frame = pd.read_csv("final_columns.csv")
    # print(df.reindex(columns = dummies_frame.columns, fill_value=0))
    new_item = pd.get_dummies(df).reindex(columns=dummies_frame.columns,fill_value=0)
    xgb_model = xgb.Booster()
    xgb_model.load_model("hdb_model.bst")
    xginput = xgb.DMatrix(new_item.values)
    print(xgb_model.predict(xginput))
    price_pred = xgb_model.predict(xginput)
    return price_pred