# encoding=utf-8
f=open("original_content.txt","r")
content=f.read()
f.close()
lawstart=0
while(True):
    lawstart=content.find("法第",lawstart)
    if lawstart==-1:
        break
    article=content.find("條",lawstart)
    print(content[lawstart-15:article+3])
    lawstart=article
    
