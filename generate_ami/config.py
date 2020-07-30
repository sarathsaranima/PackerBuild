""""
Configuration file for creating the packer AMI
"""

PACKER_EXE_PATH = "./resources/packer.exe"
VARS_FILE_PATH = "./resources/vars.json"

ami_filters = {"filters": {"virtualization-type": "hvm",
                           "name": "amzn2-ami-hvm-2.0.*.1-x86_64-ebs",
                           "root-device-type": "ebs"}}


builder_config = {"region": "ap-southeast-2",
                  "type": "t2.micro",
                  "owners": "amazon"}

script_path = "C:\\GitRepo\\PackerBuild\\generate_ami\\resources\\apache.sh"

