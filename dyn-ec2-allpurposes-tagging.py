"""
Created by Adrian
"""
import boto3
import json


def lambda_handler(event, context):
    region = event['region']
    event_type = event['detail-type']
    print(event)
    ec2_resource = boto3.resource('ec2', region_name=region)
    ec2_client = boto3.client('ec2', region_name=region)
    if event_type == "EBS Snapshot Notification":
        try:
            this_snp = event['detail']['snapshot_id'].split('/')[1]
            this_snp_vol_src = this_vol_arn = event['detail']['source'].split('/')[1]
            volume_info = ec2_client.describe_volumes(VolumeIds=[this_snp_vol_src])
            volume_tags = volume_info['Volumes'][0]['Tags']
            '''
            The code below only carries over specific tags and their values
            Uncomment and adjust to your scenario
            '''
            for tags in volume_tags:
                if tags["Key"] == 'Customer':
                    customer = tags["Value"]
                    print("Customer: ", customer)
                    tag_snp = ec2_client.create_tags(
                        Resources=[
                            this_snp,
                        ],
                        Tags=[
                            {
                                'Key': 'Customer',
                                'Value': customer,
                            },
                            {
                                'Key': 'Taggedby',
                                'Value': 'snp-tagging',
                            },
                        ])
                if tags["Key"] == 'Environment':
                    environment = tags["Value"]
                    print("Environment: ", environment)
                    tag_snp = ec2_client.create_tags(
                        Resources=[
                            this_snp,
                        ],
                        Tags=[
                            {
                                'Key': 'Environment',
                                'Value': environment,
                            }, ])
                if tags["Key"] == 'Application':
                    application = tags["Value"]
                    print("Application: ", application)
                    tag_snp = ec2_client.create_tags(
                        Resources=[
                            this_snp,
                        ],
                        Tags=[
                            {
                                'Key': 'Application',
                                'Value': application,
                            }, ])

        except:
            print("IsVolumeOrphan: yes")

    if event_type == "EBS Multi-Volume Snapshots Completion Status":
        snps = event['detail']['snapshots']
        print(snps)
        for snp in snps:
            try:
                this_snp = snp['snapshot_id'].split('/')[1]
                this_snp_vol_src = snp['source'].split('/')[1]
                print("SnapshotId: ", this_snp, "VolumeId: ", this_snp_vol_src, "Region: ", region)
                volume_info = ec2_client.describe_volumes(VolumeIds=[this_snp_vol_src])
                volume_tags = volume_info['Volumes'][0]['Tags']
                print(volume_tags)

                for tags in volume_tags:
                    if tags["Key"] == 'Customer':
                        customer = tags["Value"]
                        print("Customer: ", customer)
                        tag_snp = ec2_client.create_tags(
                            Resources=[
                                this_snp,
                            ],
                            Tags=[
                                {
                                    'Key': 'Customer',
                                    'Value': customer,
                                },
                                {
                                    'Key': 'Taggedby',
                                    'Value': 'snp-tagging',
                                },
                            ])
                    if tags["Key"] == 'Environment':
                        environment = tags["Value"]
                        print("Environment: ", environment)
                        tag_snp = ec2_client.create_tags(
                            Resources=[
                                this_snp,
                            ],
                            Tags=[
                                {
                                    'Key': 'Environment',
                                    'Value': environment,
                                }, ])
                    if tags["Key"] == 'Application':
                        application = tags["Value"]
                        print("Application: ", application)
                        tag_snp = ec2_client.create_tags(
                            Resources=[
                                this_snp,
                            ],
                            Tags=[
                                {
                                    'Key': 'Application',
                                    'Value': application,
                                }, ])

            except:
                print("IsVolumeOrphan: yes")
                tag_snp = ec2_client.create_tags(
                    Resources=[
                        this_snp,
                    ],
                    Tags=[
                        {
                            'Key': 'isVolumeOrphan',
                            'Value': 'yes',
                        },
                        {
                            'Key': 'Taggedby',
                            'Value': 'snp-tagging',
                        }, ])
