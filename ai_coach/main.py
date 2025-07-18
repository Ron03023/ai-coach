import streamlit as st
from coach import chat_with_ai
from database import init_db, add_task, list_tasks

init_db()

st.title("AI Performance Coach 🧠💪")

mode = st.sidebar.selectbox("Choose your coach mode", ["Fitness", "Productivity"])

if mode == "Fitness":
    st.header("Workout & Diet")
    user_input = st.text_input("Talk to your fitness coach:")
    if st.button("Send"):
        reply = chat_with_ai(user_input, role="fitness")
        st.write("💬 Coach:", reply)

elif mode == "Productivity":
    st.header("Tasks + Pomodoro")
    task = st.text_input("New Task")
    if st.button("Add Task"):
        add_task(task)
        st.success("Task added.")
    
    st.subheader("Your Tasks")
    for task in list_tasks():
        st.write("📝", task[1])

    st.subheader("Chat with Productivity Coach")
    user_input = st.text_input("Talk to your coach:")
    if st.button("Send to coach"):
        reply = chat_with_ai(user_input, role="productivity")
        st.write("🧠 Coach:", reply)
