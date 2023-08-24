import streamlit as st
from azure.storage.blob import BlobServiceClient


# Get Azure Storage account details from environment variables
azure_connection_string = "DefaultEndpointsProtocol=https;AccountName=mastergolfstorage;AccountKey=8gRRmfcAYMKhOxjNX5PIYrS6IFIFcx/Rzhx4wHtDbMuS6gY7ZIBXhMfi7LELh42FUUJ9UuZpGSBk+AStlPg4rw==;EndpointSuffix=core.windows.net"
azure_container_name = "mastergolfcontainer"

def main():
    st.title("File Upload to Azure Storage")

    # File upload section
    st.subheader("Upload a file")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "xlsx", "pdf", "docx", "doc"])

    if uploaded_file is not None:
        # Upload the file to Azure Storage and display success message
        if upload_to_azure_storage(uploaded_file, uploaded_file.name):
            st.success("File upload successful!")
        else:
            st.error("File upload failed.")

def upload_to_azure_storage(file, file_name):
    try:
        # Create a BlobServiceClient object using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

        # Create a new blob client using the container name and the original file name
        blob_client = blob_service_client.get_blob_client(container=azure_container_name, blob=file_name)

        # Upload the file contents to Azure Storage
        blob_client.upload_blob(file, overwrite=True)

        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    main()

# import streamlit as st
# from azure.cosmos import CosmosClient, PartitionKey

# # Azure Cosmos DBの設定
# URL = 'https://adachitakehirodemo3.documents.azure.com:443/'
# KEY = 'C7Z6MXR3EUj5DGngcK4dF84ZZr0yfjPhZPCheo635tFgbUIbZ3GZJG3MWD3lis5PDkHAW63w7BAZACDbPuTKGw=='
# DATABASE_NAME = 'SampleTestDB'
# CONTAINER_NAME = 'Test'

# client = CosmosClient(URL, credential=KEY)
# database = client.get_database_client(DATABASE_NAME)
# container = database.get_container_client(CONTAINER_NAME)

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
#     container.upsert_item(item_body)
#     st.success(f"Uploaded data with key: {data_key}")

# # データの取得と表示
# st.subheader("Retrieve Data from Cosmos DB")
# query_key = st.text_input("Enter key to retrieve:")

# if st.button("Retrieve"):
#     query = f"SELECT * FROM c WHERE c.id = '{query_key}'"
#     results = list(container.query_items(query=query, enable_cross_partition_query=True))
    
#     if results:
#         st.write(results[0])
#     else:
#         st.warning(f"No data found for key: {query_key}")