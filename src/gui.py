from tkinter import Button, Entry, IntVar, Label, Radiobutton, StringVar, Tk

from utils.research_gate_publication_spider import research_publication
from utils.research_gate_questions_spider import research_question


class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("輸入資訊")
        # Set window size to 800x600 pixels
        master.geometry("800x600")
        # Allow window resizing
        master.resizable(True, True)

        # Add padding to main window
        master.configure(padx=20, pady=20)

        self.keyword_label = Label(master, text="Keyword:", pady=10)
        self.keyword_label.pack(fill='x')

        self.keyword_var = StringVar()
        self.keyword_entry = Entry(master, textvariable=self.keyword_var, width=150)
        self.keyword_entry.pack(fill='x', padx=20, pady=10)

        self.cf_clearance_label = Label(master, text="CF Clearance:", pady=10)
        self.cf_clearance_label.pack(fill='x')

        self.cf_clearance_var = StringVar()
        self.cf_clearance_entry = Entry(master, textvariable=self.cf_clearance_var, width=150)
        self.cf_clearance_entry.pack(fill='x', padx=20, pady=10)

        self.user_agent_label = Label(master, text="User Agent:", pady=10)
        self.user_agent_label.pack(fill='x')

        self.user_agent_var = StringVar()
        self.user_agent_entry = Entry(master, textvariable=self.user_agent_var, width=150)
        self.user_agent_entry.pack(fill='x', padx=20, pady=10)
        
        self.option_var = IntVar(value=1)
        self.publication_radio = Radiobutton(master, text="Publication", variable=self.option_var, value=1)
        self.publication_radio.pack(pady=10)
        self.question_radio = Radiobutton(master, text="Question", variable=self.option_var, value=2)
        self.question_radio.pack(pady=10)

        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        keywords = self.keyword_var.get().strip()
        cf_clearance = self.cf_clearance_var.get().strip()
        user_agent = self.user_agent_var.get().strip()
        option = self.option_var.get()
        
        print(keywords)
        print(cf_clearance)
        print(user_agent)

        if option == 1:
            research_publication(keywords,cf_clearance, user_agent)
        elif option == 2:
            research_question(keywords,cf_clearance, user_agent)
        else:
            results = "Please select an option."

        print('已經完成')
        
