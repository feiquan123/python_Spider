from urllib import request
from bs4 import BeautifulSoup as BS

if __name__ == '__main__':
    response = request.urlopen("http://www.baidu.com")
    # bs = BS('<h1 class="name">name is joke</h1>", "html.parser')  # 读字符串
    # bs = BS(response.read(), "html.parser")  # 读 HTML 网页
    with open("百度一下，你就知道.html", 'r', encoding="utf-8")  as f:
        bs = BS(f, "html.parser")  # 读 HTML 文件
    # print(bs.title)

    tag = bs.link
    print(tag.name)

    # 改变标签名
    tag.name = 'blockquote'
    print(tag)

    # 获取属性，与字典相同
    print(tag["href"])

    del(tag["rel"])
    tag["id"] = "#show"
    print(tag)
