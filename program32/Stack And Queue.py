books = []
books.append("learn c")
books.append("learn c++")
books.append("learn java")
print(books)

books.pop()
print("now the top book is: ", books[-1])

books.pop()
print("now the top book is: ", books[-1])

books.pop()
if not books:
    print(" no books left")
