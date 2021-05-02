import sys


def olHandle(data):
    return f'<ol></ol>'


def ulHandle(data):
    return f'<ul></ul>'


def headingsHandle(data):
    """heading tags"""
    return f'<h?></h?>'
    # data = data.lstrip('#').strip()
    # if 1 <= count <= 6:
    #     write.append(f'<h{count}>{data}</h{count}>')
    # return write


funtion_convert = {
    '#': headingsHandle,
    '-': ulHandle,
    '*': olHandle,
}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r') as markdownFile:
            htmlTagList = []
            linesRead = markdownFile.readlines()
            for line in linesRead:
                line = line.strip()
                firstChar = line[0]
                if firstChar in funtion_convert.keys():
                    htmlTag = funtion_convert[firstChar](line)
                else:
                    htmlTag = 'parrafo'
                htmlTagList.append(htmlTag)

            print(htmlTagList)
        # Write into an html file
        # with open(sys.argv[2], 'w', encoding="utf-8") as html:
        #     content = '\n'.join([str(char)
        #                          for elem in write for char in elem])
        #     html.write(content + '\n')
        # sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        sys.exit(1)
