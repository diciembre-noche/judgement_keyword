# encoding=utf-8
from convertChineseDigitsToArabic import convertChineseDigitsToArabic
import json
import jieba

with open('need_rework.json') as f:
    content = f.readlines()
fnew = open('reworked.json', 'w')
for i in range(len(content)):
    c1=content[i].find(',')
    c2=content[i].find(',',c1+1)
    to_be_convert=(content[i][c2+1:-6])
    converted=(convertChineseDigitsToArabic(to_be_convert))
    if converted ==0:
        fnew.write('%s%s\\n",\n' % (content[i][0:c2+1],to_be_convert))  
    else:
        fnew.write('%s%s\\n",\n' % (content[i][0:c2+1],converted))

fnew.close()
