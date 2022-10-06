from appwrite.client import Client
from appwrite.services.databases import Databases

def setup_client() -> Client:
  client = Client()

  (client
    .set_self_signed()
    .set_endpoint('https://localhost/v1') # Your API Endpoint
    .set_project('6332241e1e91b30cdb44') # Your project ID
    .set_key('d783d4e1ae2dc6ff25241c52a96f7438054c6a546e3f9e548d2c434b731138ab4f752dea1f1dea59465abe28e8ba5e65032499339436f8eb0cb6c22e4640e666bf7800d0b9a682643d3161bc069210e54e2da685fa9bca911ed43f584ba4a1eea1eca6c1071221d373e5c7ac9c53a4e6a73d33b74714cdb58cce4c3a6c89628a') # Your secret API key
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

  DATABASE_ID = '6332243c4a34567ece37'
  COLLECTION_ID = '6332245d234ad970aedd'
  OLD_ATTRIBUTE_KEY = 'name1'
  NEW_ATTRIBUTE_KEY = 'barbapapa'

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
