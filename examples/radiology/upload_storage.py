#!/bin/env python

# This is an example script to upload data (images, text, metadata) to
# google cloud storage and datastore. We use the wordfish standard,
# assuming the data has been de-identified. The first step 
# below we structure our dataset. This also validates that it's
# formatted correctly. In the second step, we use the radiology
# client to upload the structures to storage and datastore.


from som.api.google.storage.radiology import Client
from som.wordfish.structures import structure_dataset

radiology_client = Client()
compressed_data = '../wordfish-standard/demo/cookies.zip'
#compressed_data = '../../../wordfish-standard/demo/cookies.zip'
structures = structure_dataset(compressed_data,clean_up=False)
response = radiology_client.upload_dataset(structures)
