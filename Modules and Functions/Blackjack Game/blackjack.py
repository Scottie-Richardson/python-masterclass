import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

main_window = tkinter.Tk()


def load_cards(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    extension = 'ppm'
    # tkinter versions before 8.6 do not support png file extensions, so if you wish to use png
    #   files instead, the below code may be nessicary. I however will be using ppm files.
    # if tkinter.TkVersion >= 8.6:
    #     extension = 'png'
    # else:
    #     extension = 'ppm'

    # For each suit, retrieve the image for the cards
    for suit in suits:
        # Load the numbered cards (1-10)
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # Load the face card
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # Pop the next card off the top of the deck
    next_card = deck.pop()

    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # Return the card's face value
    return next_card


def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)


# Set up the screen and frames for the dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_cards(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
print(deck)
random.shuffle(deck)
print(deck)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

main_window.mainloop()
