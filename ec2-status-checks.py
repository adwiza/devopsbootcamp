import boto3
import schedule


ec2_client = boto3.client('ec2', region_name='eu-west-3')
ec2_resource = boto3.resource('ec2', region_name='eu-west-3')

# new_vpc = ec2_resource.create_vpc(
#     CidrBlock='10.0.0.0/16'
# )
#
# new_vpc.create_subnet(
#     CidrBlock='10.0.1.0/24',
# )
#
# new_vpc.create_subnet(
#     CidrBlock='10.0.2.0/24',
# )
#
# new_vpc.create_tags(
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'my-vpc'
#         },
#     ]
# )
#
# all_available_vpcs = ec2_client.describe_vpcs()
#
# vpcs = all_available_vpcs['Vpcs']
#
# for vpc in vpcs:
#     print(vpc['VpcId'])
#     cidr_block_assoc_sets = vpc['CidrBlockAssociationSet']
#     for assoc_set in cidr_block_assoc_sets:
#         print(assoc_set['CidrBlock'])

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(instance['InstanceId'], instance['State']['Name'])


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )

    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f'Instance {status["InstanceId"]} is {state} with instance status is {ins_status} and system_status is {sys_status}')


schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()
