import json

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST',])
def index(request):
    str1=request.data
    str1=json.dumps(str1)
    query=json.loads(str1)
    if query['type']=='create':
        list=query['content']
        for i in list:
            create_record(i['hkuid'],i['venue'],i['date'],i['time'])
    elif query['type']=='modify':
        list = query['content']
        for i in list:
            modify_record(i['recordid'],i['hkuid'], i['venue'], i['date'], i['time'])
    elif query['type'] == 'delete':
        list = query['content']
        for i in list:
            delete_record(i['recordid'])
    return Response({"msg":"hello"})
