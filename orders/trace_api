import requests
import json
from datetime import timedelta, datetime
from urllib import response

def find_close_contact_id()
    string= requests.alldata
    allrecords= json.dumps(string)

    #case_data= requests.reportedCaseData
    #case_record= json.dumps(case_data)
    case_record= list uid_of_reported_cases and date


    venue_list=[]
    for i in case_record:
        date= case_record[i]['date']
        uid= case_record[i]['hkuid']
        for j in allrecords:
            newlist=[]
            #infected_history=[]
            if allrecords[j]['hkuid']==uid:
                #infected_history.append(allrecords[j])
                if (allrecords[j]['date']==date- timedelta(days=2)) or (allrecords[j]['date']==date- timedelta(days=1)) or (allrecords[j]['date']==date):
                    if allrecords[j]['type']=="entry":
                        close_venue= allrecords[j]['venue']
                        close_date= allrecords[j]['date']
                        close_entry= allrecords[j]['time']
                        newlist.append(close_venue)
                        newlist.append(close_date)
                        newlist.append(close_entry)
                        
                    if allrecords[j]['type']=="exit":
                        close_exit= allrecords[j]['time']
                        newlist.append(close_exit)
                        venue_list.append(newlist)
    #venue list now have lists of venue, date, entry and exit time
    x=0 #x= number of cases processed
    timemask= "%H:%M"
    close_contact_list=[]
    while x<len(case_record):
        process_date= venue_list[x]['close_date']
        process_venue= venue_list[x]['close_venue']
        process_entrytime=venue_list[x]['close_entry']
        process_exittime=venue_list[x]['close_exit']
        for i in allrecords: 
            if (allrecords[i]['date']==process_date) and (allrecords[i]['venue']==process_venue):
                if allrecords[i]['type']=="entry":
                    if not (datetime.strptime(allrecords[i]['time'], timemask)>datetime.strptime(process_exittime, timemask)):
                        
                if allrecords[i]['type']=="exit":
                    if not (datetime.strptime(allrecords[i]['time'], timemask)<datetime.strptime(process_entrytime, timemask)):
                        
        x+=1
            

    if not case_record:
        return Response({"msg":"No Reported Cases"})
    else:
        if not close_contact_list:
            return Response({"msg":"No Close Contacts"})
    
