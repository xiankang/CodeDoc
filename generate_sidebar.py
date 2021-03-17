import os

def WriteFile(targetFile, contentFile, level):
    name = contentFile.split(".md")
    filename = os.path.basename(contentFile)
    filename_nosufix = filename.split(".md")
    contentFile = contentFile.replace(" ", "%20")
    targetFile.write( f"{2 * level * ' '}* [{filename_nosufix[0]}]({name[0]})\n" )

def WriteDirStart(targetFile, dir, level):
    targetFile.write(f"{2 * level * ' '}* <details>\n")
    targetFile.write(f"{2 * level * ' '}<summary>{dir}</summary>\n\n")

def WriteDirEnd(targetFile, level):
    targetFile.write(f"{2 * level * ' '}</details>\n\n\n")

def generateSidebar(basepath, sidebar_file, level):
    for item in os.listdir(basepath):
        path = os.path.join(basepath, item)
        if os.path.isfile(path):
            if ".md" not in path or "_sidebar.md" in path:
                continue
            WriteFile(sidebar_file, path, level)
        else:
            WriteDirStart(sidebar_file, item, level)
            generateSidebar(path, sidebar_file, level + 1)
            WriteDirEnd(sidebar_file, level)

# 打开sidebar文件
sidebar_file = open('_sidebar.md', 'w', encoding='utf-8')
# 产生sidebar内容
generateSidebar("./src", sidebar_file, 0)
# 关闭sidebar文件
sidebar_file.close()

