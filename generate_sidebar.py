import os

def allFile(basepath):
	files = []
	for item in os.listdir(basepath):
		path = os.path.join(basepath, item)
		if os.path.isfile(path):
			files.append(path)
		else:
			files.extend(allFile(path))
	return files


		
files = allFile(".")

sidebar_file = open('_sidebar.md', 'w', encoding='utf-8')
# sidebar_file.writelines("# coding=utf-8\n")

for file in files:
	if ".md" in file:
		if "_sidebar.md" in file:
			continue
		name = file.split(".md")
		filename = os.path.basename(file)
		filename_nosufix = filename.split(".md")
		file = file.replace(" ", "%20")
		sidebar_file.write( f"* [{filename_nosufix[0]}]({name[0]})\n" )

sidebar_file.close()