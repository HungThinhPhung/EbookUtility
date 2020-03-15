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

