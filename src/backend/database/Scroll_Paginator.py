from src.backend.database.connection import connectionDB


class ScrollPaginator:
    def __init__(self, query, params=None, page_size=100, name="scroll_paginate"):
        self.cursor = None
        self.connection = None
        self.scroll_name = name
        self.query = query
        self.params = params
        self.page_size = page_size
        self.has_next_page = True

    def connect(self):
        try:
            self.connection = connectionDB()
            self.cursor = self.connection.cursor(name=self.scroll_name)
            self.cursor.itersize = 1000
        except Exception as e:
            print(f"Error occurred while connecting: {e}")

    def get_next_page(self):
        try:
            if self.cursor is None:
                self.connect()
                self.cursor.execute(self.query, self.params)

            rows = self.cursor.fetchmany(self.page_size)
            if not rows:
                self.has_next_page = False
                if self.cursor:
                    self.cursor.close()
                if self.connection:
                    self.connection.close()
                return []
            return rows
        except Exception as e:
            print(f"Error occurred while fetching data: {e}")

    def has_next(self):
        return self.has_next_page
