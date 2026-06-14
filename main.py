import tkinter as tk
from newspaper import Article
from textblob import TextBlob
import nltk

# Download NLTK data
nltk.download('punkt')

def summarize():
    try:
        url = utext.get("1.0", "end").strip()

        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Enable text boxes
        title.config(state="normal")
        author.config(state="normal")
        publication.config(state="normal")
        summary.config(state="normal")
        sentiment.config(state="normal")

        # Clear previous content
        title.delete("1.0", "end")
        author.delete("1.0", "end")
        publication.delete("1.0", "end")
        summary.delete("1.0", "end")
        sentiment.delete("1.0", "end")

        # Insert article information
        title.insert("1.0", article.title)

        author.insert(
            "1.0",
            ", ".join(article.authors) if article.authors else "Not Available"
        )

        publication.insert(
            "1.0",
            str(article.publish_date) if article.publish_date else "Not Available"
        )

        summary.insert("1.0", article.summary)

        # Sentiment Analysis
        analysis = TextBlob(article.text)

        if analysis.sentiment.polarity > 0:
            result = "Positive 😊"
        elif analysis.sentiment.polarity < 0:
            result = "Negative 😞"
        else:
            result = "Neutral 😐"

        sentiment.insert("1.0", result)

        # Disable text boxes
        title.config(state="disabled")
        author.config(state="disabled")
        publication.config(state="disabled")
        summary.config(state="disabled")
        sentiment.config(state="disabled")

    except Exception as e:
        print("Error:", e)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("AI News Summarizer")
root.geometry("1200x700")

# Title
tk.Label(root, text="Title", font=("Arial", 12, "bold")).pack()
title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

# Author
tk.Label(root, text="Author", font=("Arial", 12, "bold")).pack()
author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

# Publication Date
tk.Label(root, text="Publication Date", font=("Arial", 12, "bold")).pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

# Summary
tk.Label(root, text="Summary", font=("Arial", 12, "bold")).pack()
summary = tk.Text(root, height=15, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

# Sentiment
tk.Label(root, text="Sentiment Analysis", font=("Arial", 12, "bold")).pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

# URL
tk.Label(root, text="Article URL", font=("Arial", 12, "bold")).pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button
btn = tk.Button(
    root,
    text="Summarize",
    font=("Arial", 12, "bold"),
    command=summarize
)
btn.pack(pady=10)

root.mainloop()