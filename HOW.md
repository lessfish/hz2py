第一次用 Python 写 workflow，简单记下坑

关于如何写一个 workflow，大部分类似的步骤可以看 [之前的笔记](https://github.com/hanzichi/CDNSearcher/blob/master/HOW.md)（Node 实现）

Python 的话推荐用 [alfred-workflow](https://github.com/deanishe/alfred-workflow) 这个库简化开发流程，有点蛋疼的是这个库只能用 Python 2.x

下载需要的库到 workflow 的目录下：

```bash
pip install --target=. Alfred-Workflow
pip install --target=. pypinyin
```

核心实现可以看 [这个文件](https://github.com/hanzichi/hanzi2pinyin/blob/master/index.py)，内容非常简单

其他需要注意点的，Python 2.x 对中文的兼容有点蛋疼，需要在代码文件最前加上这样的代码：

```py
import sys
reload(sys) 
# Python 2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
```

另外，我将该 workflow 的 Bundle Id 设置为 `https://github.com/hanzichi/hanzi2pinyin`，但是报莫名错误，后来改短了就好了，但是我之前的 [CDNSearcher](https://github.com/hanzichi/CDNSearcher) 用的也是类似的命名方式却没问题，有点奇怪
