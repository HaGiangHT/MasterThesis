from lightly.api import ApiWorkflowClient

# Create the Lightly client to connect to the API.
dataset_id = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be").get_datasets_by_name(f"central")[0].id
client = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be", dataset_id=dataset_id)

# Get all the tags for this dataset
tags = client.get_all_tags()
filename = client.export_filenames_by_tag_name(tags[0].name)
print(tags[0].name)
with open(f"./filenames/filenames-of-{tags[0].name}.txt", "w") as f:
         f.write(filename)

