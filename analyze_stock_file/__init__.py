import logging
import azure.functions as func
import pandas as pd
import joblib
import os

app = func.FunctionApp()

@app.function_name(name="analyze_stock_file")
@app.blob_trigger(arg_name="myblob",
                  path="stock-data/{name}",
                  connection="BlobStorageConnectionString")
def analyze_stock(myblob: func.InputStream):
    logging.info(f"Triggered by file: {myblob.name}")
    try:
        df = pd.read_csv(myblob)
        logging.info(f"📊 Columns: {df.columns.tolist()}")

        avg = df['Price'].mean()
        max_val = df['Price'].max()
        min_val = df['Price'].min()

        model_path = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
        model = joblib.load(model_path)
        prediction = model.predict([[len(df) + 1]])[0]

        logging.info(f"📈 Avg: {avg:.2f}, Max: {max_val:.2f}, Min: {min_val:.2f}")
        logging.info(f"📌 Prediction: {prediction:.2f}")

    except Exception as e:
        logging.error(f"❌ Error: {e}")
