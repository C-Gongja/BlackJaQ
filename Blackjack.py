from tkinter import *
import random
import time
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('BlackJaQ - Card Deck')
root.geometry("1200x800")
root.configure(background="green")

# ---------------
# Resize Cards
# ---------------
def resize_cards(card):
    # Open the image
    our_card_img = Image.open(card)

    # Resize The Image
    our_card_resize_image = our_card_img.resize((75, 109))

    # output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    # Return that card
    return our_card_image

# -----------------
# Shuffle The Cards
# -----------------
def shuffle():
    global superpos_count
    # Clear all the old cards from previous games
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    player_label_11.config(image='')
    player_label_21.config(image='')
    player_label_31.config(image='')
    player_label_41.config(image='')
    player_label_51.config(image='')

    card_button.config(state="active")
    stand_button.config(state="active")

    superpos_count = 0

    # Define Our Deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
    # 11 = Jack, 12=Queen, 13=King, 14 = Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Create our players
    global dealer, player, dealer_spot, player_spot, player_card, superpos, dealer_score, player_score, stand_bool, entangle_num, player_aces, dealer_aces, player_stands  
    dealer = []
    player = []
    superpos = []
    dealer_spot = 0
    player_spot = 0
    dealer_score = 0
    player_score = 0
    stand_bool = 0
    entangle_num = 0 
    player_aces = 0 
    dealer_aces = 0 
    player_stands = False

    # Shuffle Two Cards for player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    # Put number of remaining cards in title bar
    root.title(f'BlackJaQ - {len(deck)} Cards Left')

# ------------------------------
# Dealer's turn if player stands
# ------------------------------
def dealer_hit():
    global dealer_spot, dealer_score
    global dealer_aces 
    if dealer_spot < 5:
        try:
            # Get the player Card
            dealer_card = random.choice(deck)
            # Remove Card From Deck
            deck.remove(dealer_card)
            # Append Card To Dealer List
            dealer.append(dealer_card)

            dcard = int(dealer_card.split("_", 1)[0])
            if dcard == 14:
                dcard = 11
                dealer_aces += 1
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dcard = 10

            dealer_score += dcard
            while dealer_score > 21 and dealer_aces > 0:  
                dealer_score -= 10 
                dealer_aces -= 1 
            

            # Output Card To Screen
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            if dealer_spot == 0:
                # Resize Card
                dealer_image1 = resize_cards(f'cards/{dealer_card}.png')
                # Output Card To Screen
                dealer_label_1.config(image=dealer_image1)
                # Increment our player spot counter
                dealer_spot += 1
            elif dealer_spot == 1:
                # Resize Card
                dealer_image2 = resize_cards(f'cards/{dealer_card}.png')
                # Output Card To Screen
                dealer_label_2.config(image=dealer_image2)
                # Increment our player spot counter
                dealer_spot += 1
            elif dealer_spot == 2:
                # Resize Card
                dealer_image3 = resize_cards(f'cards/{dealer_card}.png')
                # Output Card To Screen
                dealer_label_3.config(image=dealer_image3)
                # Increment our player spot counter
                dealer_spot += 1
            elif dealer_spot == 3:
                # Resize Card
                dealer_image4 = resize_cards(f'cards/{dealer_card}.png')
                # Output Card To Screen
                dealer_label_4.config(image=dealer_image4)
                # Increment our player spot counter
                dealer_spot += 1
            elif dealer_spot == 4:
                # Resize Card
                dealer_image5 = resize_cards(f'cards/{dealer_card}.png')
                # Output Card To Screen
                dealer_label_5.config(image=dealer_image5)
                # Increment our player spot counter
                dealer_spot += 1

            # Put number of remaining cards in title bar
            root.title(f'BlackJaQ - {len(deck)} Cards Left')

        except:
            root.title(f'BlackJaQ - No Cards In Deck')
# ---------------------------
# Player demands another card
# ---------------------------
def player_hit():
    card_button.configure(text="Collapse", command=collapse)
    stand_button.configure(text="Entangle!", command=entangle)
    global superpos_count
    global player_spot
    global player_card
    if player_spot < 5:
        try:
            # Get the player Card
            create_superposition()
            player_card = f'superposition_{player_spot}.png'
            #player_card = random.choice(deck)

            # Append Card To Dealer List
            #player.append(player_card)
            # Output Card To Screen
            global player_image1, player_image2, player_image3, player_image4, player_image5

            if player_spot == 0:
                # Resize Card
                player_image1 = resize_cards(player_card)
                # Output Card To Screen
                player_label_1.config(image=player_image1)
                # Increment our player spot counter
                player_spot += 1
            elif player_spot == 1:
                # Resize Card
                player_image2 = resize_cards(player_card)
                # Output Card To Screen
                player_label_2.config(image=player_image2)
                # Increment our player spot counter
                player_spot += 1
            elif player_spot == 2:
                # Resize Card
                player_image3 = resize_cards(player_card)
                # Output Card To Screen
                player_label_3.config(image=player_image3)
                # Increment our player spot counter
                player_spot += 1
            elif player_spot == 3:
                # Resize Card
                player_image4 = resize_cards(player_card)
                # Output Card To Screen
                player_label_4.config(image=player_image4)
                # Increment our player spot counter
                player_spot += 1
            elif player_spot == 4:
                # Resize Card
                player_image5 = resize_cards(player_card)
                # Output Card To Screen
                player_label_5.config(image=player_image5)
                # Increment our player spot counter
                player_spot += 1

            # Put number of remaining cards in title bar
            root.title(f'BlackJaQ - {len(deck)} Cards Left')

        except:
            root.title(f'BlackJaQ - No Cards In Deck')
    else:
        messagebox.showinfo("Out of space!",f"No card slots remaining, automatic stand!")
        stand()
# -------------------------------------------------------------
# Collapse the superposition of the previous card (not current)
# -------------------------------------------------------------
def collapse():
    global superpos
    global player_card
    global player_spot, player_score
    global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
    global entangle_num
    global player_aces
    global stand_bool
    card_button.configure(text = "Hit Me!", command = player_hit)
    stand_button.configure(text = "Stand", command = stand)
    x = 0 ##(iterator)
    rand = random.randint(0,1) ## top or bottom we choose
    while x <= entangle_num: 
        player_card = superpos[player_spot - entangle_num + x - 2][rand] 
        player.append(player_card)
        pcard_s = player_card.split("_", 1)[0]
        pcard = int(pcard_s.split("/", 1)[1])
        if pcard == 14:
            pcard = 11
            player_aces += 1 
        elif pcard == 11 or pcard == 12 or pcard == 13:
            pcard = 10
        player_score += pcard
        while player_score > 21 and player_aces > 0:
            player_score -= 10 
            player_aces -= 1 
        if player_spot - entangle_num + x == 2: 
            player_image_1 = resize_cards(player_card)
            player_label_1.config(image=player_image_1)
            player_label_11.config(image='')
        elif player_spot - entangle_num + x == 3:
            player_image_2 = resize_cards(player_card)
            player_label_2.config(image=player_image_2)
            player_label_21.config(image='')
        elif player_spot - entangle_num + x == 4:
            player_image_3 = resize_cards(player_card)
            player_label_3.config(image=player_image_3)
            player_label_31.config(image='')
        elif player_spot - entangle_num + x == 5:
            player_image_4 = resize_cards(player_card)
            player_label_4.config(image=player_image_4)
            player_label_41.config(image='')
        elif player_spot - entangle_num + x == 6:
            player_image_5 = resize_cards(player_card)
            player_label_5.config(image=player_image_5)
            player_label_51.config(image='')
        x += 1 
    
    entangle_num = 0 
    
    if player_score > 21 and player_stands == False:
        messagebox.showinfo("Player loses!",f"Collapsed cards total over 21, automatic stand!")
        stand_bool = 1
        stand()





# ------------------------------------------------------------
# Entangle current two cards according to their superpositions
# ------------------------------------------------------------
def entangle():
    card_button.configure(text="Hit Me!", command=player_hit)
    stand_button.configure(text = "Stand", command = stand)
    
   

    global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
    global player_image_11, player_image_21, player_image_31, player_image_41, player_image_51
    global superpos, player_spot, entangle_num 

    entangle_num += 1 
    
    card1 = superpos[player_spot - 2][0]
    card11 = superpos[player_spot - 2][1]
    card2 = superpos[player_spot - 1][0]
    card21 = superpos[player_spot - 1][1]

    if player_spot == 2:
        player_image_1 = resize_cards(card1)
        player_label_1.config(image=player_image_1)
        player_image_11 = resize_cards(card11)
        player_label_11.config(image=player_image_11)
        player_image_2 = resize_cards(card2)
        player_label_2.config(image=player_image_2)
        player_image_21 = resize_cards(card21)
        player_label_21.config(image=player_image_21)
    elif player_spot == 3:
        player_image_2 = resize_cards(card1)
        player_label_2.config(image=player_image_2)
        player_image_21 = resize_cards(card11)
        player_label_21.config(image=player_image_21)
        player_image_3 = resize_cards(card2)
        player_label_3.config(image=player_image_3)
        player_image_31 = resize_cards(card21)
        player_label_31.config(image=player_image_31)
    elif player_spot == 4:
        player_image_3 = resize_cards(card1)
        player_label_3.config(image=player_image_3)
        player_image_31 = resize_cards(card11)
        player_label_31.config(image=player_image_31)
        player_image_4 = resize_cards(card2)
        player_label_4.config(image=player_image_4)
        player_image_41 = resize_cards(card21)
        player_label_41.config(image=player_image_41)
    elif player_spot == 5:
        player_image_4 = resize_cards(card1)
        player_label_4.config(image=player_image_4)
        player_image_41 = resize_cards(card11)
        player_label_41.config(image=player_image_41)
        player_image_5 = resize_cards(card2)
        player_label_5.config(image=player_image_5)
        player_image_51 = resize_cards(card21)
        player_label_51.config(image=player_image_51)



# -------------------------------------------------------------------------
# Player stands. All superpositions are collapsed, turn is handed to dealer
# -------------------------------------------------------------------------
def stand():
    card_button.configure(text="Collapse", command=collapse)
    stand_button.configure(text = "Entangle!", command = entangle)

    global player_score, dealer_score, player_spot, dealer_spot, stand_bool, player_stands
    player_stands = True
    if (stand_bool == 0):
        player_spot += 1
        collapse()
        stand_bool = 1

    # time.sleep(0.25) ## This is an attempt to make the image show before the message, but it doesn't work
    # When there's something nonsense here the message doesn't show but the cards collapse, but when there's 
    #anything that run shere the message shows before cards collapse??? I don't know why...
    
    card_button.config(state="disabled")
    stand_button.config(state="disabled")
    if player_score > 21:
        # Player Busts
        
        messagebox.showinfo("Dealer Wins!!", f"Dealer Wins! Player: {player_score}")
    elif dealer_score >= 17:
        if dealer_score > 21:
            # bust
            
            messagebox.showinfo("Player Wins!!", f"Player Wins!  Dealer: {dealer_score}  Player: {player_score}")
        elif dealer_score == player_score:
            # tie
            
            messagebox.showinfo("Tie!!", f"It's a Tie!!  Dealer: {dealer_score}  Player: {player_score}")
        elif dealer_score > player_score:
            # dealer wins
            
            messagebox.showinfo("Dealer Wins!!", f"Dealer Wins!  Dealer: {dealer_score}  Player: {player_score}")
        else:
            # player wins
            
            messagebox.showinfo("Player Wins!!", f"Player Wins!  Dealer: {dealer_score}  Player: {player_score}")
        print("message has been shown")
    else:
        if dealer_spot < 5: 
            # Add card to dealer
            dealer_hit()
        # Recalculate
        stand()
        

def create_superposition():
    global superpos_count
    global superpos_img
    global superpos
    global player_spot
    superpos1 = random.choice(deck) 
            # Remove Card From Deck
    deck.remove(superpos1) 
            
    superpos2 = random.choice(deck) 
    # Remove Card From Deck
    deck.remove(superpos2)
    
    superpos.append([f'cards/{superpos1}.png', f'cards/{superpos2}.png']) 
    
    imgs = [Image.open(i) for i in superpos[player_spot]]

    #Get image dimensions
    w, h = imgs[0].size

    #Define cropping bounds
    left = 0
    right = w
    upper1 = 0
    lower1 = h / 2
    upper2 = h / 2
    lower2 = h

    #Crop both images
    imgs[0] = imgs[0].crop([left, upper1, right, lower1])
    imgs[1] = imgs[1].crop([left, upper2, right, lower2])

    #Make new image
    img_merge = Image.new(imgs[0].mode, (w, h))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))
        y += img.height
    img_merge.save(f'superposition_{superpos_count}.png')
    superpos_count += 1


# --------------
# Deal Out Cards
# --------------
def deal_cards():
    try:
        # Get the dealer Card
        card = random.choice(deck)
        # Remove Card From Deck
        deck.remove(card)
        # Append Card To Dealer List
        dealer.append(card)
        # Output Card To Screen
        global dealer_image
        dealer_image = resize_cards(f'cards/{card}.png')
        dealer_label.config(image=dealer_image)
        # dealer_label.config(text=card)

        # Get the player Card
        card = random.choice(deck)
        # Remove Card From Deck
        deck.remove(card)
        # Append Card To Dealer List
        player.append(card)
        # Output Card To Screen
        global player_image
        player_image = resize_cards(f'cards/{card}.png')
        player_label.config(image=player_image)
        # player_label.config(text=card)

        # Put number of remaining cards in title bar
        root.title(f'BlackJaQ - {len(deck)} Cards Left')

    except:
        root.title(f'BlackJaQ - No Cards In Deck')

# --------------------------------------
# --------------- GUI ------------------
# --------------------------------------
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)


player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

#Entanglement Row
player_label_11 = Label(player_frame, text='')
player_label_11.grid(row=2, column=0, pady=20, padx=20)

player_label_21 = Label(player_frame, text='')
player_label_21.grid(row=2, column=1, pady=20, padx=20)


player_label_31 = Label(player_frame, text='')
player_label_31.grid(row=2, column=2, pady=20, padx=20)

player_label_41 = Label(player_frame, text='')
player_label_41.grid(row=2, column=3, pady=20, padx=20)

player_label_51 = Label(player_frame, text='')
player_label_51.grid(row=2, column=4, pady=20, padx=20)


# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Collapse", font=("Helvetica", 14), command=collapse)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text = "Entangle!", font=("Helvetica", 14), command = entangle)
stand_button.grid(row=0, column=2)

# Shuffle Deck On Start
shuffle()

root.mainloop()
