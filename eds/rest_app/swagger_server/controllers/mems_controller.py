import connexion
from swagger_server.models.mems_data import MemsData
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from base64 import b64decode
import requests


#@app.route('/eds/MemsIPE')
def get_memsdata():
    """
    get_memsdata


    :rtype: MemsData
    """


