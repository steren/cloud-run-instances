const { InstancesClient } = require('@google-cloud/run').v2;

/**
 * Deploys a standalone Cloud Run Instance (not a Service or Job).
 * 
 * @param {string} projectId - Google Cloud Project ID.
 * @param {string} location - Google Cloud Region (e.g., 'us-central1').
 * @param {string} instanceId - Unique identifier for the instance.
 * @param {string} image - Container image URI (e.g., 'us-docker.pkg.dev/cloudrun/container/hello').
 */
async function deployInstance(projectId, location, instanceId, image) {
  const client = new InstancesClient();

  const parent = `projects/${projectId}/locations/${location}`;

  const request = {
    parent: parent,
    instanceId: instanceId,
    instance: {
      containers: [
        {
          image: image,
          resources: {
            limits: {
              cpu: '1',
              memory: '512Mi',
            },
          },
        },
      ]
    },
  };

  console.log(`Creating instance: ${instanceId}...`);

  try {
    const [operation] = await client.createInstance(request);
    console.log('Operation started. Waiting for completion...');

    const [response] = await operation.promise();
    console.log(`Successfully deployed instance: ${response.name}`);
    console.log(`State: ${response.state}`);
  } catch (error) {
    console.error('Error deploying instance:', error);
  }
}

// Example usage:
const PROJECT_ID = 'your-project-id';
const LOCATION = 'us-central1';
const INSTANCE_ID = 'my-standalone-instance';
const IMAGE = 'us-docker.pkg.dev/cloudrun/container/hello';

deployInstance(PROJECT_ID, LOCATION, INSTANCE_ID, IMAGE);
