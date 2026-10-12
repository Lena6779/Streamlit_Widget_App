# NEEDED IMPORTS 
import streamlit as st
from datetime import date


st.title("Book Writing Planner")
st.write("Plan your book idea and track your writing progress along the way")

st.header("Book Details")

book_title = st.text_input("Book Title")
genre = st.selectbox(
    "Genre",
    ["Fantasy", "Mystery", "Romance", "Horror", "Science Fiction", "Nonfiction"]
)

if book_title:
    st.write(f"You're writing **{book_title}**, a {genre.lower()} book.")

# Word count and progress calculation

st.header("Writing Progress")

genre_ranges = { # Did some research and this is usually the word-count ranges based on common publishing guidelines known for different generes 
    "Fantasy": (80000, 150000, 100000),
    "Science Fiction": (80000, 150000, 100000),
    "Mystery": (60000, 100000, 80000),
    "Romance": (50000, 100000, 75000),
    "Horror": (60000, 100000, 80000),
    "Nonfiction": (40000, 100000, 70000),
}

# The tuple seen in the dictionary above for each genre
min_words, max_words, default_words = genre_ranges[genre] 

target_words = st.number_input(
    "Target word count",
    min_value=min_words,
    max_value=max_words,
    value=default_words,
    step=1000
)
words_written = st.number_input(
    "Words written so far",
    min_value=0,
    value=0,
    step=100
)

num_chapters = st.slider("Number of chapters", min_value=1, max_value=50, value=20)

# Calculations
progress = words_written / target_words
words_remaining = max(target_words - words_written, 0)
words_per_chapter = target_words // num_chapters

# Display results
col1, col2, col3 = st.columns(3)
col1.metric("Percent Complete", f"{progress:.0%}")
col2.metric("Words Remaining", f"{words_remaining:,}")
col3.metric("Words per Chapter", f"{words_per_chapter:,}")

st.progress(min(progress, 1.0))

# Conditional messages
if progress >= 1:
    st.success("🎉 You hit your target word count! Congratulations! Now time to edit all your hard work!")
elif progress >= 0.5:
    st.info("You're past the halfway point. Keep writing; don't give up!")
elif progress > 0:
    st.info("Good start so far! Every word counts to creating your ideal good story.")
else:
    st.warning("You haven't started yet but don't fret, try writing 500 words today and make it a habit.")

st.header("Deadline")

deadline = st.date_input("When do you want to finish?")

days_left = (deadline - date.today()).days

if days_left > 0:
    words_per_day = words_remaining / days_left
    st.metric("Words per Day Needed", f"{words_per_day:,.0f}")

    if words_per_day > 2000:
        st.warning("That's a lot of words per day. Consider moving your deadline for later. Give yourself time to write!")
    elif words_per_day > 0:
        st.success("That's a doable daily goal! Good job!")
elif days_left == 0:
    st.warning("Your deadline is today! Write at full steam!")
else:
    st.warning("That date has already passed. Pick a future date for your book to be ready.")