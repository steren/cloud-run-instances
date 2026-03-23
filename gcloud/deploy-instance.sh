#!/bin/bash

# Configuration
PROJECT_ID="steren-run"
LOCATION="europe-west9"
IMAGE="ubuntu" # Official Ubuntu image from DockerHub

# Create the instance
echo "Creating instance..."
gcloud alpha run instances create \
  --project="$PROJECT_ID" \
  --image="$IMAGE" \
  --region="$LOCATION"
