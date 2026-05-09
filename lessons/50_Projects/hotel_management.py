from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

def add_room(db, key, value):

    if len(db) != 5:
        db[key] = value
        print(db)
    else:
        print("Too Many!")


def delete_room(db, key):
    
    if key in db:
        del db[key]
        print(db)


def update_listbox(db):
    
    if len(db) == 0:
        return []
    else:
        l = []
        for key, value in db.items():
            l.append(f"{key}: {value}")
        
        return l


cash_amount = 0


def rob_room():
    selected_item = listbox.value
    if selected_item:
        name = selected_item.split(":", 1)[0].strip()
        if name in db:
            db[name] += "😂"
            _update_listbox(db)


def _add_room():
    name = name_entry.value.strip()
    room = room_entry.value.strip()
    

    if name and room:
        if room.isdigit():
            add_room(db, name, room)
            _update_listbox(db)
            name_entry.clear()
            room_entry.clear()
        else:
            error("Input Error", "Please Input a Number")
    else:
        error("Input Error", "Both fields must be filled out.")

# Global dictionary to store rooms
db = {}

# Function to update the listbox with current rooms
def _update_listbox(db):
    listbox.clear()
    for i in update_listbox(db):
        listbox.append(i)

# Function to delete a room
def _delete_room():
    selected_item = listbox.value
    if selected_item:
        name = selected_item.split(":", 1)[0].strip()
        if name in db:
            del db[name]
            _update_listbox(db)

# Main app
app = App(title="Hotel Management", width=350, height=400)

# Top pane for input
top_pane = Box(app, align="top", width="fill", border=True)

Text(top_pane, text="Name:", align="left")
name_entry = TextBox(top_pane, width="12", align="left")
Text(top_pane, text="Days:", width="6" , align="left")
room_entry = TextBox(top_pane, width="5", align="left")

PushButton(top_pane, text="Add", width="6", align="bottom", command=_add_room)



# Bottom pane for displaying rooms
bottom_pane = Box(app, align="bottom", width="fill", height="fill", border=True)
listbox = ListBox(bottom_pane, items=[], width="fill", height="fill")
Text(bottom_pane, text="Cash Money: $", width="15" , align="left")
PushButton(bottom_pane, text="Check Out", align="left", command=_delete_room)
PushButton(bottom_pane, text="Rob", align="left", command=rob_room)



# Function to handle enter key press
def handle_enter(event):
    if event.tk_event.keysym == "Return":
        _add_room()

# Bind enter key press event to handle_enter function
app.when_key_pressed = handle_enter

_update_listbox(db) # Initial update of listbox


app.display()