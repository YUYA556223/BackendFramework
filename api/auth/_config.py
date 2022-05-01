from typing import Union
import pyrebase
from pyrebase.pyrebase import Firebase


class AuthConfig:
    cfg_cache: Union[Firebase, None] = None

    @staticmethod
    def firebase_config():
        if AuthConfig.cfg_cache is None:
            AuthConfig.cfg_cache =\
                pyrebase.initialize_app({
                    "apiKey": "AIzaSyDB9cSL8o3PIyysMNI0Ba7gug67-IH9ZoI",
                    "authDomain": "mirailab-30a0e.firebaseapp.com",
                    "projectId": "mirailab-30a0e",
                    "storageBucket": "mirailab-30a0e.appspot.com",
                    "messagingSenderId": "61265060138",
                    "appId": "1:61265060138:web:fb90f2b317d760c0c8be53",
                    "measurementId": "G-J708BFNEJY",
                    "databaseURL": "",
                    "storageBucket": ""})
        return AuthConfig.cfg_cache

    @staticmethod
    def cache_count():
        return 100
