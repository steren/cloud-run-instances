import { InstancesClient } from '@google-cloud/run';

const client = new InstancesClient();

const projectId = 'steren-run';
const location = 'europe-west9';
const image = 'us-docker.pkg.dev/cloudrun/container/hello';

const [operation] = await client.createInstance({
  parent: `projects/${projectId}/locations/${location}`,
  instance: {
    containers: [{ image }],
  },
});

console.log('Operation started. Waiting for completion...');
const [response] = await operation.promise();
console.log(`Successfully deployed instance: ${response.name}`);
