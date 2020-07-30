import logging

from generate_ami.build_ami import PackerAmi
from generate_ami.create_instance import CreateInstance
from input import get_tag_from_user

logging.basicConfig(format='%(message)s', level=logging.DEBUG)

__version__ = '0.0.1'
__author__ = 'Sarath Nair'


def main():
    try:
        tag_name = get_tag_from_user()
        if tag_name:
            packer_ami = PackerAmi(tag_name)
            packer_ami.create_ami()
            ec2_inst = CreateInstance(packer_ami.tag_name, packer_ami.access_id, packer_ami.secret_access)
            ec2_inst.create_ec2_instance()
    except ValueError as e:
        logging.debug("Error :{}".format(e))
    except Exception as e:
        logging.debug("Other Exception :{}".format(e))


if __name__ == "__main__":
    main()


