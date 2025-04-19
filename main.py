import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, date
import plotly.express as px
import random

# Connect to DB
conn = sqlite3.connect('expenses.db', check_same_thread=False)
c = conn.cursor()

# Tables
c.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    amount REAL,
    category TEXT,
    date TEXT,
    note TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS income (
    username TEXT,
    month TEXT,
    amount REAL,
    PRIMARY KEY(username, month)
)''')

c.execute('''CREATE TABLE IF NOT EXISTS savings_goal (
    username TEXT PRIMARY KEY,
    goal_amount REAL,
    deadline TEXT
)''')

conn.commit()

# Functions
def signup(username, password):
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def login(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone() is not None

def add_expense(username, amount, category, note):
    c.execute("INSERT INTO expenses (username, amount, category, date, note) VALUES (?, ?, ?, ?, ?)",
              (username, amount, category, str(date.today()), note))
    conn.commit()

def get_expenses(username):
    c.execute("SELECT amount, category, date, note FROM expenses WHERE username = ?", (username,))
    return c.fetchall()

def set_income(username, month, amount):
    c.execute("REPLACE INTO income (username, month, amount) VALUES (?, ?, ?)", (username, month, amount))
    conn.commit()

def get_income(username, month):
    c.execute("SELECT amount FROM income WHERE username = ? AND month = ?", (username, month))
    result = c.fetchone()
    return result[0] if result else 0

def set_savings_goal(username, goal_amount, deadline):
    c.execute("REPLACE INTO savings_goal (username, goal_amount, deadline) VALUES (?, ?, ?)",
              (username, goal_amount, deadline))
    conn.commit()

def get_savings_goal(username):
    c.execute("SELECT goal_amount, deadline FROM savings_goal WHERE username = ?", (username,))
    return c.fetchone()

def get_daily_tip():
    tips = [
        "Cut down on takeout and cook at home!",
        "Track your spending daily to stay on top!",
        "Set small, weekly savings goals.",
        "Review your subscriptions monthly.",
        "Avoid impulse shopping — use a 24-hour rule."
    ]
    return random.choice(tips)

# Login / Signup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.set_page_config(page_title="Daily Budget Pro", layout="centered")

if not st.session_state.logged_in:
    st.title("💸 Daily Budget Pro")
    choice = st.selectbox("Login or Signup", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):
        if choice == "Signup":
            try:
                signup(username, password)
                st.success("Signup successful. Please log in.")
            except:
                st.error("Username already exists.")
        else:
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Login failed. Try again.")
else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    page = st.sidebar.radio("Go to", ["Add Expense", "View Summary", "Savings Goal", "Set Income", "Logout"])

    if page == "Add Expense":
        st.title("📝 Add Expense")
        amount = st.number_input("Amount (₹)", min_value=0.0)
        category = st.selectbox("Category", ["Food", "Travel", "Bills", "Shopping", "Other"])
        note = st.text_input("Note (optional)")
        if st.button("Add"):
            add_expense(st.session_state.username, amount, category, note)
            st.success("Expense added.")

    elif page == "View Summary":
        st.title("📊 Expense Summary")
        expenses = get_expenses(st.session_state.username)
        df = pd.DataFrame(expenses, columns=["Amount", "Category", "Date", "Note"])
        st.dataframe(df)

        if not df.empty:
            st.subheader("Spending by Category")
            fig = px.pie(df, names="Category", values="Amount", title="Spending Breakdown")
            st.plotly_chart(fig)

            current_month = datetime.now().strftime("%B")
            income = get_income(st.session_state.username, current_month)
            total_spent = df["Amount"].sum()
            savings = income - total_spent if income else 0

            st.metric("Income (₹)", income)
            st.metric("Spent (₹)", total_spent)
            st.metric("Saved (₹)", savings)

            score = 10 if savings > income * 0.2 else 7 if savings > 0 else 4
            st.info(f"💯 Monthly Scorecard: {score}/10")

        st.subheader("💡 Tip of the Day")
        st.success(get_daily_tip())

    elif page == "Savings Goal":
        st.title("🎯 Savings Goal Tracker")
        goal = get_savings_goal(st.session_state.username)

        if goal:
            goal_amount, deadline = goal
            st.success(f"Goal: ₹{goal_amount:.2f} by {deadline}")
            current_month = datetime.now().strftime("%B")
            income = get_income(st.session_state.username, current_month)
            c.execute("SELECT SUM(amount) FROM expenses WHERE username = ?", (st.session_state.username,))
            spent = c.fetchone()[0] or 0
            savings = income - spent if income else 0
            st.metric("Current Savings", f"₹{savings:.2f}")
            st.progress(min(savings / goal_amount, 1.0))

        with st.form("Set Goal"):
            amount = st.number_input("Target Amount (₹)", min_value=100.0)
            deadline = st.date_input("Deadline")
            if st.form_submit_button("Save Goal"):
                set_savings_goal(st.session_state.username, amount, deadline.strftime("%Y-%m-%d"))
                st.success("Goal saved!")

    elif page == "Set Income":
        st.title("💼 Set Monthly Income")
        current_month = datetime.now().strftime("%B")
        income = st.number_input(f"Enter income for {current_month}", min_value=0.0)
        if st.button("Save Income"):
            set_income(st.session_state.username, current_month, income)
            st.success("Income saved.")

    elif page == "Logout":
        st.session_state.logged_in = False
        st.rerun()

