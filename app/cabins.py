import requests
from flask import Blueprint

cabins = Blueprint('cabins', __name__)


@cabins.route('/', methods=['GET'])
def query_cabins():
    r = requests.get('http://localhost:3030/cabins/owned', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzY2ZTRjN2U0YjY2ZGEyNzFiMDIyZGEiLCJlbWFpbCI6InRlc3QyQHRlc3QuY29tIiwiaWF0IjoxNjY3Njg3NjI1LCJleHAiOjE2Njc3NzQwMjV9.fG0rvRaqgxKu52vEP_Vwvckb3xll5qzcp50SWuAs0w0'})
    return r.json()
