# Program : Make 'N Shake (Culminating Project)
# Names : Maheer Morshed, Divisha Chandralingam, Aamina Mohammed Farook
# Date : June 20 2022
# Description : A game where you catch ingredients to make milkshake orders

# Import libraries
import math
import tkinter
import random
import pygame
from PIL import ImageTk, Image

# Login / Register / Guest Functions---------------------------------------------------------------------------------------------------

def make_main_screen ():
    # Globalize variables
    global WIN_WIDTH 
    global WIN_HEIGHT
    global BUTTON_FONT 
    global window
    
    #Creates window
    window = tkinter.Tk ()

    # Grabs full screen dimensions depending on user screen interface
    WIN_WIDTH = window.winfo_screenwidth ()
    WIN_HEIGHT = window.winfo_screenheight ()
    
    BUTTON_FONT = ("Times", 17)

    window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # Opens 'store_background' image and resizes it
    background = Image.open ("images/store_background.png")
    background = background.resize ((WIN_WIDTH, WIN_HEIGHT))

    # Converts image into tkinter-file so tkinter functions can use it
    background = ImageTk.PhotoImage (background)

    main = tkinter.Canvas (window, bg="pink", 
                            width = WIN_WIDTH, 
                            height = WIN_HEIGHT)
    
    # Loads 'store_background' image into main canvas
    main.create_image (0, 0, anchor="nw", image=background)

    # Creates frames for all texts and buttons

    title_frame = tkinter.Frame (main, bd=20, relief=tkinter.SUNKEN)
    title_frame.place (x = (WIN_WIDTH // 2) - 50, y = 25)

    login_frame = tkinter.Frame (main)
    login_frame.place (x = (WIN_WIDTH // 2) , y = (WIN_HEIGHT // 1.75))

    signup_frame = tkinter.Frame (main)
    signup_frame.place (x = (WIN_WIDTH // 2) - 10, y = (WIN_HEIGHT // 1.55))

    guest_frame = tkinter.Frame(main)
    guest_frame.place (x = (WIN_WIDTH // 2) - 35, y = (WIN_HEIGHT // 1.4))

    # Creates title on top of display window, and loads to monitor
    title = tkinter.Label (title_frame, 
                            text = "Make n Shake",
                            font = ("Times", 20))
    title.pack ()

    # Creates login button, loads to monitor
    login = tkinter.Button (login_frame, 
                            text = "Login",
                            font = BUTTON_FONT, 
                            bg = "red",
                            command = login_event)
    login.pack ()

    # Creates register button, loads to monitor
    signup = tkinter.Button (signup_frame, 
                            text = "Sign Up",
                            font = BUTTON_FONT, 
                            bg = "brown",
                            command = signup_event)
    signup.pack ()

    # Creates play guest button, loads to monitor
    play_as_guest = tkinter.Button (guest_frame, 
                                    text = "Play As Guest",
                                    font = BUTTON_FONT, 
                                    bg = "white", 
                                    command = guest_login)
    play_as_guest.pack ()

    # Loads all texts and buttons to monitor
    main.pack ()
   
    window.mainloop ()

def login_event ():
    #Globalizing variables
    global login_window
    global ID_entry
    global pass_entry
    global error_label

    window.destroy ()

    #Creates new window for user to log in
    login_window = tkinter.Tk ()
    login_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    login_canvas = tkinter.Canvas (login_window, 
                                    bg="pink", 
                                    width=WIN_WIDTH, 
                                    height=WIN_HEIGHT)

    # Creates frames to place widgets in organized manner
    ID_entry_frame = tkinter.Frame (login_canvas)
    ID_entry_frame.place (x = (WIN_WIDTH / 2.5), y = 200)
   
    pass_entry_frame = tkinter.Frame (login_canvas)
    pass_entry_frame.place (x = (WIN_WIDTH / 2.5), y = 300)
   
    enter_frame = tkinter.Frame (login_canvas)
    enter_frame.place (x = (WIN_WIDTH / 2.05), y = (WIN_HEIGHT / 2.1))
   
    return_frame = tkinter.Frame (login_canvas)
    return_frame.place (x = (WIN_WIDTH / 12.3), y= (WIN_HEIGHT / 1.23))

    error_frame = tkinter.Frame (login_canvas)
    error_frame.place (x = (WIN_WIDTH / 2.2), y = (WIN_HEIGHT / 2.3))

    #Creates title for ID entry box and actual entry and loads to monitor
    ID_entry_title = tkinter.Label (ID_entry_frame, 
                                    text = "Enter User ID", 
                                    fg = "red", 
                                    font = ("Times", 15))
    ID_entry = tkinter.Entry (ID_entry_frame, 
                              font = ("Helvetica", 20))
    ID_entry_title.pack ()
    ID_entry.pack ()

    #Creates title for password entry and actual entry and loads to monitor
    pass_entry_title = tkinter.Label (pass_entry_frame, 
                                      text = "Enter Password", 
                                      fg = "red", 
                                      font = ("Times", 15))
    pass_entry = tkinter.Entry (pass_entry_frame, 
                                font = ("Helvetica", 20))
    pass_entry_title.pack ()
    pass_entry.pack ()

    # Creates label to tell user if an error occurs
    error_label = tkinter.Label (error_frame, 
                                bg = "pink", 
                                fg = "red")
    error_label.pack ()

    # Creates enter button 
    enter_button = tkinter.Button (enter_frame, 
                                  text = "Login", 
                                  bg = "green", 
                                  fg = "black", 
                                  font = BUTTON_FONT, 
                                  command = sign_in)
    enter_button.pack ()
    
    # Creates button for if the user wishes to go back to main scren
    return_button = tkinter.Button (return_frame, 
                                    text = "Go Back", 
                                    bg = "red", 
                                    fg = "black", 
                                    font = BUTTON_FONT, 
                                    command = login_exit)
    return_button.pack ()

    # Loads all combined widgets to monitor
    login_canvas.pack ()

    login_window.mainloop ()

def sign_in ():
    # Globalize variables
    global log_in_Id
    global guest_mode
    global score

    found = False
    
    # Collects user input from entry boxes
    Id = ID_entry.get ()
    password = pass_entry.get ()
    
    database = open ("data.txt", 'r')

    line_read = database.readline ()

    # If correct login info found in database file,
    # guest mode gets disabled and global 'score' variable
    # is accessed (3rd element on a row of database file)
    while (line_read != ""):
        line_read = line_read.split ()
        if (Id == line_read[0]):
            if (password == line_read[1]):
                print ("success!")
                log_in_Id = Id
                found = True
                score = int (line_read[2])
                guest_mode = False
                pre_game (login_window)
            line_read = ""
        else:      
            line_read = database.readline ()

    database.close ()

    # If correct info not found, error message thrown at user
    if (found == False):
        error_label.configure (text = "Invalid ID/password")

def login_exit ():
    # Destroys login window, and goes back to main screen
    login_window.destroy ()
    make_main_screen ()

def signup_event ():
    #Globalize variables
    global signup_window
    global ID_create_entry
    global pass_create_entry
    global con_pass_create_entry
    global error_msg_box

    
    window.destroy ()

    # Create register window in full screen
    signup_window = tkinter.Tk ()
    signup_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    signup_canvas = tkinter.Canvas (signup_window, 
                                    bg = "pink", 
                                    width = WIN_WIDTH, 
                                    height = WIN_HEIGHT)
       
    # Creating frames to better organize visual widgets
    ID_create_frame = tkinter.Frame (signup_canvas)
    ID_create_frame.place (x = (WIN_WIDTH // 2.5), y = 100)

    pass_create_frame = tkinter.Frame (signup_canvas)
    pass_create_frame.place (x = (WIN_WIDTH // 2.5), y = 200)

    con_pass_create_frame = tkinter.Frame (signup_canvas)
    con_pass_create_frame.place (x = (WIN_WIDTH // 2.5), y = 300)

    return_frame = tkinter.Frame (signup_canvas)
    return_frame.place (x= (WIN_WIDTH // 14), y=700)

    register_frame = tkinter.Frame (signup_canvas)
    register_frame.place (x = (WIN_WIDTH // 2.15), y = (WIN_HEIGHT / 1.75))

    error_frame = tkinter.Frame (signup_canvas)
    error_frame.place (x = (WIN_WIDTH // 2.1), y = (WIN_HEIGHT // 2.2))

    ID_create_entry_title = tkinter.Label (ID_create_frame, 
                                            text = "Create Your ID", 
                                            fg = "red", 
                                            font = ("Times", 15))
    ID_create_entry = tkinter.Entry (ID_create_frame, 
                                    font = ("Helvetica", 20))
    ID_create_entry_title.pack ()
    ID_create_entry.pack ()

    pass_create_entry_title = tkinter.Label (pass_create_frame, 
                                            text = "Create Password", 
                                            fg = "red", 
                                            font = ("Times", 15))
    pass_create_entry = tkinter.Entry (pass_create_frame, 
                                        font = ("Helvetica", 20))
    pass_create_entry_title.pack ()
    pass_create_entry.pack ()

    con_pass_create_entry_title = tkinter.Label (con_pass_create_frame, 
                                                text = "Confirm password", 
                                                fg = "red", 
                                                font = ("Times", 15))
    con_pass_create_entry = tkinter.Entry (con_pass_create_frame, 
                                           font = ("Helvetica", 20))
    con_pass_create_entry_title.pack ()
    con_pass_create_entry.pack ()

    error_msg_box = tkinter.Label (error_frame, 
                                  font = ("Helvetica", 10), 
                                  bg = "pink")
    error_msg_box.pack ()


    return_button = tkinter.Button (return_frame, 
                                   bg = "red", 
                                   text = "Go Back",
                                   font = ("Helvetica", 20), 
                                   command = signup_exit)
    return_button.pack ()

    register_button = tkinter.Button (register_frame, 
                                      bg = "green", 
                                      text = "Register", 
                                      font = ("Helvetica", 20), 
                                      command = register)
    register_button.pack ()

    signup_canvas.pack ()

def register ():
    # Globalize variables
    global log_in_Id
    global score 
    global guest_mode 

    # Holds potential error message
    error_msg = ""

    # Grabs user's entry inputs
    Id = ID_create_entry.get ()
    password = pass_create_entry.get ()
    con_pass = con_pass_create_entry.get ()
    
    op_file = open ("data.txt", 'r')

    #Error checking

    if (len (Id) == 0 or len (password) == 0 or len (con_pass) == 0):
        error_msg = "A field cannot be empty."
    elif (len (Id) != 6):
        error_msg = "User ID is not exactly 6 characters. Enter a ID with only 6-characters. "
    elif (Id.isdigit () == False):
        error_msg = "User ID must only be made of integers."
    elif (password != con_pass):
        error_msg = "These 2 passwords dont match."
    else:
        line_read = op_file.readline ()
        
        while (line_read != ""):
            line_read = line_read.split ()

            if (Id in line_read[0]):
                error_msg = "User ID already exists."
                line_read = ""
            else:
                line_read = op_file.readline ()
        
    op_file.close ()

    error_msg_box.configure (text = error_msg, 
                            fg = "red")

    # Registers user info to database file if successful
    # Opens pre_game window
    if (error_msg == ""):
        op_file = open ("data.txt", 'a')

        data_line = f"{Id} {password} {0}\n"
        op_file.write (data_line)

        op_file.close ()

        log_in_Id = Id
        guest_mode = False
        score = 0

        pre_game (signup_window)

def signup_exit ():
    # Closes out of register window and returns to main screen
    signup_window.destroy()
    make_main_screen()

def guest_login ():
    #Globalize variables
    global log_in_Id
    global guest_mode
    global score
    
    log_in_Id = "Guest"
    
    guest_mode = True

    score = 0

    # Closes main window and goes to pre_game window
    pre_game (window)

# Before the actual game--------------------------------------------------------------------------------------------------------------

def pre_game (window):    
    #Globalize variables
    global pre_game_window
    
    score_text = f"Score:{score}"

    log_msg = f"Logged as: {log_in_Id}"

    window.destroy ()
    
    # Creates pre_game window
    pre_game_window = tkinter.Tk ()
    pre_game_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # Loads question_button image into program
    # Resizes the image
    # Converts the image into a tkinter-file to be used by tkinter functions
    icon = Image.open ("images/question_button.png")
    icon = icon.resize ((100, 100))
    icon = ImageTk.PhotoImage (icon)

    pre_game_canvas = tkinter.Canvas (pre_game_window, 
                                      bg = "pink", 
                                      width = WIN_WIDTH, 
                                      height = WIN_HEIGHT)
    
    # Creates frames for better organization of visual widgets
    logged_as_frame = tkinter.Frame (pre_game_canvas)
    logged_as_frame.place (x = WIN_WIDTH - 200, y = 25)

    score_frame = tkinter.Frame (pre_game_canvas)
    score_frame.place (x = (WIN_WIDTH // 2) - 45, y= 200)
    
    play_button_frame = tkinter.Frame (pre_game_canvas)
    play_button_frame.place (x = (WIN_WIDTH // 2) - 175, y = 625)
    
    instructions_frame = tkinter.Frame (pre_game_canvas)
    instructions_frame.place (x = 100, y = (WIN_HEIGHT - 375))

    log_out_frame = tkinter.Frame (pre_game_canvas)
    log_out_frame.place (x = WIN_WIDTH - 200, y = 650)
    
    # Creating labels and buttons
    logged_as_label = tkinter.Label (logged_as_frame, 
                                    text = log_msg, 
                                    bg = "pink", 
                                    fg = "black")
    logged_as_label.pack ()
    
    score_label = tkinter.Label (score_frame, 
                                text = score_text, 
                                fg = "brown", 
                                bg = "pink",
                                font = ("Times", 32))
    score_label.pack ()

    play_button = tkinter.Button (play_button_frame, 
                                  text = "Click To Play", 
                                  bg = "green", 
                                  fg = "black",
                                  font = ("Times", 20), 
                                  width = 25, 
                                  command = play)
    play_button.pack ()

    instructions_button = tkinter.Button (instructions_frame, 
                                          image = icon, 
                                          bg = "pink", 
                                          borderwidth = 0,
                                          command = instructions)
    instructions_button.pack ()

    log_out_button = tkinter.Button (log_out_frame, 
                                     text = "Log Out", 
                                     bg = "lime", 
                                     fg = "black", 
                                     font = ("Times", 20), 
                                     command = log_out)

    log_out_button.pack ()

    pre_game_canvas.pack ()

    pre_game_window.mainloop ()

def instructions ():
    global instructions_window
    
    pre_game_window.destroy ()

    # Creates full screen window for instructions
    instructions_window = tkinter.Tk ()
    instructions_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    instructions_canvas = tkinter.Canvas (instructions_window, 
                                          width = WIN_WIDTH, 
                                          height = WIN_HEIGHT, 
                                          bg = "pink")

    # Creates frames
    instructions_title_frame = tkinter.Frame (instructions_canvas)
    instructions_title_frame.place (x = 85, y = 25)
    
    instructions_frame = tkinter.Frame (instructions_canvas)
    instructions_frame.place (x = 85, y = 150)
    
    return_frame = tkinter.Frame (instructions_canvas)
    return_frame.place (x = 45, y = 675)

    # Creates widgets contained in those frames
    instructions_title = tkinter.Label (instructions_title_frame, 
                                        text = "How To Play", 
                                        font = ("Times", 25), 
                                        bg = "pink")
    instructions_title.pack ()
    
    instructions_text = ["Congratulations!\n",
                        "You have successfully opened your own milkshake shop!\n",
                        "Now it is time to serve some customers and make 'em happy!\n\n"
                        "You can create a milkshake order at any time\n",
                        "When you're ready, click the 'Start Order' to begin\n",
                        "Use the right/left arrow keys to move the glass\n",
                        "Catch as many ingredients as you can to complete the order\n",
                        "Once all the ingredients have fallen, your product will be given to the customer\n",
                        "You get 100 points for every ingredient you successfully catch\n",
                        "\n Good luck and happy milkshake making! :)"]

    # Iterates through entire list, and builds the big block of instructions
    inst = ""
    for instruction in instructions_text:
        inst = inst + instruction

    # Block of instructions made from loop inplemented into a blue label
    instructions_label = tkinter.Label (instructions_frame, 
                                        bg = "blue", 
                                        text = inst, 
                                        font = ("Helvetica", 20))
    instructions_label.pack ()
    
    return_button = tkinter.Button (return_frame, 
                                    text = "Go Back", 
                                    font = ("Times", 20), 
                                    bg = "red",
                                    command = return_from_instructions)
    return_button.pack ()

    instructions_canvas.pack ()

    instructions_window.mainloop ()

def return_from_instructions ():
    pre_game (instructions_window)

def log_out ():
    pre_game_window.destroy ()
    make_main_screen ()

# In the actual game-----------------------------------------------------------------------------------------------------------------

# Detects if the ingredients touch cup using distance formula
def collision (x1, x2, y1, y2):
    global distance 

    x_part = (x2 - x1) ** 2
    y_part = (y2 - y1) ** 2

    distance = math.sqrt (x_part + y_part)

    if (distance < 50):
        return True

def customer_orders ():
    #Globalize variables
    global order
    
    order = []
    
    random_index = random.randrange(0,6)
    size = random.randrange(0,3)
    
    if size == 0:
        order.append ("Small - $4.99")
    elif size == 1:
        order.append ("Medium - $5.99")
    elif size == 2:
        order.append ("Large - $6.99")
    
    flavours = ["Chocolate Milkshake", 
                "Vanilla Milkshake", 
                "Mint Chocolate Milkshake",
                "Strawberry Milkshake", 
                "Matcha Milkshake", 
                "Caramel Milkshake"]

    ingredients = [
    ["chocolate ice cream", "chocolate syrup", "milk"], 
    ["vanila ice cream", "chocolate syrup", "milk"],
    ["mint chocolate ice cream", "chocolate syrup", "milk"],
    ["strawberry ice cream", "strawberry slices", "strawberry syrup", "milk"],
    ["Matcha Green Tea ice cream", "Match powder", "milk"], 
    ["vanilla ice cream", "caramel syrup", "milk"]
    ]

    ingredient_images = [
        ["chocolate_ice_cream.png",
        "chocolate_syrup.png",
        "milk.png"],
        
        ["vanilla_ice_cream.png",
        "chocolate_syrup.png",
        "milk.png"],

        ["mint_chocolate_ice_cream.png",
        "chocolate_syrup.png",
        "milk.png"],

        ["strawberry_ice_cream.png",
        "strawberry_slices.png",
        "strawberry_syrup.png",
        "milk.png"],

        ["matcha_ice_cream.png",
        "matcha_powder.png",
        "milk.png"],

        ["vanilla_ice_cream.png",
        "caramel_syrup.png",
        "milk.png"]
    ]
    
    flavour_index = flavours[random_index]
    ingredients_index = ingredients[random_index]
    image_ingredients_index = ingredient_images[random_index]
    
    order.append ("Order: " + flavour_index)
    order.append (ingredients_index)

    return image_ingredients_index

def play ():
    global in_game_window
    global store_canvas
    
    pre_game_window.destroy ()

    # Creates window for begininning the actual game

    in_game_window = tkinter.Tk ()
    in_game_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    store_canvas = tkinter.Canvas (in_game_window, 
                                  width = WIN_WIDTH, 
                                  height = WIN_HEIGHT, 
                                  bg = "magenta")

    # Frames creations
    start_order_frame = tkinter.Frame (store_canvas)
    start_order_frame.place (x = 10, y = 10)

    end_shift_frame = tkinter.Frame (store_canvas)
    end_shift_frame.place (x = 10, y = 80)

    exit_sign_frame = tkinter.Frame (store_canvas)
    exit_sign_frame.place (x = WIN_WIDTH // 1.1 , y = 45)

    exit_sign = tkinter.Label (exit_sign_frame, 
                               text = "Exit", 
                               fg = "red", 
                               bg = "white", 
                               font = ("Helvetica", 30))
    exit_sign.pack ()

    # Creating props
    window = store_canvas.create_rectangle ((WIN_WIDTH // 10), (WIN_HEIGHT // 10),
                                            (WIN_WIDTH // 2), (WIN_WIDTH // 5), 
                                            fill = "cyan")

    door = store_canvas.create_rectangle ((WIN_WIDTH // 1.2), 100, 
                                           WIN_WIDTH, WIN_HEIGHT,
                                           fill = "brown")

    counter = store_canvas.create_rectangle (0, (WIN_HEIGHT // 1.5),
                                             WIN_WIDTH, WIN_HEIGHT,
                                             fill = "gray")
    
    # Creating buttons
    start_order_button = tkinter.Button (start_order_frame, 
                                        bg = "blue", 
                                        text = "Start Order", 
                                        font = BUTTON_FONT, 
                                        fg = "black", 
                                        command = milkshake_manufacture)
    start_order_button.pack ()

    end_shift_button = tkinter.Button (end_shift_frame, 
                                       bg = "red", 
                                       text = "End Shift", 
                                       font = BUTTON_FONT, 
                                       fg = "black", 
                                       command = finish_game)
    end_shift_button.pack ()
    
    store_canvas.pack ()

    in_game_window.mainloop ()

# Moves the player around when they begin making milkshakes
def player_move (x, y):
    game_window.blit (cup, (x, y))

def milkshake_manufacture ():
    # Globalize variables
    global game_window
    global cup
    global score
    
    x = WIN_WIDTH - 100
    y = WIN_HEIGHT - 100
    cup_position_x = x // 2
    cup_position_y = y - 250
    change_x = 0
    ingredient_y = 0
    left_border = 0
    right_border = int(round(x // 10) * 8.5)
    items_caught = 0

    # Gets random order
    images = customer_orders ()

    # Initiates pygame
    pygame.init ()

    # Loads kitchen background image from computer and resizes it
    background = pygame.image.load ('images/kitchen_background.png')
    background = pygame.transform.scale (background, (x, y))

    # Loads cup from image, and rescales it
    cup = pygame.image.load ('images/milkshake_cup.png')
    cup = pygame.transform.scale (cup, (175, 175))

    # Creates font for score texts
    font = pygame.font.Font ('freesansbold.ttf', 32)

    # Creates full dimension pygame window
    game_window = pygame.display.set_mode ((x, y))

    
    for items in images:
        # Loads image of an ingredient
        ingredient = pygame.image.load (f'images/{items}')
        ingredient = pygame.transform.scale (ingredient, (175, 175))
        
        # Randomly generates horizontal position of ingredient
        ingredient_x = random.randrange (left_border, right_border)


        while (ingredient_y < 800):
            # Creates score text
            score_text = font.render (f"Caught: {items_caught}/{len(images)}",
                                      True, (255, 255, 255))
            
            game_window.blit (background, (0,0))
            
            game_window.blit (ingredient, (ingredient_x, ingredient_y))
            
            game_window.blit (score_text, (20, 20))

            # Sets events for if user presses key dow/up
            for event in pygame.event.get ():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change_x = 5
                    elif event.key == pygame.K_LEFT:
                        change_x = -5
                if event.type == pygame.KEYUP:
                    change_x = 0

            cup_position_x += change_x
            ingredient_y += 1.5

            # If ingredient collides with cup, it skips to next ingredient, and updates
            # the score
            if (collision (cup_position_x, ingredient_x, ingredient_y, cup_position_y)):
                score += 100
                items_caught += 1
                ingredient_y = 1000

            # Boundaries to ensure cup doesnt go off screen
            if (cup_position_x < left_border):
                cup_position_x = left_border
            elif (cup_position_x > right_border):
                cup_position_x = right_border

            game_window.blit (cup, (cup_position_x, cup_position_y))

            pygame.display.update ()

        ingredient_y = 0

        # If all ingredients have falleen, quit the pygame window and create a receipt
        if (items == images[len(images)-1]):
            pygame.display.quit ()
            make_receipt ()

def make_receipt ():
    # Initializing variables
    size_type = order[0]
    flavor_type = order[1]
    ingredients = order[2]
    ingredient_text = ""

    receipt_window = tkinter.Tk ()
    receipt_window.geometry (f"{WIN_WIDTH}x{WIN_HEIGHT}")

    receipt_canvas = tkinter.Canvas (receipt_window, 
                                     bg = "gray", 
                                     width = WIN_WIDTH, 
                                     height = WIN_HEIGHT)
    
    # Creates 3 different areas where different info shows on receipt
    flavor_frame = tkinter.Frame (receipt_canvas)
    flavor_frame.place (x = (WIN_WIDTH // 2) - 100 , y = 150)
    
    type_frame = tkinter.Frame (receipt_canvas)
    type_frame.place (x = (WIN_WIDTH // 2) - 100, y = 300)

    ingredient_frame = tkinter.Frame (receipt_canvas)
    ingredient_frame.place (x = (WIN_WIDTH // 2) - 100, y = 450)

    flavor_label = tkinter.Label (flavor_frame, 
                                  text = flavor_type, 
                                  fg = "black", 
                                  bg = "gray", 
                                  font = ("Helvetica", 27))
    flavor_label.pack ()

    type_label = tkinter.Label (type_frame, 
                                text = size_type, 
                                fg = "black", 
                                bg = "gray", 
                                font = ("Helvetica", 23))
    type_label.pack ()

    # Creates a vertical box of ingredients used in order just made
    for item in ingredients:
        ingredient_text += f"{item}\n"

    ingredient_label = tkinter.Label (ingredient_frame, 
                                      text = ingredient_text, 
                                      fg = "black", 
                                      bg = "gray", 
                                      font = ("Helvetica", 17))
    
    # Moves ingredient label to the left
    ingredient_label.pack (side = tkinter.LEFT)

    receipt_canvas.pack ()

    receipt_window.mainloop ()

def write_score ():
    #Initializing variables
    new_line = ""
    datatext = ""

    datafile = open("data.txt", 'r')

    dataread = datafile.readline()

    # Reads through database file
    # The logged in user will have their scores changed to whatever they earned
    while (dataread != ""):
        data_split = dataread.split()

        if (data_split[0] == log_in_Id):
            data_split[2] = score

            new_line = f"{data_split[0]} {data_split[1]} {data_split[2]}\n"

            datatext += new_line
            
            dataread = ""
        else:
            datatext += dataread
        
        dataread = datafile.readline()
    
    datafile.close()

    # Overwrite the entire file with new info (combining old info plus new info)

    datafile = open("data.txt", 'w')

    datafile.write(datatext)

    datafile.close()

def finish_game():
    if (not guest_mode):
        write_score()

    pre_game(in_game_window)

# Starting the entire program
make_main_screen()

