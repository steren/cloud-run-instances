from google.cloud import run_v2

client = run_v2.InstancesClient()

project_id = "steren-run"
location = "europe-west9"
image = "python" # Official Python image from DockerHub

operation = client.create_instance(
    request={
        "parent": f"projects/{project_id}/locations/{location}",
        "instance": {
            "containers": [{"image": image}]
        }
    }
)

print("Operation started. Waiting for completion...")
response = operation.result()
print(f"Successfully deployed instance: {response.name}")
