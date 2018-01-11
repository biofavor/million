# million

【百万英雄】【冲顶大会】【芝士超人】在线答题辅助
![](https://raw.githubusercontent.com/biofavor/million/master/s.gif)

- === 思路 ===
- 核心：判断何时出题，截取题目图像，OCR成文字，弹出百度搜索该文字。
- 截图：电脑通过Total Control连接手机，iphone的话用itools里的airplay工具无线投屏也行。当然用手游模拟器直接装APP也行。
- OCR ：识别文字并打开百度搜索：
- 语义：结巴分词，后期可尝试【玻森中文语义开放平台】，免费版现在每天限制500次关键词提取
- 最后：这只是一个辅助工具，百度很多时候搞不定这些变态的题目啊！可以尝试多台电脑分别对
- 选项也进行OCR，综合判断，语义分析的复杂让我对这个没啥兴趣了。

## 使用

- 安装Total Control并连接手机，放置到如图的位置，或者修改位置的相关坐标到手机屏幕。
- 安装OCR pytesseract组件
- 安装pyscreenshot组件
- 安装jieba 结巴分词组件
- 缺失模块pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 模块名
感兴趣的朋友，加我扣扣啦26231629
![](https://raw.githubusercontent.com/biofavor/million/master/872579128340594942.jpg)
