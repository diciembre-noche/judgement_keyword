# encoding=utf-8
def look_up_law(content,lawstart,law_list):
    for i in range(len(law_list)):
        to_be_checked=content[lawstart-len(law_list[i])+3:lawstart+3]
        if(to_be_checked==law_list[i]):
            return(to_be_checked)
    return "目錄裡沒有的法"
f=open("lawlist.txt","r")
content=f.read()
f.close()
law_list=content.split("\n")
law_list.pop()


f=open("original_content.txt","r")
content=f.read()
f.close()
lawstart=0
content=content.replace(" ","")
content=content.replace("\n","")
content=content.replace("\r","")
while(True):
    lawstart=content.find("法第",lawstart)
    if lawstart==-1:
        break
    law_name=look_up_law(content,lawstart,law_list)
    article=content.find("條",lawstart)
    if (law_name=="目錄裡沒有的法"):
        print("......"+content[lawstart-18:article+3])
    else:
        print(law_name+content[lawstart+3:article+3])
    lawstart=article
    
