"""main.py"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import wikipedia as wk
from newsapi import NewsApiClient as nac
import datetime
import random

class MainWindow:
    """Application controller object."""
    
    def __init__(self):
        self.p = None
        
        self.main_page = tk.Tk()
        self.main_page.title("MetaWikipedia")
        self.main_page.geometry("500x500")

        self.style = ThemedStyle(self.main_page)
        self.style.set_theme("scidblue")

        self.left_pane = ttk.PanedWindow(self.main_page)
        self.right_pane = ttk.PanedWindow(self.main_page)

        # Left pane
        self.search = ttk.Button(self.left_pane, text="Search", command=self.search_wikipedia)
        self.search.place(relx=0,rely=0,relheight=0.1,relwidth=0.5)

        self.randomize_but = ttk.Button(self.left_pane, text="Randomize", command=self.randomize)
        self.randomize_but.place(relx=0.5,rely=0,relheight=0.1,relwidth=0.5)

        self.search_box = tk.Text(self.left_pane)
        self.search_box.place(relx=0,rely=0.1,relheight=0.1,relwidth=1)

        self.summary = tk.Text(self.left_pane, wrap=tk.WORD)
        self.summary.place(relx=0,rely=0.2,relheight=0.4,relwidth=1)

        extra_list_choices = ["none", "categories", "pageid", "sections", "html"]
        self.extra_list_choice = tk.StringVar()
        self.extra_list_choice.set("none")
        self.extra_list = ttk.OptionMenu(
            self.left_pane,
            self.extra_list_choice,
            *extra_list_choices,
            command=self.update_choice
        )
        self.extra_list.place(relx=0,rely=.6,relheight=.1,relwidth=1)

        self.other_text = tk.Text(self.left_pane)
        self.other_text.place(relx=0,rely=0.7,relheight=.3,relwidth=1)


        # Right pane
        self.api_key_label = ttk.Label(self.right_pane, text="API Key")
        self.api_key_label.place(relx=0, rely=0, relheight=0.1, relwidth=.4)

        self.api_key_entry = ttk.Entry(self.right_pane, text="ABC...")
        self.api_key_entry.place(relx=.4, rely=0, relheight=0.1, relwidth=.6)

        self.news_box = tk.Text(self.right_pane)
        self.news_box.place(relx=0, rely=.1, relheight=.5, relwidth=1)

        self.top_categories_label = ttk.Label(self.right_pane, text="Top Categories")
        self.top_categories_label.place(relx=0,rely=0.6,relheight=0.1,relwidth=1)

        self.top_categories = tk.Text(self.right_pane)
        self.top_categories.place(relx=0,rely=0.7,relheight=0.3,relwidth=1)

        self.category_map = {}

        self.randomize()
        
        self.left_pane.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        self.right_pane.place(relx=.5, rely=0, relheight=1, relwidth=0.5)
        self.main_page.mainloop()

    def search_wikipedia(self):
        """Safely browse wikipedia articles."""
        self.summary.delete('1.0', tk.END)
        possibilities = wk.search(self.search_box.get('1.0',tk.END).replace("\n",""))
        if len(possibilities) > 0:
            try:
                p = wk.page(possibilities[0])
            except wk.DisambiguationError as e:
                p = wk.page(e.options[0])
            self.summary.configure(state="normal")
            self.summary.delete('1.0', tk.END)
            self.summary.insert('1.0', p.summary)
            self.summary.configure(state="disabled")
            self.p = p
            self.update_category_map(p.categories)
        self.get_news()
        return None

    def update_choice(self, value):
        """Update box based on menu choice."""
        if self.p is not None:
            if value == "none":
                self.other_text.delete('1.0', tk.END)
                self.other_text.insert('1.0', "")
            if value == "categories":
                self.other_text.delete('1.0', tk.END)
                self.other_text.insert('1.0', self.p.categories)
            if value == "pageid":
                self.other_text.delete('1.0', tk.END)
                self.other_text.insert('1.0', self.p.pageid)
            if value == "sections":
                self.other_text.delete('1.0', tk.END)
                self.other_text.insert('1.0', self.p.sections)
            if value == "html":
                self.other_text.delete('1.0', tk.END)
                self.other_text.insert('1.0', self.p.html())

    def randomize(self):
        """Randomize wikipedia article."""
        self.search_box.delete('1.0', tk.END)
        self.search_box.insert('1.0', wk.random())
        self.search_wikipedia()

    def update_category_map(self, category_list):
        """Update the category map after a search."""
        for category in category_list:
            skip = False
            for i in ["wiki", "sources", "article", "stub",
                      "wayback", "cs1"]:
                if i in category.lower():
                    skip = True
            if skip:
                continue
            if category in self.category_map:
                self.category_map[category] += 1
            else:
                self.category_map[category] = 1
        self.update_top_categories()

    def update_top_categories(self):
        """Update the top categories text box."""
        cats = self.sorted_categories()
        display = ""
        for cat in cats:
            hit = "hits" if self.category_map[cat] > 1 else "hit"
            display += f"{cat}, {self.category_map[cat]} {hit}\n"
        self.top_categories.configure(state="normal")
        self.top_categories.delete('1.0', tk.END)
        self.top_categories.insert('1.0', display)
        self.top_categories.configure(state="disabled")

    def sorted_categories(self):
        """Sort categories by hits."""
        count = lambda category: self.category_map[category]
        l = sorted(self.category_map, key=count, reverse=True)
        if len(l) > 5:
            return l[:5]
        else:
            return l

    def get_news(self):
        """Get news using News API."""
        if self.api_key_entry.get() == "":
            return None
        api = nac(api_key=self.api_key_entry.get())
        now = datetime.datetime.utcnow()
        two_weeks = (now-datetime.timedelta(days=14))
        #today = now.strftime()
        query = ""
        for cat in self.sorted_categories():
            query += f"{cat},"
        search = api.get_top_headlines(q=query,
                                    sources="bbc-news,the-verge",
                                    language="en")
        news = ""
        for article in search["articles"]:
            news += f"{search['articles'][article]['title']}\n"
        self.news_box.delete('1.0', tk.END)
        self.news_box.insert('1.0', news)



if __name__ == "__main__":
    main_window = MainWindow()
