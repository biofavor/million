# coding: utf-8
'''
# === 思路 ===
# 核心：判断何时出题，截取题目图像，OCR成文字，弹出百度搜索该文字。
# 截图：电脑通过Total Control连接手机，进行截图，目前发现最好的方法了。
# OCR ：识别文字并打开百度搜索：
# 语义：结巴分词，后期可尝试【玻森中文语义开放平台】，免费版现在每天限制500次关键词提取
# 最后：这只是一个辅助工具，百度很多时候搞不定这些变态的题目啊！可以尝试多台电脑分别对
# 选项也进行OCR，综合判断，语义分析的复杂让我对这个没啥兴趣了。
'''
import time
import webbrowser
import pytesseract
import pyscreenshot as ImageGrab
import jieba

VERSION = "1.0.0"
def main():
    '''
    主函数
    '''
    print('程序版本号：{}'.format(VERSION))
    while True:
        img=ImageGrab.grab(bbox=(1870,360,1871,361)) # X1,Y1,X2,Y2 截取监测图像所在电脑屏幕的位置,1920X1080分辨率，不同的电脑可通过开始——》运行mspaint，截屏然后粘贴查看
        img = img.convert ('RGB')
        #coordinates of the pixel
        X,Y = 0,0
        #Get RGB
        pixelRGB = img.getpixel((X,Y))
        R,G,B = pixelRGB 
        brightness = sum([R,G,B])/3 ##0 表示很暗 (黑色) ， 255 表示很亮 (白色)
        # print(brightness)       
        # 亮度大于210,说明题目弹出来了
        if(brightness>210):
            time.sleep(0)# 观察到题目不是一瞬间出现，提前截图的话可能会截不完整。可以填入1-2。实测，0也没问题。
            img_a=ImageGrab.grab(bbox=(1390,220,1870,360)) # X1,Y1,X2,Y2 截取答案的图像,1920X1080分辨率，不同的电脑可通过开始——》运行mspaint，截屏然后粘贴查看
            code = pytesseract.image_to_string(img_a, lang='chi_sim').replace('\n','').replace(' ','').split('.')[-1].split('?')[0]
            #print(code)
            jieba_out = " ".join(code)
            print(jieba_out)
            webbrowser.open("https://www.baidu.com/s?wd="+jieba_out)
            time.sleep(7)# 弹出来之后需要停一下，不然重复弹窗影响阅读
if __name__ == '__main__':
    main()
