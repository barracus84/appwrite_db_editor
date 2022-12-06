from appwrite.client import Client
from appwrite.services.databases import Databases

def setup_client() -> Client:
  client = Client()

  (client
    .set_self_signed()
    .set_endpoint('https://localhost/v1') # Your API Endpoint
    .set_project('[PROJECT-ID]') # Your project ID
    .set_key('[SECRET-API-KEY]') # Your secret API key
  )

  return client

def create_string_attribute(*
  , databases: Databases
  , database_id: str
  , collection_id: str
  , key: str
  , size: int
  , required: bool
) -> dict:
  ''' Create string attribute '''
  return databases.create_string_attribute(database_id, collection_id, key, size, required)

def main():

  DATABASE_ID = '[DATABASE-ID]'
  COLLECTION_ID = '[COLLECTION-ID]'
  OLD_ATTRIBUTE_KEY = 'old_attribute_key'
  NEW_ATTRIBUTE_KEY = 'new_attribute_key'

  # setup client
  client = setup_client()

  databases = Databases(client)

  # list documents
  documents = databases.list_documents(DATABASE_ID, COLLECTION_ID)

  # scroll documents, update document new attribute value with old attribute value
  for doc in documents['documents']:
    document_id = doc['$id']
    old_attribute_value = doc[OLD_ATTRIBUTE_KEY]
    obj_update = {
      NEW_ATTRIBUTE_KEY: old_attribute_value
    }

    databases.update_document(DATABASE_ID, COLLECTION_ID, document_id, obj_update)

  databases.delete_attribute(DATABASE_ID, COLLECTION_ID, OLD_ATTRIBUTE_KEY)

if __name__ == "__main__":
    main()
