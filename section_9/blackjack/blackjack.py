import random

try:
  import tkinter
except ImportError:
  import TkInter as tkinter

mainWindow = tkinter.Tk()


def loadImages(cardImages):
  suits = ['heart', 'club', 'diamond', 'spade']
  faceCards = ['jack', 'queen', 'king']

  if tkinter.TkVersion >= 8.6:
    extension = 'png'
  else:
    extension = 'ppm'
  
  # for each suit, retrieve the image for the cards
  for suit in suits:
    # first the number cards 1 to 10
    for card in range(1, 11):
      name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
      image = tkinter.PhotoImage(file=name)
      cardImages.append((card, image,))
    
    # next the face cards
    for card in faceCards:
      name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
      image = tkinter.PhotoImage(file=name)
      cardImages.append((10, image,))


def dealCard(frame):
  # pop the next card off the top of the deck
  nextCard = deck.pop()
  # add the image to a Label and display the label
  tkinter.Label(frame, image=nextCard[1], relief='raised').pack(side='left')
  # return the card's face value
  return nextCard


def dealDealer():
  dealCard(dealerCardFrame)


def dealPlayer():
  dealCard(playerCardFrame)


# Set up the screen and frames for the dealer and player
mainWindow.title('Black Jack')
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background='green', fg='white').grid(row=1, column=0)
# embedded frame to hold the card images
dealerCardFrame = tkinter.Frame(cardFrame, background='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background='green', fg='white').grid(row=3, column=0)
# embedded frame to hold the card images
playerCardFrame = tkinter.Frame(cardFrame, background='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tkinter.Button(buttonFrame, text='Dealer', command=dealDealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text='Player', command=dealPlayer)
playerButton.grid(row=0, column=1)

# load cards
cards = []
loadImages(cards)

# create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# create the list to store the dealer's and player's hands
dealerHand = []
playerHand = []

mainWindow.mainloop()
