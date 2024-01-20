from pyrogram import Client

api_id = "21364355"
api_hash = "72f11aec1dd3e5764554d477341a3d0b"

with Client("your_session_name", api_id, api_hash) as app:
    print(app.export_session_string())
