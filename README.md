# Cloud Run Instance Deployer

This repository provides Node.js, Python, cURL, and gcloud CLI examples to deploy standalone Cloud Run Instances using the Google Cloud Run Admin SDK. Unlike instances of Cloud Run Services, Jobs, or Worker Pools, these instances are individually manageable.

Cloud Run instances are currently in Private Preview, sign up [here](https://forms.gle/MKxUAxYnEqH44K7V7)

## Project Structure

```text
cloud-run-instances/
├── nodejs/
│   ├── deploy-instance.js  # Node.js deployment script
│   └── package.json        # Node.js dependencies
├── python/
│   ├── deploy_instance.py   # Python deployment script
│   └── requirements.txt     # Python dependencies
├── gcloud/
│   └── deploy-instance.sh   # gcloud CLI example script
└── curl/
    └── deploy-instance.sh   # cURL example script
```

## Usage

Each script requires a Google Cloud Project ID, a location (region), an instance ID, and a container image URI.

### gcloud CLI

1.  Navigate to the `gcloud` directory: `cd gcloud`
2.  Ensure you have the gcloud CLI installed and authenticated: `gcloud auth login`
3.  Make the script executable: `chmod +x deploy-instance.sh`
4.  Update the project and instance variables in the script.
5.  Run the script: `./deploy-instance.sh`

### Node.js

1.  Navigate to the `nodejs` directory: `cd nodejs`
2.  Install dependencies: `npm install`
3.  Authenticate with Google Cloud: `gcloud auth application-default login`
4.  Update the project and instance variables in `deploy-instance.js`.
5.  Run the script: `npm start`

### Python

1.  Navigate to the `python` directory: `cd python`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Authenticate with Google Cloud: `gcloud auth application-default login`
4.  Update the project and instance variables in `deploy_instance.py`.
5.  Run the script: `python deploy_instance.py`

### cURL

1.  Navigate to the `curl` directory: `cd curl`
2.  Ensure you are authenticated with gcloud: `gcloud auth login`
3.  Make the script executable: `chmod +x deploy-instance.sh`
4.  Update the project and instance variables in the script.
5.  Run the script: `./deploy-instance.sh`

## SDK Reference

- Node.js: [InstancesClient Reference](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.instancesclient)
- Python: [google.cloud.run_v2.services.instances Reference](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.instances)
- REST: [Instances REST Reference](https://cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances)
