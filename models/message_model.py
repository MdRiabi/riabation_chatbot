import sqlite3

def save_message(user_id, role, content):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content))
    conn.commit()
    conn.close()

def get_messages(user_id):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages WHERE user_id = ?", (user_id,))
    messages = c.fetchall()
    conn.close()
    return messages
