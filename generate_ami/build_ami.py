""""
This file contains method to create an AMI using packer and configuration
"""
import json
import logging
from calendar import timegm
from time import gmtime

from packerlicious import builder, provisioner, Template
from packerpy import PackerExecutable

from .config import builder_config, script_path, PACKER_EXE_PATH, VARS_FILE_PATH
from .helpers import generate_exception, get_abs_file_path

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class PackerAmi(object):
    """"
    A class to manage the AMI creation using packer
    """
    tag_name = ''
    ami_name = ''
    tag_name = ''
    region_name = ''
    access_id = ''
    secret_access = ''

    def __init__(self, user_tag):
        self.tag_name = user_tag

    def create_ami(self):
        """
        Create an AMI using the packer package and template generated from config.
        """
        logging.debug("Validating Packer executable path {} ".format(PACKER_EXE_PATH))
        packer_path = get_abs_file_path(PACKER_EXE_PATH)
        if not packer_path:
            exc_msg = "Packer executable not available : {}".format(PACKER_EXE_PATH)
            generate_exception(exc_msg)
        p = PackerExecutable(packer_path)
        json_file_name = get_abs_file_path(VARS_FILE_PATH)
        logging.debug("Validating configuration path {} ".format(PACKER_EXE_PATH))
        if not json_file_name:
            exc_msg = "Configuration not available under : {}".format(VARS_FILE_PATH)
            generate_exception(exc_msg)
        with open(json_file_name) as f:
            template_vars = json.load(f)
            self.access_id = template_vars["aws_access_key"]
            self.secret_access = template_vars["aws_secret_key"]
        logging.debug("Creating packer template from configuration")
        tag_configs = self.generate_tag_for_ami()
        ts = timegm(gmtime())
        self.ami_name = "packer-auto{}".format(ts)
        template = self.create_template_from_config(tag_configs)
        logging.debug("Packer template generation successful {}".format(template.to_json()))
        logging.debug("Generating AMI using config : {}".format(template_vars))
        (ret, out, err) = p.build(template.to_json(), var=template_vars)
        if ret == 1:
            msg = "AMI generation unsuccessful"
            logging.error("{} {}".format(msg, err))
            generate_exception(msg)
        else:
            logging.debug("AMI generation successful {}".format(self.ami_name))
            logging.debug("AMi Generation Details {}".format(out))

    def create_template_from_config(self, tag_configs):
        """
        Generate a packer template using configurations.
        :param tag_configs: dict containing the tag details
        :return: template of type packerlicious.Template
        """
        template = Template()
        template.add_builder(
            builder.AmazonEbs(
                access_key="{{user `aws_access_key`}}",
                secret_key="{{user `aws_secret_key`}}",
                region=builder_config.get("region", "ap-southeast-2"),
                instance_type=builder_config.get("type", "t2.micro"),
                ssh_username="{{user `ssh_username`}}",
                ami_name=self.ami_name,
                source_ami="ami-02769748522663066",
                tags=tag_configs

            ))
        template.add_provisioner(
            provisioner.Shell(
                script=script_path
            )
        )
        return template

    def generate_tag_for_ami(self):
        """
        Method to generate a tag config details using a tag name.
        :return: dict
        """
        tag_configs = {"Name": self.tag_name}
        return tag_configs
