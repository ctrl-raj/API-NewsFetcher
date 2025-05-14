# API-NewsFetcher
The News API-Fetcher App is a simple yet functional desktop application built using Python and Tkinter, designed to fetch and display the latest news articles based on user input. It connects to the NewsAPI to retrieve real-time news headlines by keyword or topic, making it a great demonstration of working with APIs and GUI development.
🔧 Core Features:
- Topic-Based Search: Users can type in any keyword (e.g., "AI", "football", "India") and receive the top 5 most recent news articles related to that topic.
- Clean GUI Interface: Built using Tkinter, the app features a clean layout with themed colors and custom fonts to enhance user experience.
- Live API Integration: News data is pulled from the NewsAPI in real time, with results filtered by the current date and sorted by publication time.
- Result Display: For each article, the app shows the title, source, and a clickable URL—all neatly formatted.
- Save to File (Optional): Users can choose to save the fetched results into a local text file for offline reading or future reference.
- UTF-8 Encoding: Handles special characters and symbols correctly while saving text.

👨‍💻 Technical Highlights:
- Built with Python 3
- GUI handled via Tkinter
- Uses the requests library for HTTP requests
- Dynamic content updates based on user input
- Clean string formatting and basic error handling

This app is an ideal beginner-level project for those exploring API consumption, HTTP requests, and GUI programming in Python. It can also be extended with features like language filters, date range selection, or even voice input. Great stepping stone for anyone looking to dive into real-world API-based applications.

📦 Dependencies & Libraries

1. Standard Python Libraries

These come pre-installed with Python:
	•	tkinter – For creating the GUI (buttons, frames, labels, inputs, etc.)
	•	datetime – For using the current date in API queries and timestamps
	•	time – (Optional) For adding delays or sleep between actions
	•	os – (Optional) For file path management and file checking

2. Third-party Libraries

You’ll need to install these manually using pip:
	•	requests
Purpose: To send HTTP GET requests to the NewsAPI and handle the responses

Optional (for extended features):

If you plan to add any enhancements like:
	•	Custom fonts loading: Pillow, pyglet, or font management tools
	•	Charting or visualization: matplotlib or plotly
	•	Data saving in structured formats: pandas or csv

…but for your current build, just these are enough:
- tkinter
- requests
- datetime
- time
- os (optional)
