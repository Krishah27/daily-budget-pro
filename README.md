# 💰 Daily Budget Pro — Smart Expense Tracker App

A personal finance tracker built using Python, Streamlit, and SQLite — perfect for students & professionals to manage income, expenses, and savings with ease.


## 📌 Project Overview
Daily Budget Pro is a clean, beginner-friendly budgeting app that helps you manage your daily expenses, track income, and stay on top of your savings goals. Built with a full login system and dynamic visualizations, it’s a perfect example of how real-world Python projects can be both functional and beautiful.


📝 **Note** : As a first-year B.Tech CSE student, this is just the beginning of my journey into app development and real-world projects. I'm excited to learn and grow, and this project marks the first of many steps I plan to take!


## 🧠 Why I Built This?
Being a first-year B.Tech student, I wanted to step beyond the classroom and create something practical — not just a “to-do list” app. I saw a real need for better financial management tools, especially for students and young professionals. This project helped me:

1. Understand both frontend (UI) and backend logic

2. Work with local databases (SQLite)

3. Visualize real-time data


## ✅ Features

🔐 Secure user login/signup system

📝 Add and categorize daily expenses with optional notes

💼 Set and track monthly income

📊 View summary with pie chart visualization by category

💾 All data stored in local SQLite database

🎯 Set savings goals and track progress with visual indicators

📅 Automatically tracks expenses by date

📈 Monthly scorecard based on income and expenses

💡 Daily budgeting tips to encourage healthy financial habits

⚠️ Real-time warning popup when spending too much in a specific category (like “You're spending more on Food!”)


## 🛠️ Tech Stack

Python 3.10+

Streamlit

Pandas

Plotly & Altair for visualization

SQLite (Local DB)

Spyder IDE + Anaconda



## 🛠️ How to Run Locally

Follow these steps to set up and run the app on your local machine:

### STEP 1️⃣ : Clone the repository

git clone https://github.com/Krishah27/daily-budget-pro <br>
cd daily-budget-pro


### STEP 2️⃣ : Install dependencies

Make sure you have Python installed. Then install required packages using:


pip install -r Requirements.txt


### STEP 3️⃣ : Set up the database

Run the following script once to create the initial SQLite database (`expenses.db`):

python setup_db.py

This will automatically create the necessary tables in the database.

### STEP 4️⃣ : Run the app

Launch the Streamlit app using:


streamlit run main.py


Your browser will open at `http://localhost:8501` and the app will be live!


⚠️ **Note**: If `expenses.db` already exists, you don’t need to run `setup_db.py` again unless you want to reset the data.


## REQUIREMENTS 

streamlit==1.32.0 <br>
pandas==2.2.1 <br>
plotly==5.19.0 <br>
altair==5.2.0 <br>
Pillow==10.2.0 <br>

SQLite is built-in with Python. No need to install it separately.

## 🌟 What Makes This Project Unique?

There are many expense tracking apps out there — but here’s what makes Daily Budget Pro stand out from the crowd :

✅ Smart Overspending Alerts
→ The app includes a real-time warning system that notifies users when they overspend in specific categories (e.g., Food, Shopping). It’s like having a mini financial advisor watching your habits and keeping you in check.

✅ Daily Financial Tips
→ Users receive a fresh budgeting tip every day to improve their financial habits, making this app both a tracker and a coach.

✅ Interactive Visual Summaries
→ Clear and colorful pie charts help users understand their spending patterns instantly. It’s not just data — it’s insight.

✅ Monthly Scorecard
→ Based on income vs spending, users receive a monthly score (out of 10) to reflect how well they're managing money — a gamified motivator to do better!

✅ Savings Goal Tracker
→ Users can set savings goals with deadlines and visually track their progress, making goal setting both fun and rewarding.

✅ Offline-First, No Sign-Up Needed
→ Unlike apps like Mint or Spendee which require constant internet & account setup, this runs entirely on your local machine. Just open and use !

✅ Lightweight & Beginner-Friendly
→ Many financial apps are loaded with complex dashboards and require sign-ins or subscriptions. This app has a clean, minimal interface perfect for new users and students.

✅ Built Completely with Python + Streamlit
→ No external UI libraries, no JS or backend frameworks. Just Python — showing the power of simple tools !

✅ Customizable for Any Use Case
→ Want to track hostel expenses? Add categories? Modify income logic? You can easily edit the code — unlike closed-source tools.

✅ Educational Project, Not Just a Tool
→ This isn't just an app — it's a complete solo-built project showcasing Python, database management (SQLite), data visualization, and UI logic. Great for learning and portfolio-building.

✅ No Tracking or Ads
→ Unlike mobile apps that track data or show ads, this app is 100% privacy-respecting. Your data stays on your device.

✅ Anaconda + Spyder Ready
→ Most budget apps run on cloud/web platforms. This is made with beginners in mind — fully compatible with Anaconda and Spyder IDE.


## 📈 Future Improvements

Add Google login / Firebase integration

Export reports as PDF

Cloud database support

Monthly budget reminders

## 🙋‍♂️ About Me

Hey ! I’m a first-year Computer Science student passionate about building real-world projects using Python and AI. This project is one of my first attempts at building a fully functional app — and I’m really proud of it ! I’m just starting my journey into software development, and I can’t wait to learn more. I believe in learning by building, and I'm constantly exploring ways to improve everyday life with technology.
Looking forward to growing as a developer and building more impactful tools !

## Let’s connect! 🔗 https://www.linkedin.com/in/krishna-shah-9a1a27316?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

⭐ Like this project? Feel free to fork, star ⭐, and share your feedback! Requests & Ideas are Welcome 🙌

## ⚡ Made with Python & ❤️
