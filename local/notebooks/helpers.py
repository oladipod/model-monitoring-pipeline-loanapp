import pandas as pd
import numpy as np
import os
import json
import traceback
import datetime
import pickle
import uuid
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaseEnsemble
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from glob import glob


import config
# import queries



credentials = json.load(open(config.PATH_TO_CREDENTIALS, 'r'))
engine = create_engine(f"postgresql://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{credentials['database']}")
print(f"[INFO] Connection to `{credentials['host']}:{credentials['database']}` initiated!")






### job handlers ###
def generate_uuid() -> str:
    """
    Generate a random UUID.
    :return: str
    """
    return str(uuid.uuid4()).replace("-", "")