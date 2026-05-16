from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

cash_amount = 0

def add_room(db, key, value):
    global cash_amount
    if len(db) != 5:
        db[key] = value
        print(int(value))
        cash_amount += (int(value) * 100)
        print(cash_amount)
        print(db)
    else:
        error("Sorry" , "All Rooms are Full!")


def delete_room(db, key):
    print(db)
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


def rob_room():
    global cash_amount
    selected_item = listbox.value
    if selected_item:
        name = selected_item.split(":", 1)[0].strip()
        if name in db:
            db[name] += "😂"
            cash_amount += 100
            _update_listbox(db)


def _add_room():
    name = name_entry.value.strip()
    room = room_entry.value.strip()
    

    if name and room:
        if room.isdigit():
            days = int(room)
            if days > 0:
                add_room(db, name, room)
                _update_listbox(db)
                name_entry.clear()
                room_entry.clear()
            else:
                error("Input Error", "Please Input a Valid Number")
        else:
            error("Input Error", "Please Input a Valid Number")
    else:
        error("Input Error", "Both fields must be filled out.")

# Global dictionary to store rooms
db = {}

# Function to update the listbox with current rooms
def _update_listbox(db):
    listbox.clear()
    for i in update_listbox(db):
        listbox.append(i)

def _update_cashamount():
    global cash_amount
    # Display the current value of the variable
    MoneyUi.value = f"Money: ${cash_amount}"
    # Schedule the next update in 1000ms (1 second)
    MoneyUi.after(1000, _update_cashamount)


# Function to delete a room
def _delete_room():
    global cash_amount
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
MoneyUi = Text(bottom_pane, text=cash_amount, width="15" , align="left")
PushButton(bottom_pane, text="Check Out", align="left", command=_delete_room)
PushButton(bottom_pane, text="Rob", align="left", command=rob_room)

MoneyUi.after(1000, _update_cashamount)

# Function to handle enter key press
def handle_enter(event):
    if event.tk_event.keysym == "Return":
        _add_room()

# Bind enter key press event to handle_enter function
app.when_key_pressed = handle_enter

_update_listbox(db) # Initial update of listbox


app.display()