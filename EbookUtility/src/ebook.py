import pickle


class Ebook:

    def __init__(self):
        self.chapter = []
        self.data = []
        self.title = ''

    def load_from_raw(self, chapter: list, data: list, title=''):
        self.chapter = chapter
        self.data = data
        self.title = title

    def load_from_pickle(self, pickle_file: str):
        pickle_data = pickle.load(open(pickle_file, 'rb'))
        self.chapter = pickle_data['chapter']
        self.title = pickle_data['title']
        self.data = pickle_data['data']

    def is_valid(self):
        if not isinstance(self.chapter, list) or not isinstance(self.data, list):
            return False
        if not len(self.chapter) == len(self.data):
            return False
        return True

    def to_html(self):
        if not self.is_valid():
            raise Exception('Invalid ebook')
        with open('../data/{}.html'.format(self.title), 'w', encoding='utf-8') as f:
            f.write(self.__render_html())

    def __render_html(self):
        chapter_num = len(self.chapter)
        content = ''
        tob = ''
        for i in range(chapter_num):
            content += self.render_chapter_data(self.chapter[i], self.data[i], i)
            tob += self.render_chapter_title(self.chapter[i], i)

        header = '<!doctype html><html><head><meta charset="utf-8">'\
                 '<title>{}</title></head><body>{}{}</body></html>'
        title = self.title.replace('-', ' ').title()
        return header.format(title, tob, content)

    @staticmethod
    def render_chapter_data(chapter, data, id):
        result = '<h2 id="{}">{}</h2><br>'.format(id + 1, chapter)
        for p in data:
            result += '<br><p>{}</p>'.format(p)
        return result

    @staticmethod
    def render_chapter_title(chapter, id):
        return '<a href="#{}">{}</a><br>'.format(id + 1, chapter)
