import boto3


ec2_client_paris = boto3.client('ec2', region_name='eu-west-3')
ec2_resource_paris = boto3.resource('ec2', region_name='eu-west-3')

reservations_paris = ec2_client_paris.describe_instances()['Reservations']

instance_ids_paris = []

for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instance_ids_paris.append(ins['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)
