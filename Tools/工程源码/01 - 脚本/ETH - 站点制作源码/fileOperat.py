import os
import shutil
import time

filterText = 'wsdc' # 需要替换的关键字

try:
    shutil.rmtree('./dist')
except OSError as e:
    print(f'Error: ./dist : {e}')

# 复制模板文件到输出文件夹
with os.scandir('./NFT Project') as srcs:
    for project in srcs:
        shutil.copytree('./wsdc', 'dist/' + project.name)
# 替换关键字
with os.scandir('./dist') as dists:
    for distFile in dists:
        # 只读形式打开文件
        with open(distFile.path + '/img/js.js', 'r', encoding='UTF-8') as jsjs:
            # 文件内容赋值变量存储
            jsjsStr = jsjs.read()
            # 单词替换
            jsjsStr = jsjsStr.replace(filterText, distFile.name)
        with open(distFile.path + '/index.html', 'r', encoding='UTF-8') as indexHtml:
            # 文件内容赋值变量存储
            indexHtmlStr = indexHtml.read()
            # 单词替换
            indexHtmlStr = indexHtmlStr.replace(filterText, distFile.name)
        # 覆盖写入替换后的内容
        with open(distFile.path + '/img/js.js', 'w', encoding='UTF-8') as jsjs:
            jsjs.write(jsjsStr)
        with open(distFile.path + '/index.html', 'w', encoding='UTF-8') as indexHtml:
            indexHtml.write(indexHtmlStr)
# 复制图片到输出文件下对应的项目中
with os.scandir('./NFT Project') as NFTProject:
    for project in NFTProject:
        with os.scandir(project.path + '/images') as imgs:
            for img in imgs:
                shutil.copy(img, 'dist/' + project.name + '/img')
print('操作已完成，请查看 dist 文件夹下生成的站点项目')