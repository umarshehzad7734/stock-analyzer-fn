#function_app.py
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


@app.blob_trigger(arg_name="myblob", path="stock-data/{name}",
                               connection="BlobStorageConnectionString") 
def process_stock_file(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")



@app.blob_trigger(arg_name="myblob", path="stock-data/{name}",
                               connection="DefaultEndpointsProtocol=https;AccountName=stockanalyzerdatastore;AccountKey=EEYwQlmLSZXbE09dCfTxEs6ZV0ph06r72kuVR5lqTvPkzDfK3e+P5rcbijY911TG5fJEtLyzCn6K+AStSlcTMA==;EndpointSuffix=core.windows.net") 
def process_stock_file(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")



@app.blob_trigger(arg_name="myblob", path="stock-data/{name}",
                               connection="BlobStorageConnectionString") 
def process_stock_file(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")



@app.blob_trigger(arg_name="myblob", path="stock-data/{name}",
                               connection="BlobStorageConnectionString") 
def process_stock_file(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")



@app.blob_trigger(arg_name="myblob", path="stock-data/{name}",
                               connection="BlobStorageConnectionString") 
def analyze_stock_file(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
