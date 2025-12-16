import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

nonvalid_email = os.getenv('nonvalid_email')
nonvalid_password = os.getenv('nonvalid_password')

empty_email = os.getenv('empty_email')
empty_password = os.getenv('empty_password')