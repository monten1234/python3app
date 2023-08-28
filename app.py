import streamlit as st
from azure.cosmos import CosmosClient, PartitionKey
import azure.cosmos.cosmos_client as cosmos_client

# Azure Cosmos DBの設定
URL = 'https://adachitakehirodemo3.documents.azure.com:443/'
KEY = 'C7Z6MXR3EUj5DGngcK4dF84ZZr0yfjPhZPCheo635tFgbUIbZ3GZJG3MWD3lis5PDkHAW63w7BAZACDbPuTKGw=='
DATABASE_NAME = 'SampleTestDB'
CONTAINER_NAME = 'Test'

client = CosmosClient(URL, credential=KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

st.title("Azure Cosmos DB with Streamlit!")

# データのアップロード
st.subheader("Upload Data to Cosmos DB")
data_key = st.text_input("Enter a key:")
data_value = st.text_input("Enter a value:")

if st.button("Upload"):
    item_body = {
        "id": data_key,
        "value": data_value
    }
    container.upsert_item(item_body)
    st.success(f"Uploaded data with key: {data_key}")

# データの取得と表示
st.subheader("Retrieve Data from Cosmos DB")
query_key = st.text_input("Enter key to retrieve:")

if st.button("Retrieve"):
    query = f"SELECT * FROM c WHERE c.id = '{query_key}'"
    results = list(container.query_items(query=query, enable_cross_partition_query=True))
    
    if results:
        st.write(results[0])
    else:
        st.warning(f"No data found for key: {query_key}")

# import streamlit as st
# import azure.cosmos.cosmos_client as cosmos_client
# import azure.cosmos.errors as errors
# import azure.cosmos.http_constants as http_constants

# import os
# url = os.environ['https://adachitakehirodemo3.documents.azure.com:443/']
# key = os.environ['C7Z6MXR3EUj5DGngcK4dF84ZZr0yfjPhZPCheo635tFgbUIbZ3GZJG3MWD3lis5PDkHAW63w7BAZACDbPuTKGw==']
# client = cosmos_client.CosmosClient(url, {'masterKey': key})

# database_id = 'SampleTestDB'
# container_id = 'Test'
# # container = client.ReadContainer("dbs/" + database_id + "/colls/" + container_id)

# st.title("Azure Cosmos DB with Streamlit")

# # データのアップロード
# st.subheader("Upload Data to Cosmos DB")
# data_key = st.text_input("Enter a key:")
# data_value = st.text_input("Enter a value:")

# if st.button("Upload"):
#     item_body = {
#         "id": data_key,
#         "value": data_value
#     }
#     client.UpsertItem("dbs/" + database_id + "/colls/" + container_id,item_body)
#     st.success(f"Uploaded data with key: {data_key}")

# import streamlit as st
# from azure.cosmos import CosmosClient

# # Cosmos DBの接続情報
# URL = "YOUR_COSMOS_DB_URL"
# KEY = "YOUR_COSMOS_DB_KEY"
# DATABASE_ID = "YOUR_DATABASE_ID"
# COLLECTION_ID = "YOUR_COLLECTION_ID"

# # Cosmos DBクライアントの初期化
# client = CosmosClient(URL, {'masterKey': KEY})

# # Streamlit アプリ
# def main():
#     st.title('Cosmos DB Data Uploader')
    
#     # ユーザー入力を収集
#     item_id = st.text_input('Enter Item ID')
#     product_name = st.text_input('Enter Product Name')
#     product_model = st.text_input('Enter Product Model')

#     if st.button('Upload to Cosmos DB'):
#         if item_id and product_name and product_model:
#             item = {
#                 'id': item_id,
#                 'productName': product_name,
#                 'productModel': product_model
#             }

#             # アイテムをCosmos DBにアップロード
#             client.UpsertItem("dbs/" + DATABASE_ID + "/colls/" + COLLECTION_ID, item)
#             st.success('Data uploaded successfully!')
#         else:
#             st.error('Please fill all fields.')

# if __name__ == "__main__":
#     main()
