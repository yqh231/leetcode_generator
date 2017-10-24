import requests
from lxml import etree
import sys


def get_html(question_name):
    url = 'https://leetcode.com/problems/' + question_name + '/description/'
    html = requests.get(url=url).content
    return html


def parse_html(html):
    src = etree.HTML(html)
    title = src.xpath('//title')
    question = src.xpath('//meta[@name="description"]/@content')
    return title[0].text, question[0]


def generator_file(path, title, content):
    with open('{}/{}.py'.format(path, title), mode='w') as file:
        file.write('"""\n')
        file.write(title)
        file.write(content)
        file.write('"""')


if __name__ == '__main__':
    question_name = sys.argv[1]
    path = sys.argv[2]
    html = get_html(question_name)
    title, content = parse_html(html)
    generator_file(path, title, content)
