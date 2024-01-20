from pyrogram import Client

api_id = "your_api_id"
api_hash = "your_api_hash"

with Client("your_session_name", api_id, api_hash) as app:
    print(app.export_session_string())
