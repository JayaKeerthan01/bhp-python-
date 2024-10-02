import json
import pickle
import numpy as np
import sklearn

__data_columns=None
__location=None
__model=None

def get_estimated_price(location,sqft,bath,bhk):
    try:
        loc_ind=__data_columns.index(location.lower())
    except:
        loc_ind=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk

    if loc_ind>=0:
        x[loc_ind]=1
    return round(__model.predict([x])[0],2)


def get_location_names():
    load_saved_artifacts()
    return __location
def load_saved_artifacts():
    global __data_columns
    global __location
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
        __location=__data_columns[3:]
    with open("./artifacts/bengaluru_house_prices.pickle","rb") as f:
        __model=pickle.load(f)



if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("2nd stage nagarbhavi",1000,2,2))




























