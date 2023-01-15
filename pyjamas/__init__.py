"""
By default, the functions to store it in any database, as well as the function to check passwords. So developers can use these two expoorted functions
"""

from getpass import getpass as getpass
from .database import store_in_database as store_in_database
from .passwords import check_password as check_password
from .miscellaneous import load_desired_env_variable as load_desired_env_variable
