from Functions import fetch #to transfer the value topic/entry
from Functions import save_news
from Functions import view_news
import tkinter as tk
from PIL import ImageTk
import pyglet


# fonts
pyglet.font.add_file("../Assets/AbrilFatface-Regular.ttf")
pyglet.font.add_file("../Assets/RobotoMono-Regular.ttf")

# colours
beige = "#f5f5dc"
dark_beige = "#cbb799"
mid = "#a07856"
light_brown = "#6f4d38"
dark_brown = "#632611"

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False) #doesn't allow to propagate influence of one element

    #logo widget
    logo_img = ImageTk.PhotoImage(file="../Assets/NewsAPILogo160x160.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack(pady=5)

    tk.Label(
        frame1, #it is part of frame1
        text="Bringing you the latest headlines from across the globe — \nfast, focused, and filtered your way.\nSearch. Save. Stay updated.\nWhether you're tracking trends or digging into the deep,\nwe’ve got your news — one query at a time.",
        bg=beige,
        fg=dark_brown,
        font=("Abril Fatface", 14)
        ).pack()

    # Search News Button widget
    tk.Button(
        frame1,
        text="Search News",
        font=("Abril Fatface", 18, "bold"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: load_frame2()  # calls load_frame2() [lambda->when clicked]
        ).pack(pady=10)  # creates gaps in-between elements

    # View News Button widget
    tk.Button(
        frame1,
        text="View Saved News",
        font=("Abril Fatface", 18, "bold"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: (get_saved_news(), load_frame5())  # calls load_frame5() [lambda->when clicked]
        ).pack(pady=10)  # creates gaps in-between elements

    # Close button
    tk.Button(
        frame1,
        text="Exit",
        font=("Abril Fatface", 15, "bold italic"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: root.destroy()  # calls load_frame2() [lambda->when clicked]
    ).pack(pady=10)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    global entry


    #logo Widget
    logo_img = ImageTk.PhotoImage(file="../Assets/NewsAPILogo160x160.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack(pady=5)

    #label
    tk.Label(
        frame2, #it is the part of frame2
        text="Search Top 5 Headlines of the Day",
        bg=beige,
        fg=dark_brown,
        font=("Abril Fatface", 20)
        ).pack(pady=25, padx=25)

    #label 2
    tk.Label(
        frame2,
        text="Enter your Topic or a Keyword",
        bg=light_brown,
        fg=beige,
        font=("Roboto Mono", 12)
        ).pack(fill="both") #stretches the bg to the horizontal edges

    # Entry Widget
    entry = tk.Entry(frame2,
                     width=50)
    entry.pack(pady=10)

    # Search button
    search_button = tk.Button(frame2,
                              text="Search",
                              font=("Abril Fatface", 18, "bold"),
                              bg=dark_brown,
                              fg=dark_beige,
                              cursor="hand2",
                              activebackground=mid,
                              activeforeground=dark_brown,
                              command=lambda: (on_search(),load_frame3())
                              )
    search_button.pack()

    # Back button widget
    tk.Button(
        frame2,
        text="Back",
        font=("Abril Fatface", 15, "bold italic"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: load_frame1()# calls load_frame1() [lambda->when clicked]

        ).pack(pady=20)  # creates gaps in-between elements

def load_frame3():
    frame3.tkraise()
    clear_widgets(frame2)

    # logo Widget
    logo_img = ImageTk.PhotoImage(file="../Assets/NewsAPILogo160x160.png")
    logo_widget = tk.Label(frame3, image=logo_img, bg=beige)
    logo_widget.image = logo_img  # Already done but it is needed
    logo_widget.pack(pady=5)

    # text 1 Heading
    tk.Label(
        frame3,  # it is part of frame1
        text=f"Top results based on search '{topic}'",
        bg=beige,
        fg=dark_brown,
        font=("Abril Fatface", 20)
    ).pack(pady=10)

    # text 2 Headlines
    text_output = tk.Text(frame3,
                          wrap="word",
                          width=80,
                          height=20,
                          bg=light_brown,
                          fg=beige,
                          font=("Roboto Mono", 12, "bold")
                          ) # stretches the bg to the horizontal edges
    text_output.pack(pady=20)

    text_output.config(state="normal")
    text_output.delete("1.0","end")
    text_output.insert("1.0", all_headlines)
    text_output.config(state="disabled")

    # Save Results button widget
    tk.Button(
        frame3,
        text="Save Results",
        font=("Abril Fatface", 15, "bold"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: (save_news(), load_frame4())).pack(pady=10)

    # Back button widget
    tk.Button(
        frame3,
        text="Back",
        font=("Abril Fatface", 15, "bold italic"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: load_frame1()).pack(pady=10)

def load_frame4(): # Saved window
    clear_widgets(frame3)
    frame3.tkraise()

    #Label
    tk.Label(
        frame3,  # it is part of frame1
        text=f"Results have been saved to file\n NewsApiDataBase.txt",
        bg=beige,
        fg=dark_brown,
        font=("Abril Fatface", 20)
    ).pack(pady=10)

    # Back button widget
    tk.Button(
        frame3,
        text="Back",
        font=("Abril Fatface", 15, "bold italic"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: load_frame1()).pack(pady=10)

def load_frame5():
    frame5.tkraise()
    clear_widgets(frame1)
    #Label
    tk.Label(
        frame5,  # it is part of frame1
        text=f"Previously saved News\nNewsApiDataBase",
        bg=beige,
        fg=dark_brown,
        font=("Abril Fatface", 20)
    ).pack(pady=10)

    # text 1 Saved News
    text_output = tk.Text(frame5,
                              wrap="word",
                              width=80,
                              height=25,
                              bg=light_brown,
                              fg=beige,
                              font=("Roboto Mono", 12, "bold")
                              ) # stretches the bg to the horizontal edges
    text_output.pack(pady=20)

    text_output.config(state="normal")
    text_output.delete("1.0","end")
    text_output.insert("1.0", saved_news)
    text_output.config(state="disabled")

    # Back button widget
    tk.Button(
        frame5,
        text="Back",
        font=("Abril Fatface", 15, "bold italic"),
        bg=dark_brown,
        fg=dark_beige,
        cursor="hand2",
        activebackground=mid,
        activeforeground=dark_brown,
        command=lambda: load_frame1()).pack(pady=20)

def on_search():
    global topic
    global all_headlines
    topic = entry.get()
    fetch(topic)  # pass it directly
    all_headlines = fetch(topic)
def get_saved_news():
    global saved_news
    saved_news = view_news()


# initialize app
root = tk.Tk()
root.title("NewsAPI Fetch") # Gives a title to the window
root.eval("tk::PlaceWindow . center") # Places the window in center

# Create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=beige)# Size and BG Colour
frame2 = tk.Frame(root, bg=beige)
frame3 = tk.Frame(root, bg=beige)
frame4 = tk.Frame(root, bg=beige)
frame5 = tk.Frame(root, bg=beige)

for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, column=0, sticky="nesw") #sticks bg to all directions
    #this does
    #frame1.grid(row=0, column=0)  # Default Values
    #frame2.grid(row=0, column=0)
    #frame3.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()