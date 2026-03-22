# Cloud Run Standalone Instance Deployer

This repository provides Node.js and Python scripts to deploy standalone Cloud Run Instances using the Google Cloud Run Admin v2 SDK. Unlike standard Services or Jobs, these instances represent manageable, non-request-driven container units within a location.

## Project Structure

```text
cloud-run-instances/
├── nodejs/
│   ├── deploy_instance.js  # Node.js deployment script
│   └── package.json        # Node.js dependencies
└── python/
    ├── deploy_instance.py   # Python deployment script
    └── requirements.txt     # Python dependencies
```

## Usage

Each script requires a Google Cloud Project ID, a location (region), an instance ID, and a container image URI.

### Node.js

1.  Navigate to the `nodejs` directory: `cd nodejs`
2.  Install dependencies: `npm install`
3.  Update the example constants in `deploy_instance.js` or modify the script to accept parameters.
4.  Run the script: `npm start`

### Python

1.  Navigate to the `python` directory: `cd python`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Update the example constants in `deploy_instance.py` or modify the script to accept parameters.
4.  Run the script: `python deploy_instance.py`

## SDK Reference

- Node.js: [InstancesClient Reference](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.instancesclient)
- Python: [google.cloud.run_v2.services.instances Reference](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.instances)
