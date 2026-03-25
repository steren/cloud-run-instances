#!/bin/bash

# Configuration
ACCESS_TOKEN=$(gcloud auth print-access-token)
PROJECT_ID="steren-run"
LOCATION="europe-west9"
IMAGE="ubuntu" # Official Ubuntu image from DockerHub

# Create the instance
echo "Creating instance..."
curl -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -X POST \
  -d "{\"containers\": [{\"image\": \"$IMAGE\"}]}" \
  "https://run.googleapis.com/v2/projects/$PROJECT_ID/locations/$LOCATION/instances"
