from operator import itemgetter

import boto3

ec2_client = boto3.client('ec2', region_name='eu-west-3')

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        }
    ]
)
for volume in volumes['Volumes']:

    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )

    sorter_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    for snap in snapshots['Snapshots']:
        print(snap['StartTime'])

    print('#'*100)

    for snap in sorter_by_date:
        print(snap['StartTime'])

    for snap in sorter_by_date[2:]:
        # delete snapshot
        # print(snap['SnapshotId'])
        # print(snap['StartTime'])
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)
