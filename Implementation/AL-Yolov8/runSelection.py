from lightly.api import ApiWorkflowClient
from lightly.openapi_generated.swagger_client import DatasetType
from lightly.openapi_generated.swagger_client import DatasourcePurpose
import json


# Create the Lightly client to connect to the API.
client = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be")

# Create a new dataset on the Lightly Platform.
#client.create_dataset(dataset_name="central", dataset_type=DatasetType.IMAGES)
#dataset_id = client.dataset_id

dataset_id = client.set_dataset_id_by_name(dataset_name="central", shared=False)

with open(f'./initial_balancing.json') as file:
    json_data = json.load(file)

person_value = json_data['person']
bicycle_value = json_data['bicycle']
car_value = json_data['car']
motorcycle_value = json_data['motorcycle']
bus_value = json_data['bus']
truck_value = json_data['truck']



# Configure the Input datasource.
client.set_local_config(
    relative_path="train",
    web_server_location="http://localhost:3456",
    purpose=DatasourcePurpose.INPUT,
)
# Configure the Lightly datasource.
client.set_local_config(
    relative_path="pred",
    web_server_location="http://localhost:3456",
    purpose=DatasourcePurpose.LIGHTLY,
)

scheduled_run_id = client.schedule_compute_worker_run(
    worker_config={
        "enable_training": False,
        "datasource": {
            "bypass_verify": True,
            "process_all": True
        },
        "shutdown_when_job_finished": True
    },
    selection_config={
        "n_samples": 1000,
        "strategies": [
            {
                # strategy to find diverse objects
                "input": {
                    "type": "EMBEDDINGS",
                    "task": "yolov8_detection",
                },
                "strategy": {
                    "type": "DIVERSITY",
                },
            },
            {
                # strategy to balance the class ratios
                "input": {
                    "type": "PREDICTIONS",
                    "name": "CLASS_DISTRIBUTION",
                    "task": "yolov8_detection",
                },
                "strategy": {
                    "type": "BALANCE",
                    "target": {
                        "person": person_value,
                        "bicycle": bicycle_value,
                        "car": car_value,
                        "motorcycle": motorcycle_value,
                        "airplane": 0,
                        "bus": bus_value,
                        "train": 0,
                        "truck": truck_value
                    },
                },
            },
            {
                # strategy to prioritize images with more objects
                "input": {
                    "type": "SCORES",
                    "task": "yolov8_detection",
                    "score": "object_frequency",
                },
                "strategy": {"type": "WEIGHTS"},
            },
            {
                # strategy to use prediction score (Active Learning)
                "input": {
                    "type": "SCORES",
                    "task": "yolov8_detection",
                    #"score": "objectness_least_confidence",
                    "score": "uncertainty_entropy",
                },
                "strategy": {"type": "WEIGHTS"},
            },
        ],
    },
    # lightly_config={
    #     "trainer": {
    #         "max_epochs": 20,
    #     },
    #     "loader": {"batch_size": 50},
    # },
)

# You can use this code to track and print the state of the Lightly Worker.
# The loop will end once the run has finished, was canceled, or failed.
print(scheduled_run_id)
for run_info in client.compute_worker_run_info_generator(scheduled_run_id=scheduled_run_id):
    print(f"Lightly Worker run is now in state='{run_info.state}' with message='{run_info.message}'")

if run_info.ended_successfully():
    print("SUCCESS")
else:
    print("FAILURE")
