from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c = Category(1, "C")
t = Topic(1, "T", "C:\\user")
d = Document(1, 1, 1, "D")
s = Storage()

s.add_document(d)
s.delete_document(1)
print(s.documents)  # [
