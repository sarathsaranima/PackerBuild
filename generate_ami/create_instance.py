""""This is the file to create instances"""
from calendar import timegm
from time import gmtime
import logging

import boto3

from .config import builder_config

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class CreateInstance(object):
    ec2_client = None,
    tag_name = ''

    def __init__(self, name, key_id, secret_key):
        self.tag_name = name
        self.ec2_client = boto3.client('ec2',
                                  aws_access_key_id=key_id,
                                  aws_secret_access_key=secret_key,
                                  region_name=builder_config.get("region", "ap-southeast-2"))

    def get_ami_by_name(self):
        """"
        Method to get ami ID from tag name
        """
        # images = ec2_client.describe_images()
        images = self.ec2_client.describe_images(Filters=[{'Name': 'tag:Name', 'Values': [self.tag_name]}])
        return images['Images'][0]['ImageId']

    def create_ec2_instance(self):
        """"
        Method to  create EC2 instance using AMI
        """
        ts = timegm(gmtime())
        server_tag_name = "WebServer-{}".format(ts)
        ami_id = self.get_ami_by_name()
        self.ec2_client.run_instances(
            MinCount=1,
            MaxCount=1,
            ImageId=ami_id,
            InstanceType=builder_config.get("type", "t2.micro"),
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': server_tag_name
                        }
                    ]
                }
            ]
        )
        logging.debug("Ec2 instance created successfully with Image {}".format(self.tag_name))
