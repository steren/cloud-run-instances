import random
from google.cloud import run_v2

client = run_v2.InstancesClient()

project_id = "steren-run"
location = "europe-west9"
instance_id = f"my-instance-{random.randint(100, 999)}"
image = "us-docker.pkg.dev/cloudrun/container/hello"

operation = client.create_instance(
    request={
        "parent": f"projects/{project_id}/locations/{location}",
        "instance_id": instance_id,
        "instance": {
            "containers": [{"image": image}]
        }
    }
)

print(f"Creating instance: {instance_id}...")
response = operation.result()
print(f"Successfully deployed instance: {response.name}")
