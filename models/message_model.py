import sqlite3
from collections import defaultdict

def save_message(user_id, role, content, timestamp):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (user_id, role, content, timestamp) VALUES (?, ?, ?, ?)", (user_id, role, content, timestamp))
    conn.commit()
    conn.close()

#def get_messages(user_id):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages WHERE user_id = ?", (user_id,))
    messages = c.fetchall()
    conn.close()
    return messages


def get_messages_grouped(user_id):
    """
    Retourne les messages groupés par timestamp de session.
    """
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("""
        SELECT timestamp, role, content 
        FROM messages 
        WHERE user_id = ?
        ORDER BY timestamp ASC
    """, (user_id,))
    rows = c.fetchall()
    conn.close()

    grouped = defaultdict(list)
    for timestamp, role, content in rows:
        grouped[timestamp].append((role, content))

    return grouped