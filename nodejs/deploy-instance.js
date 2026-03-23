import { InstancesClient } from '@google-cloud/run';

const client = new InstancesClient();

const projectId = 'steren-run';
const location = 'europe-west9';
const instanceId = `my-instance-${Math.floor(Math.random() * 1000)}`;
const image = 'us-docker.pkg.dev/cloudrun/container/hello';

const [operation] = await client.createInstance({
  parent: `projects/${projectId}/locations/${location}`,
  instanceId: instanceId,
  instance: {
    containers: [{ image }],
  },
});

console.log(`Creating instance: ${instanceId}...`);
const [response] = await operation.promise();
console.log(`Successfully deployed instance: ${response.name}`);
