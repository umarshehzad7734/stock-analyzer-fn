
import logging
import azure.functions as func
import pandas as pd
import pickle
import io

app = func.FunctionApp()

# Load ML model globally (loads once per container start)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.function_name(name="analyze_stock_file")
@app.blob_trigger(arg_name="myblob", path="stock-data/{name}", connection="AzureWebJobsStorage")
@app.output_blob(arg_name="outputblob", path="stock-output/{name}", connection="AzureWebJobsStorage")
def main(myblob: func.InputStream, outputblob: func.Out[str]):
    logging.info(f"Blob trigger function processed blob: {myblob.name} ({myblob.length} bytes)")

    # Read CSV from blob input
    df = pd.read_csv(myblob)

    # Ensure expected columns
    if 'Open' not in df.columns or 'Close' not in df.columns:
        outputblob.set("Invalid input: Missing 'Open' or 'Close' columns.")
        return

    df['Predicted Close'] = model.predict(df[['Open']])
    result = df.to_csv(index=False)

    outputblob.set(result)
    logging.info("Prediction completed and output saved.")
