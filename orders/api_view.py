import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.records import *

@api_view(['POST',])
def index(request):
    str1 = request.data
    str1 = json.dumps(str1)
    query = json.loads(str1)
    if query['type']=='create':
        list=query['content']
        for i in list:
            recordid=create_record(i['hkuid'],i['venue'],i['datetime'])
            return {"state":"success","cmd":"create","hkuid":i['hkuid'],"recordid":recordid,"venue":i['venue'],"datetime":i['datetime']}
    elif query['type']=='modify':
        list = query['content']
        for i in list:
            modify_record(i['recordid'],i['hkuid'], i['venue'], i['datetime'])
            return {"state": "success", "cmd": "modify", "hkuid": i['hkuid'], "recordid": i["recordid"], "venue": i['venue'],
                    "datetime": i['datetime']}
    elif query['type'] == 'delete':
        list = query['content']
        for i in list:
            delete_record(i['recordid'])
            return {"state": "success", "cmd": "delete","recordid": i["recordid"]}
    return {"state":"fail"}
