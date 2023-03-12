import inspect

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def get_object_from_id(self, id):
        calling_method_name = inspect.currentframe().f_back.f_code.co_name

        if "category" in calling_method_name:
            try:
                category = [x for x in self.categories if x.id == id][0]
            except IndexError:
                pass

            return category

        elif "topic" in calling_method_name:
            try:
                topic = [x for x in self.topics if x.id == id][0]
            except IndexError:
                pass

            return topic

        elif "document" in calling_method_name:
            try:
                document = [x for x in self.documents if x.id == id][0]
            except IndexError:
                pass

            return document

    def edit_category(self, category_id, new_name):
        category = Storage.get_object_from_id(self, category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = Storage.get_object_from_id(self, topic_id)
        if topic.id == topic_id:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = Storage.get_object_from_id(self, document_id)
        if document.id == document_id:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        return '\n'.join(Document.__repr__(x) for x in self.documents)
