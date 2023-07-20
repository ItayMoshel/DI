class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items
        self.page_size = page_size
        self.pages = [self.items[i:i + self.page_size] for i in range(0, len(self.items), self.page_size)]
        self.current_page = 0

    def getVisibleItems(self):
        return self.pages[self.current_page]

    def nextPage(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            return self
        else:
            return False

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            return self
        else:
            return False

    def goToPage(self, page_num):
        if 0 <= page_num <= len(self.pages):
            self.current_page = page_num - 1
            return self
        else:
            return False


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.prevPage()
print(p.getVisibleItems())
p.goToPage(1)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
