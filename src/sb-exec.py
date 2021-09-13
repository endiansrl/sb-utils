#!/usr/bin/env python3
# Documentation for API located here:
# http://docs.endian.com/5.0/utm/switchboard_admin_api_swagger.yaml.html

import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import configparser
import argparse
import yaml
import uuid
from os import path
from loguru import logger

credentials = "credentials.txt"

class switchboard(object):

    def __init__(self):
        self.base_url = None
        self.api_key = None
        self.session = None

    def login(self, url, username, password, api_key):
        self.base_url = "https://{}/manage/commands/commands.access.admin.".format(url)
        self.api_key = api_key
        self.session = requests.session()
        self.session.auth = (username, password)
        logger.debug("Logging in at {} with: {}:{}".format(url, username, "*" * len(password)))
        try:
            auth = self.session.post(self.base_url + "loginTest", data={
                'name': username,
                'password': password,
                'api_key': self.api_key
            }, verify=False)
        except Exception as e:
            logger.error('Exception while logging in: {}'.format(e))
            quit()
        if auth.status_code == 200:
            logger.debug("Login successful.")
            return True
        else:
            logger.debug("Login issue: {}".format(auth.content))
            return False

    def logout(self):
        self.session = None
        logger.debug("Logged out.")

    def exec(self, data):
        try:
            command = data['command']
            del data['command']
        except Exception:
            logger.error("command variable is required, please correct your syntax")
            quit()
        try:
            description = data['description']
            del data['description']
            logger.info("Running: {}".format(description))
        except Exception:
            logger.error('description variable is required, please correct your syntax')
            quit()
        data['api_key'] = self.api_key
        logger.info(data)
        result = self.session.post(self.base_url + command, data=data)
        logger.patch(lambda record: record.update(function="exec:{}".format(command))).debug(result.content)
        return result.content


def init_logging(file):
    config = {
        "handlers": [
            {"sink": sys.stdout},
            {"sink": file, "serialize": True},
        ],
        "extra": {"user": "someone"}
    }
    logger.configure(**config)
    logger.info("Logging to {}".format(file))


def parse_arguments():
    argparser = argparse.ArgumentParser(description='Switchboard Test Case Executor')
    argparser.add_argument('file', help='YAML formatted test case file')
    return argparser.parse_args()


def parse_credentials():
    if not path.exists(credentials):
        logger.error("Cannot find credentials file, please see README")
        quit()
    config = configparser.ConfigParser()
    config.read(credentials)
    return config


def execute(commands):
    config = parse_credentials()
    s = switchboard()
    if not s.login(config['credentials']['sb_url'], config['credentials']['username'], config['credentials']['password'], config['credentials']['api_key']):
        logger.error("Cannot login, please check your credentials, your API permissions and key.")
        quit()
    for c in commands:
        s.exec(c)
    s.logout()


def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    args = parse_arguments()
    if not path.exists(args.file):
        logger.error("Test case file [{}] does not exist".format(args.file))
        quit()
    init_logging("{}.log".format(args.file))
    try:
        with open(args.file) as file:
            commands = yaml.full_load(file)
    except Exception as e:
        logger.error('Something went wrong while loading YAML file: {}'.format(e))
    execute(commands)


if __name__ == "__main__":
    main()
