# encoding=utf-8
import json
import jieba

with open('test.json') as data_file:    
    data = json.load(data_file,encoding="utf-8")
main_content= json.dumps(data['verdict']['body']['content']['main_content'],ensure_ascii=False)    
main_content=main_content.replace('\\r\\n','\n')
main_content=main_content.encode('utf-8')
print(main_content)

f = open('original_content.txt', 'w')
f.write('%s' % main_content)  
f.close()

seg_list = jieba.cut(main_content)
output='/'.join(seg_list).encode('utf-8')
f = open('segment_list.txt', 'w')
f.write('%s' % output)  
f.close()

