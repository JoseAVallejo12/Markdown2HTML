import sys


def ol_parse(data):
    return f'<ol></ol>'


def ul_parse(data):
    return f'<ul></ul>'


def heading_parse(index, lines_read_list):
    """heading tags"""
    # data = data.strip()
    # min_level = 1
    # max_level = 6
    # heading_level = len(data) - len(data.lstrip('#'))

    # if min_level <= heading_level <= max_level:
    #     string_to_parsing = data.lstrip("#").strip()
    #     return f'<h{heading_level}>{string_to_parsing}</h{heading_level}>\n'

    return None


funtion_parsing = {
    '#': heading_parse,
    '-': ul_parse,
    '*': ol_parse,
}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)
    try:
        htmlTagList = []
        with open(sys.argv[1], 'r') as markdownFile:
            lines_read_list = markdownFile.readlines()
            for index in range(len(linesRead)):
                line = lines_read_list[index].strip()
                first_char = line[0]
                if first_char in funtion_parsing.keys():
                    htmlTag = funtion_parsing[first_char](index, lines_read_list)
                else:
                    htmlTag = 'parrafo'
                htmlTagList.append(htmlTag)

            print(htmlTagList)

        # with open(sys.argv[2], 'w', encoding="utf-8") as html:
        #     for htmlLine in htmlTagList:
        #         if htmlLine:
        #             html.write(htmlLine)
        # sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        sys.exit(1)
