from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("淘宝网 - 淘！我喜欢.html", 'r', encoding="utf-8") as f:
        bs = BeautifulSoup(f, "html.parser")

    data = []

    for ele in bs.find_all("div",role="listitem"):
        item = ele.h4.text
        if item :
            desc = ele.find("p").text
            href = ele.find("a")["href"]
            data.append((item,desc,href))
        # print(ele)
    print(data)
