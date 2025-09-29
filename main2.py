import asyncio
import json
import requests as r
from bs4 import BeautifulSoup

class Juanzi(object):
    title = ""
    questions = []

    def __init__(self):
        self.title = ""
        self.questions = []

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self, f, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

class Question(object):
    title = ""
    subtitles = []
    answer_options = []

    def __init__(self):
        self.no = 0
        self.title = ""
        self.subtitles = []
        self.answer_options = []

def fetch_juanzi(url):
    res = r.get(url)
    print(res.text)
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup)
    title = soup.find("h3")
    soup.find()
    data = soup.find(id="printcontent").div
    rows = data.find_all("div", class_="row")

    juanzi = Juanzi()
    juanzi.title = title.text

    questions = []
    juanzi.questions = questions
    no = 0
    for row in rows:
        items = row.find_all("div")
        if len(items) == 1:
            pass
        else:
            # 新问题
            q = Question()
            questions.append(q)
            no += 1
            q.no = no

            ps = items[1].find_all("p", recursive=False)
            # 问题的标题
            q.title = ps[0].text
            # 问题的子标题列表
            for p in ps[1:]:
                q.subtitles.append(p.text)

            # 问题的答案选项列表
            for ao in items[1].find_all("div", recursive=False):
                q.answer_options.append(ao.text)
    return juanzi

if __name__ == "__main__":
    url = "https://www.gkzenti.cn/paper/1758335703342"
    juanzi = fetch_juanzi(url)
    print(juanzi)
    juanzi.save_to_file("juanzi.json")
