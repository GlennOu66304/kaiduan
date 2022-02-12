

## Python Code writing

You can use the default intendition to origanize the python function, but 
when you want to call the function. You need to start with new line and no intenditon.
```
def main ():
    infolist=[]
    vid="7579013546"
    cid='0'
    page_num=3000
    url='https://video.coral.qq.com/varticle/' + vid + '/comment/v2'
    print(url)

main()
```
[Calling a Function](https://www.w3schools.com/python/python_functions.asp) 
[indentation（缩进）和在python的grammar（语法）里是作为一个token考虑的](https://www.zhihu.com/question/40953675)
[python中缩进怎么打_python如何处理缩进](https://blog.csdn.net/weixin_35967330/article/details/113652590?spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-14.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-14.pc_relevant_default&utm_relevant_index=19)

## The reason why you can not see the content result

it might be the page number too large

## TypeError: argument 1 must have a "write" method

You should not put the comma at the end of the writer line code.

## Python PIP install package can not be found in conda enviroment

You need to use the code below to install the package:
```
python -m pip install numpy
python -m pip list

python3 -m pip install numpy
python3 -m pip list
```
[pip在虚拟环境安装python包却安装在全局/真实环境](https://blog.csdn.net/weixin_43256057/article/details/105357133?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=1)  
[Python报错ModuleNotFoundError: No module named 'numpy'](https://blog.csdn.net/qq_39779233/article/details/103224712)    

## ERROR: No matching distribution found for PIL

pip install pillow
[ERROR: No matching distribution found for PIL](https://blog.csdn.net/qq_40574123/article/details/116499279)   

## 解决Python词云库wordcloud不显示中文的问题

You need to download a Chinese font from the url below,
[source-han-serifPublic](https://github.com/adobe-fonts/source-han-serif/tree/release#downloading-source-han-serif)
then set this Chinese font in the wordclound path
[解决Python词云库wordcloud不显示中文的问题](https://blog.csdn.net/xiemanR/article/details/72796739)

## No module named sympy in pypy task
python -m pip install sympy
[No module named sympy in pypy task](https://stackoverflow.com/questions/40333554/no-module-named-sympy-in-pypy-task)
## Reference:
[用Python爬取了《开端》3w+评论数据，并将其可视化分析后，终于知道它为什么这么火了~](https://mp.weixin.qq.com/s/Cijlflk6VLLnxvDPsomixA)
