from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Configure your Telegram API credentials
api_id = 'YOUR API_ID'  # Replace with your api_id
api_hash = 'YOUR API_HASH'  # Replace with your api_hash
phone = 'YOUR PHONE NUMBER'  # e.g., +861234567890

# Initialize Telegram client
client = TelegramClient(phone, api_id, api_hash)

def main():
    # Connect to Telegram
    client.start()
    print("Connected to Telegram!")

    # Get all dialogs (including groups)
    dialogs = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,  # Increase if more than 200 groups
        hash=0
    ))

    # Store group list
    group_list = []
    print("\nHere are your joined groups:")
    for i, dialog in enumerate(dialogs.chats):
        if hasattr(dialog, 'title'):  # Only process groups
            group_list.append(dialog)
            print(f"{i + 1}. {dialog.title} (ID: {dialog.id})")

    # User selects groups to leave
    selected = input("\nPlease enter the group numbers to leave (separated by commas, e.g., 1,3,5):")
    selected_indices = [int(x.strip()) - 1 for x in selected.split(',') if x.strip().isdigit()]

    # Execute leave operation
    for idx in selected_indices:
        if 0 <= idx < len(group_list):
            group = group_list[idx]
            print(f"Leaving: {group.title}")
            client.delete_dialog(group.id)
            print(f"Left: {group.title}")
        else:
            print(f"Invalid number: {idx + 1}")

    print("Operation completed!")
    client.disconnect()
    
if __name__ == "__main__":
    main()