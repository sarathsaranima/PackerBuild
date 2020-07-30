""""
This file contains method to get input from user
"""
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def get_tag_from_user():
    """
    Get the tag from user
    :return: string with tag
    """
    tag_name = str(input("Enter the tag for AMI :"))
    if tag_name.strip() != '':
        return tag_name.upper()
    else:
        logging.debug("Invalid Tag name. Skipping AMI generation ")
        return None
