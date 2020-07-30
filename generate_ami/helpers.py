""""
This file contains helper functions for PackerAmi
"""
import logging
import os

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def get_abs_file_path(file_name):
    """
    Check the relative file path and generate absolute file path if exists
    :param file_name: string containing relative file path
    :return: a string containing the absolute file path
    """
    dir_name = os.path.dirname(__file__)
    abs_file_name = os.path.join(dir_name, file_name)
    if os.path.isfile(abs_file_name):
        return abs_file_name
    else:
        return None


def generate_exception(msg):
    """
    Method to generate exception.
    :param msg: string containing exception message
    :return: exception of type Exception()
    """
    logging.debug(msg)
    raise Exception(msg)
