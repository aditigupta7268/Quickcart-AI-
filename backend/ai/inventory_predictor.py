import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_inventory(data):

    df = pd.DataFrame(data)

    X = df[["day"]]

    y = df["sales"]

    model = LinearRegression()

    model.fit(X,y)

    prediction = model.predict([[30]])

    return float(prediction)