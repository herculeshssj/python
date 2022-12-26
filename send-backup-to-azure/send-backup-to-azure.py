import os, sys
from azure.storage.blob import BlobServiceClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Set env variables
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    local_file_name = sys.argv[1]

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    #container_name = 'herculeshssj-vm-03'
    container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

    # Set a local directory to hold blob data
    local_path = "/data"

    # Create a file in the local data directory to upload and download
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

    print("Done!")

except Exception as ex:
    print('Exception:')
    print(ex)