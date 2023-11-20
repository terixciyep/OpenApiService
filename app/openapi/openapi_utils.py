import json
import os

import yaml


def format_validator(openapi_file):
    try:
        json.loads(openapi_file)
        return ('json')
    except:
        try:
            yaml.safe_load(openapi_file)
            return ('yaml')
        except:
            return False




