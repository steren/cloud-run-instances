from google.cloud import run_v2

def deploy_instance(project_id: str, location: str, instance_id: str, image: str):
    """
    Deploys a standalone Cloud Run Instance (not a Service or Job).
    
    Args:
        project_id: Google Cloud Project ID.
        location: Google Cloud Region (e.g., 'us-central1').
        instance_id: Unique identifier for the instance.
        image: Container image URI (e.g., 'us-docker.pkg.dev/cloudrun/container/hello').
    """
    client = run_v2.InstancesClient()

    # The location and project to create the instance in.
    # Format: projects/{project}/locations/{location}
    parent = f"projects/{project_id}/locations/{location}"

    # Build the instance configuration
    instance = {
        "containers": [
            {
                "image": image,
                "resources": {
                    "limits": {
                        "cpu": "1",
                        "memory": "512Mi"
                    }
                }
            }
        ]
    }

    # Initialize the request object
    request = run_v2.CreateInstanceRequest(
        parent=parent,
        instance_id=instance_id,
        instance=instance
    )

    print(f"Creating instance: {instance_id}...")

    try:
        # CreateInstance returns a Long-Running Operation (LRO)
        operation = client.create_instance(request=request)
        print("Operation started. Waiting for completion...")

        response = operation.result()
        print(f"Successfully deployed instance: {response.name}")
        print(f"State: {response.state}")
    except Exception as e:
        print(f"Error deploying instance: {e}")

if __name__ == "__main__":
    # Example usage:
    PROJECT_ID = "your-project-id"
    LOCATION = "us-central1"
    INSTANCE_ID = "my-standalone-instance"
    IMAGE = "us-docker.pkg.dev/cloudrun/container/hello"

    deploy_instance(PROJECT_ID, LOCATION, INSTANCE_ID, IMAGE)
