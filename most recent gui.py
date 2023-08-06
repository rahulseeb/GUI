'''
Graphhical user inferface for the video game "The Outbound Ghost".
This allows the user to input specific card data fields.
'''

# Import the tkinter module
import tkinter
import json

# Create the default window
root = tkinter.Tk()
root.title("Card Data")
root.geometry('700x500')


# Create the list of options
tooltips = ["instanceID"]


tooltips_list = []

moves2 = []

#Subcategories for start vars
vars_list = ["cardName", "cardDescription", "rarity", "icon", "cost",
             "targetType", "spChangeOnUse", "currentCost"]

#Subcategories for movelist
moves_list =    ["moveType", "feedbackString","hitFeedbackString",
                "waitUntilEffect","waitUntilContinue", "spawnPrefabWhen",
                "hitPrefab", "hitPrefabYOffset","cardsToDraw", "specialEffects",
                "statusesToApply"]

#Subcategories for keywords
keywords_list = ["limit", "spiritual","rebound", "discardLimitNumber",
                "forceDiscard", "forceLimit", "currentLimit"]

# Variable to keep track of the option
# selected in OptionMenu
toolvar = tkinter.StringVar(root)

vars = tkinter.StringVar(root)

moves = tkinter.StringVar(root)

kwords = tkinter.StringVar(root)

resize = tkinter.StringVar(root)

# Set the default value of the variable
toolvar.set("data")

vars.set("start vars")

moves.set("moves")

kwords.set("keywords")

#Place locations of different menus
tooltips_menu = tkinter.OptionMenu(root, toolvar, *tooltips)
tooltips_menu.config(width=15)  # set the width of the option menu widget
tooltips_menu.place(relx=0.25, rely=0, anchor="ne")  # place the widget halfway vertically

vars_menu = tkinter.OptionMenu(root, vars, *vars_list)
vars_menu.config(width=15)  # set the width of the option menu widget
vars_menu.place(relx=0.75, rely=0, anchor="nw")  # place the widget halfway vertically


moves_menu = tkinter.OptionMenu(root, moves, *moves_list)
moves_menu.config(width=15)  # set the width of the option menu widget
moves_menu.place(relx=0.25, rely=0.4, anchor="ne")  # place the widget halfway vertically



keywords_menu = tkinter.OptionMenu(root, kwords, *keywords_list)
keywords_menu.config(width=15)  # set the width of the option menu widget
keywords_menu.place(relx=0.75, rely=0.4, anchor="nw")  # place the widget halfway vertically

keywords = {}

description_text = None

# Function to show or hide the entry widget based on the selected option
def show_entry_widget(*args):

    global description_text, entry_widget  # Declare the variable as global

    # Get the selected option
    tools_opt = toolvar.get()
    vars_opt = vars.get()
    moves_opt = moves.get()
    key_opt = kwords.get()

    #Ensures multiple categories cannot be selected at once
    if entry_widget:
        entry_widget.place(relx=0.5, rely=0.8, anchor="center")
    else:
        entry_widget = tkinter.Entry(root)
        entry_widget.place(relx=0.5, rely=0.8, anchor="center")

    if tools_opt != "data" and (vars_opt != "start vars" or moves_opt != "moves" or key_opt != "keywords"):
        toolvar.set("data")

    elif vars_opt != "start vars" and (tools_opt != "data" or moves_opt != "moves" or key_opt != "keywords"):
        vars.set("start vars")

    elif moves_opt != "moves" and (tools_opt != "data" or vars_opt != "start vars" or key_opt != "keywords"):
        moves.set("moves")

    elif key_opt != "keywords" and (tools_opt != "data" or vars_opt != "start vars" or moves_opt != "moves"):
        kwords.set("keywords")

    # Show the description text
    if description_text:
        description_text.place_forget()  # Hide the description text

    if vars_opt and vars_opt != "targetType":
        entry_widget.pack()
        entry_widget.place(relx=0.5, rely=0.8, anchor="center")


    if vars_opt == "targetType":
        description_text = tkinter.Text(root, height=8, width=60)
        description_text.place(x=110, y=50)
        description = "Please type in a number from 1-2\n 1 = Player, 2 = Enemy"
        description_text.insert('2.0', description)

    # If the selected option is "Hit Feedback String" or an instanceID, show the entry widget
    if moves_opt and moves_opt != "moveType" and moves_opt != "spawnPrefabWhen":
        entry_widget.pack()
        entry_widget.place(relx=0.5, rely=0.8, anchor="center")

    if moves_opt == "moveType":
        description_text = tkinter.Text(root, height=8, width=60)
        description_text.place(x=110, y=50)
        description = "Please type in a number from 1-3\n 1 = DealDamage, 2 = ApplyStatus, 3 = GainShield."
        description_text.insert('2.0', description)

    if moves_opt == "spawnPrefabWhen":
        description_text = tkinter.Text(root, height=8, width=60)
        description_text.place(x=110, y=50)
        description = "Please type in a number from 1-2\n 1 = Before, 2 = After"
        description_text.insert('2.0', description)

    if moves_opt == "statusesToApply":
        description_text = tkinter.Text(root, height=8, width=60)
        description_text.place(x=110, y=50)
        description = "Please input 2 values for StatusestoApply in the text box:  the instance ID and the counter value.\nThese values are serparated by a space respectively"
        description_text.insert('2.0', description)

    if key_opt:
        entry_widget.pack()
        entry_widget.place(relx=0.5, rely=0.8, anchor="center")

    else:
        entry_widget.pack_forget()

# Create the entry widget
entry_widget = tkinter.Entry(root)




# Call show_entry_widget whenever the selected option changes
toolvar.trace("w", show_entry_widget)
vars.trace("w", show_entry_widget)
moves.trace("w", show_entry_widget)
kwords.trace("w", show_entry_widget)

# Function to print the submitted option and data
def print_answers():
    global finaldict, moves2, keywords

    tvar_opt = toolvar.get()
    svar_opt = vars.get()
    mvar_opt = moves.get()
    keyvar_opt = kwords.get()

    if tvar_opt == "instanceID":
        tooltips_list.append({"instanceID": entry_widget.get()})
        finaldict["tooltips"] = tooltips_list
        print(finaldict)

    if svar_opt in vars_list and svar_opt != "icon" and svar_opt != "targetType":
        finaldict[svar_opt] = entry_widget.get()
        print(finaldict)

    if svar_opt == "icon":
        finaldict[svar_opt] = {"instanceID": entry_widget.get()}
        print(finaldict)

    if svar_opt == "targetType":
        if entry_widget.get() == "1":
            finaldict[svar_opt] = "Player"
        if entry_widget.get() == "2":
            finaldict[svar_opt] = "Enemy"
        print(finaldict)

    if mvar_opt in moves_list and mvar_opt != "moveType" and mvar_opt != "spawnPrefabWhen" and mvar_opt != "hitPrefab" and mvar_opt != "specialEffects" and mvar_opt != "statusesToApply":
        moves2.append({mvar_opt: [entry_widget.get()]})
        finaldict["moves"] = moves2
        print(finaldict)

    if mvar_opt == "spawnPrefabWhen":
        if entry_widget.get() == "1":
            moves2.append({mvar_opt: ["Before"]})
        if entry_widget.get() == "2":
            moves2.append({mvar_opt: ["After"]})
        finaldict["moves"] = moves2
        print(finaldict)

    if mvar_opt == "moveType":
        if entry_widget.get() == "1":
            moves2.append({mvar_opt: ["DealDamage"]})
        if entry_widget.get() == "2":
            moves2.append({mvar_opt: ["ApplyStatus"]})
        if entry_widget.get() == "3":
            moves2.append({mvar_opt: ["GainShield"]})
        finaldict["moves"] = moves2
        print(finaldict)

    if mvar_opt == "hitPrefab":
        moves2.append({mvar_opt: {"instanceID": entry_widget.get()}})
        finaldict["moves"] = moves2
        print(finaldict)

    if keyvar_opt in keywords_list:
        keywords[keyvar_opt] = entry_widget.get()
        finaldict["keywords"] = keywords
        print(finaldict)

    if mvar_opt == 'specialEffects':
        moves2.append({mvar_opt: [entry_widget.get()]})

    if mvar_opt == "statusesToApply":
        try:
            instance_id, counter = entry_widget.get().split(" ")
        except(ValueError):
            raise RuntimeError("Please enter 2 values serparated by a space")
        moves2.append({"status": {"instanceID": instance_id}, "counter": counter})
        print(finaldict)

    entry_widget.delete(0,tkinter.END)

 # Initialize the description text variable

description_text2 = None

clicked = False

pop_widget = None

cat_widget = None



#This is the remove function which works on the instance IDs
# and the moves categories. This is because those categories
# are the only ones that can have multiple values in them.

def remove():
    global clicked, pop_widget, description_text2

    if not clicked:
        pop_widget = tkinter.Entry(root)

        pop_widget.place(relx=0.5, rely=0.4, anchor="center")
        clicked = True

        if description_text2 is None:
            description_text2 = tkinter.Text(root, height=4, width=60)
            description_text2.place(x=110, y=50)

            description = "This button removes the data entry at the index you specify starting at 1\n Ex. t (tooltips) 1 or m(moves) 2"
            description_text2.insert('2.0', description)
    else:
        cat, index = pop_widget.get().split()
        if cat == 'm':
            cat = "moves"
        if cat == "t":
            cat = "tooltips"
        del finaldict[cat][int(index) - 1]
        print(finaldict)
        clicked = False
        pop_widget.destroy()

        if description_text2 is not None:
            description_text2.place_forget()
            description_text2 = None


description_text3 = None

clicked2 = False

file_widget = None

#Function that prints conents of the dictionary into
#a .json file and saves it as the user's specified name
def printfile():


    global clicked2, file_widget, description_text3

    if not clicked2:
        file_widget = tkinter.Entry(root)
        file_widget.place(relx=0.5, rely=0.4, anchor="center")
        clicked2 = True

        if description_text3 is None:
            description_text3 = tkinter.Text(root, height=4, width=60)
            description_text3.place(x=110, y=50)

            description = "Please type in the file name of the .json file \n to save the file"
            description_text3.insert('2.0', description)
    else:
        fname = file_widget.get()
        otfile = open(fname + ".json", "w")
        json.dump(finaldict, otfile)
        otfile.close()
        clicked2 = False
        file_widget.destroy()
        file_widget = None

        if description_text3 is not None:
            description_text3.place_forget()
            description_text3 = None


description_text4= None

clicked3 = False

open_widget = None

#Opens a saved .json file the user created. Do not need
#to add .json to the name it is already included
def openfile():
    global clicked3, open_widget, description_text4, finaldict

    if not clicked3:
        open_widget = tkinter.Entry(root)
        open_widget.place(relx=0.5, rely=0.4, anchor="center")
        clicked3 = True

        if description_text4 is None:
            description_text4 = tkinter.Text(root, height=4, width=60)
            description_text4.place(x=110, y=50)

            description = "Please type in the name of the file you want to open"
            description_text4.insert('2.0', description)
    else:
        fname = open_widget.get()
        otfile = open(fname + ".json", "r")
        contents = otfile.read()
        otfile.close()
        clicked3 = False
        open_widget.destroy()
        open_widget = None

        if description_text4 is not None:
            description_text4.place_forget()
            description_text4 = None


        loaded_dict = json.loads(contents)  # Load the contents of the JSON file into a new dictionary

        # Update all categories with the loaded values
               # Update tooltips category
        if "tooltips" in loaded_dict:
            tooltips_list.extend(loaded_dict["tooltips"])

        # Update moves category
        if "moves" in loaded_dict:
            moves2.extend(loaded_dict["moves"])

        # Update keywords category
        if "keywords" in loaded_dict:
            keywords.update(loaded_dict["keywords"])

        print(finaldict)



#Resets all categories and clears the descriptions and entry boxes
#Also resetting the categories makes the clicked variables equal to False
def reset_vals():

    global file_widget, pop_widget, open_widget, description_text2, description_text3, description_text4, clicked, clicked2, clicked3

    toolvar.set("data")
    vars.set("start vars")
    moves.set("moves")
    kwords.set("keywords")

    clicked = False

    clicked2 = False

    clicked3 = False

    if description_text2 is not None:
        description_text2.place_forget()
        description_text2 = None

    if pop_widget is not None:
        pop_widget.place_forget()

    if description_text3 is not None:
        description_text3.place_forget()
        description_text3 = None

    if file_widget is not None:
        file_widget.place_forget()

    if description_text4 is not None:
        description_text4.place_forget()
    description_text4 = None

    if open_widget is not None:
        open_widget.place_forget()

    if entry_widget is not None:
        entry_widget.place_forget()

    print (open_widget, file_widget)

    print(finaldict)


#Dictionary holding the values
finaldict = {"tooltips":tooltips_list, "moves": moves2, "keywords": keywords}

reset_button = tkinter.Button(root, text='Reset', command=reset_vals)
reset_button.place(relx=0.5, rely=0.7, anchor="center")

finish_button = tkinter.Button(root, text='Finish', command=printfile)
finish_button.place(relx=0.5, rely=0.5, anchor="center")


open_file = tkinter.Button(root, text='open', command=openfile)
open_file.place(relx=0.5, rely=0.6, anchor="center")


remove_button = tkinter.Button(root, text='remove', command=remove)
remove_button.place(relx=0.5, rely=0.05, anchor="center")# Submit button

# Whenever we click the submit button, our submitted
# option and data (if applicable) are printed
submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()

