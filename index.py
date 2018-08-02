#!/usr/bin/python
# encoding: utf-8
# -*- coding: UTF-8 -*-

from workflow import Workflow
from pypinyin import pinyin
import sys
reload(sys) 
# Python 2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


def main(wf):
    # 获取需要查询的内容
    query = wf.args[0]

    str = ' '.join([item[0] for item in pinyin(query)])

    # Script Filter 返回的 List
    wf.add_item(title=str)
    wf.send_feedback()
    

if __name__ == '__main__':
    
    wf = Workflow()

    logger = wf.logger

    sys.exit(wf.run(main))