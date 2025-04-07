from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Chat, Channel
from pick import pick

# Configure your Telegram API credentials
api_id = '__'  # Replace with your api_id
api_hash = '__'  # Replace with your api_hash
phone = '__'  # e.g., +861234567890

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

    if not group_list:
        print("No groups found.")
        client.disconnect()
        return
    
    # Use pick for interactive multi-selection
    title = "Please select the groups to leave (use arrow keys to move, space to select, Enter to confirm):"
    options = [f"{dialog.title} (ID: {dialog.id})" for dialog in group_list]
    selected = pick(options, title, multiselect=True, min_selection_count=1)

    # Execute leave operation
    for option, idx in selected:
        group = group_list[idx]
        print(f"Leaving: {group.title}")
        try:
            if isinstance(group, Channel):
                from telethon.tl.functions.channels import LeaveChannelRequest
                client(LeaveChannelRequest(group))
                try:
                    client.delete_dialog(group.id)
                except Exception as del_ex:
                    print(f"Failed to delete dialog for {group.title}: {del_ex}")
            elif isinstance(group, Chat):
                client.delete_dialog(group.id)
            else:
                print("Unsupported group type")
        except Exception as e:
            print(f"Failed to leave {group.title}: {e}")
        else:
            print(f"Left: {group.title}")

    print("Operation completed!")
    client.disconnect()
    
if __name__ == "__main__":
    main()