# encoding=utf-8
#known issues:  
#同法 前法 
#第A及B條
#alias 某些法有縮寫e.g.刑事訴訟法&刑訴法 
#同篇判決書中重複的條目
#憲法增修條文
#條目是國字
def look_up_law(content,lawstart,law_list,nchar):
    for i in range(len(law_list)):
        to_be_checked=content[lawstart-len(law_list[i])+3*nchar:lawstart+3*nchar]
        if(to_be_checked==law_list[i]):
            return(to_be_checked)
    return "目錄裡沒有的法"
import os
import json
files = [x for x in os.listdir('jrf_stories') if x.endswith('.json')]
res = open('working/results.csv', 'w')
for fname in files:
    #print (fname)
    with open('jrf_stories/'+fname) as data_file:
        data = json.load(data_file,encoding="utf-8")
    try:
        main_content= json.dumps(data['verdict']['body']['content']['main_content'],ensure_ascii=False)
    except:
        continue
    main_content=main_content.replace('\\r\\n','\n')
    main_content=main_content.encode('utf-8')

    f = open('working/working.txt', 'w')
    f.write('%s' % main_content)
    f.close()
    del(main_content)

    f=open("lawlist.txt","r")
    content=f.read()
    f.close()
    law_list=content.split("\n")
    law_list = filter(None, law_list)


    #f=open("original_content.txt","r")
    #f=open("行政-104-訴更一-17.txt","r")
    #f=open("test.txt","r")
    f=open("working/working.txt","r")
    content=f.read()
    f.close()
    content=content.replace(" ","")
    content=content.replace("\n","")
    content=content.replace("\r","XXXYYY")
    lawstart=0
    while(True):
        lawstart1=content.find("法第",lawstart)
        lawstart2=content.find("條例第",lawstart)
        lawstart3=content.find("通則第",lawstart)
        if lawstart1==-1 and lawstart2==-1 and lawstart3==-1:
            break
        lawstartlist=[lawstart1,lawstart2,lawstart3]
        lawstartlist = [s for s in lawstartlist if s >0]
        lawstart=min(lawstartlist)
        if content[lawstart:lawstart+3]=="法":
            nchar=1
        if content[lawstart:lawstart+3]=="條"or content[lawstart:lawstart+3]=="通":
            nchar=2
        law_name=look_up_law(content,lawstart,law_list,nchar)
        article=content.find("條",lawstart+3)
        if (law_name=="目錄裡沒有的法"):
            #print("......"+content[lawstart-60:article+3])
            pass
        else:
            #print(law_name+content[lawstart+3*nchar:article+3])
            str_to_write=fname+','+law_name+','+content[lawstart+3*(nchar+1):article]
            res.write('%s\n' % str_to_write)
        lawstart=article
res.close()
