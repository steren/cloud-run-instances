#!/bin/bash

# Configuration
ACCESS_TOKEN=$(gcloud auth print-access-token)
PROJECT_ID="steren-run"
INSTANCE_ID="my-instance-$((100 + RANDOM % 900))"
LOCATION="europe-west9"
IMAGE="us-docker.pkg.dev/cloudrun/container/hello"

# Create the instance
echo "Creating instance: $INSTANCE_ID..."
curl -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -X POST \
  -d "{
    \"containers\": [
      {
        \"image\": \"$IMAGE\"
      }
    ]
  }" \
  "https://run.googleapis.com/v2/projects/$PROJECT_ID/locations/$LOCATION/instances?instanceId=$INSTANCE_ID"

# Get the instance state
echo -e "\n\nGetting instance status..."
curl -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://run.googleapis.com/v2/projects/$PROJECT_ID/locations/$LOCATION/instances/$INSTANCE_ID"
