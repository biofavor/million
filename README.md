# million

【百万英雄】【冲顶大会】在线答题辅助工具


- === 思路 ===
- 核心：判断何时出题，截取题目图像，OCR成文字，弹出百度搜索该文字。
- 截图：电脑通过Total Control连接手机，进行截图，目前发现最好的方法了。
- OCR ：识别文字并打开百度搜索：
- 语义：结巴分词，后期可尝试【玻森中文语义开放平台】，免费版现在每天限制500次关键词提取
- 最后：这只是一个辅助工具，百度很多时候搞不定这些变态的题目啊！可以尝试多台电脑分别对
- 选项也进行OCR，综合判断，语义分析的复杂让我对这个没啥兴趣了。

## 使用

- 安装Total Control并连接手机，放置到如图的位置
- 安装OCR pytesseract组件
- 安装pyscreenshot组件
