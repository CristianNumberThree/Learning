import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

class QuizApp:
    def __init__(self, master):
        #The master window of the program
        self.master = master
        self.master.title("Quiz")

        # Variables
        self.name_var = tk.StringVar()
        self.Preference = 0

        # Create entry widgets for name and preference
        self.create_name_widgets()
        self.create_preference_widgets()

        # Create buttons to start the quiz
        waifu_button = tk.Button(master, text="Waifu", command=lambda: (self.start_quiz(), self.waifu_preference()))
        waifu_button.pack(pady=2)

        husbando_button = tk.Button(master, text="Husbando", command=self.start_quiz)
        husbando_button.pack(pady=2)

        # extra easter egg button for use in full version
        easter_egg_button = tk.Button(master, text="Ewww", command=self.display_reversed_name)
        easter_egg_button.pack(pady=2)

        # Quiz data
        self.setup_quiz_data()

    def create_name_widgets(self):
        # label for the first question
        name_label = tk.Label(self.master, text="What is your name?")
        name_label.pack(pady=10)
        name_entry = tk.Entry(self.master, textvariable=self.name_var)
        name_entry.pack(pady=5)

    def create_preference_widgets(self):
        # label for the second question
        preference_label = tk.Label(self.master, text="Which do you prefer?")
        preference_label.pack(pady=10)

    def setup_quiz_data(self):
        # Quiz questions can be changed to match any criteria
        self.questions = [
            "Are you normally dishonest?",
            "Is physical appearance important?",
            "Is money more important than your relationship?",
            "Is cool better than cute?",
            "Is it important for your significant other to be calmer than you?",
            "Are good and evil always clearly defined?",
            "Do you want to have children? (if you have children put yes)",
            "Is reaching your goals more important than maintaining your relationship?",
            "Would you commit a crime for your significant other?",
            "Honestly though does your significant other's sex really matter?",
        ]

        # Answers table the answers must be within brackets and in the correct order
        self.answers = ["Yes"] * 10

        # The list of results from the answers to; name input, preference, and quiz questions are added and then referenced to in this table
        self.PreferenceList = ["Artoria Pendragon", "Loid Forger", "Levi Ackerman", "Kyo Sohma", "Kakashi Hatake",
                               "Takumi Usui", "Tomoe", "Inuyasha", "Howl Jenkins Pendragon", "Gojo Satoru",
                               "Astolfo", "Hinata Hyuga", "Ochaco Uraraka", "Asuna Yuuki", "Mikasa Akerman",
                               "Kaguya Shinomiya", "Rin Tohsaka", "Rias Gremory", "Nami", "Makima",
                               "Red", "Blue", "Green", "Pink", "Orange",
                               "Yellow", "Black", "White", "Purple", "Brown",
                               "Cyan","Lime","Maroon","Rose","Banana",
                               "Gray","Tan","Coral","Fortegreen","Olive","Yellow(color bug)"]
        
        # The descriptions to the results from the preference table
        self.DescriptionsList = ["The king of knights, I honestly can't blame you",
                                 "World class spy and perfect father",
                                 "Slaying titans with finesse, and he's hot",
                                 "Just don't take the bracelet off I guess",
                                 "He can see right through you so calm down",
                                 "Can you keep a secret? He can.",
                                 "A fox yokai?! Sheeeeesh",
                                 "He will always love you...even after you reincarnate",
                                 "M'Lord",
                                 "It'll all be fine, after all you are kind of weak",
                                 "Next level pretty boy",
                                 "But how though?",
                                 "Floating on cloud 9",
                                 "The perfect co-op partner",
                                 "Don't read the last chapter of the manga",
                                 "Love is war",
                                 "A mage and a Tsundere",
                                 "A kind devil?",
                                 "Keep your wallet close",
                                 "Well dang better luck next time",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus",
                                 "No name? ngl kinda sus, but at least you got the rare one"]
        
        # images to provide visual for descriptions
        self.ResultImage = ["Altria.png","Loid.jpg","Levi.png","Kyo.jpg","Kakashi.png",
                       "Takumi.png","Tomoe.png","Inuyasha.png","Howl.jpg",
                       "Gojo.png","Astolfo.png","Hinata.png","Ochaco.png","Asuna.jpg",
                       "Mikasa.png","Kaguya.jpg","Rin.jpg","Rias.jpg","Nami.png",
                       "Makima.png","Red.jpg","Blue.jpg","Green.jpg","Pink.jpg",
                       "Orange.jpg","Yellow.jpg","Black.jpg","White.jpg","Purple.jpg",
                       "Brown.jpg","Cyan.jpg","Lime.jpg","Maroon.jpg","Rose.jpg",
                       "Banana.jpg","Gray.jpg","Tan.jpg","Coral.jpg","Fortegreen.jpg",
                       "Olive.jpg","Yellow(color bug).jpg"]

        # Counter for correct answers
        self.correct_count = 0

    def reverse_name(self):
        # reverses the name input for use in easter egg feature
        self.name = self.name_var.get()
        self.reversed_name = self.name[::-1]

    def display_reversed_name(self):
        # The easter egg feature it is better in the full version
        easter_egg = Image.open("alternate.jpg")
        self.reverse_name()
        messagebox.showwarning("Easter Egg", f"Your perfect match is {self.reversed_name}")
        easter_egg.show()
        self.master.destroy()

    def start_quiz(self):
        # Get user input
        name = self.name_var.get()

        # Check if name is provided
        if name:
            # Open quiz window
            quiz_window = tk.Toplevel(self.master)
            quiz_window.title("Answer with Yes or No")
            answer_entries = []

            # Create labels for questions and entry widgets for answers
            for i in range(10):
                question_label = tk.Label(quiz_window, text=self.questions[i])
                question_label.pack(pady=5)

                answer_entry = tk.Entry(quiz_window)
                answer_entry.pack(pady=5)
                answer_entries.append(answer_entry)

            # Create a button to submit answers
            submit_button = tk.Button(quiz_window, text="Submit Answers", command=lambda: self.check_answers(answer_entries))
            submit_button.pack(pady=10)

        else:
            # Open quiz window
            self.Preference += 20
            quiz_window = tk.Toplevel(self.master)
            quiz_window.title("Answer with Yes or No")
            answer_entries = []

            # Create labels for questions and entry widgets for answers
            for i in range(10):
                question_label = tk.Label(quiz_window, text=self.questions[i])
                question_label.pack(pady=5)

                answer_entry = tk.Entry(quiz_window)
                answer_entry.pack(pady=5)
                answer_entries.append(answer_entry)

            # Create a button to submit answers
            submit_button = tk.Button(quiz_window, text="Submit Answers", command=lambda: self.check_answers(answer_entries))
            submit_button.pack(pady=10)

    def waifu_preference(self):
        # sets the preference to waifu if so desired
        self.Preference += 10

    def check_answers(self, answer_entries):
        # Check user answers and update correct_count
        for i in range(10):
            user_answer = answer_entries[i].get()
            correct_answer = str(self.answers[i])

            if user_answer.lower() == correct_answer.lower():
                self.correct_count += 1

        # Display results
        self.display_results()

    def show_preference(self):
        # Variable that retieves results from Preference List and Description List
        self.result = self.correct_count + self.Preference 

    def display_results(self):
        # Display the quiz results in a messagebox
        # Displays image to provide clarity
        self.show_preference()
        Result_Image_show=Image.open(self.ResultImage[self.result])
        Result_Image_show.show()
        messagebox.showinfo(
            self.DescriptionsList[self.result],
            f"Congratulations {self.name_var.get()} your perfect anime match is {self.PreferenceList[self.result]}")
        self.master.destroy()
        
# Executes program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()