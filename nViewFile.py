#!/usr/bin/python3
import json
from models.base_model import *
from models import storage


json_string = json.dumps(dict(storage.all()), indent=2)

print(json_string)
