# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character('Narrator', color="#d74a25")
define j = Character('Josue', color="#c8ffc8", image="josue", who_font="gui/Apple-Chancery.ttf", what_font="gui/Apple-Chancery.ttf")
define ja = Character('Jaime', color="#17c3ca", image="jaime")
define i = Character('Ivy', color="#fd536b", image="ivy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg neighborhood

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    play music "audio/MantraStudio.mp3"

    n "There once was a place,"
    n "Between somewhere"
    n "and somewhere else."
    n "Quite frankly it was in the middle of nowhere."
    n "But in this place, was a crazy crew of misfortunate misfits. \n \nTeenagers, who wanted a little excitement, and found it."
    n "This is the story of.."
    n "The story of how they.."

    show josue
    #image josue = "josue.png"
    #image side = "josue.png"

    j "WAIT, WHAT?!? Who are you? Who was that talking to you just now?"

    hide josue

    n "Oh sorry, that was me. I was just.."

    show josue at right

    j "Don't tell my story.."
    j "That's my job."

    hide josue

    n "Right.."
    n "I was just.."

    show ivy at right with easeinright

    image side = "side ivy.png"

    i "Ughh, how did I end up in this game?"

    show jaime at left with easeinleft

    ja "Bruh! What are you guys up to?"

    show josue

    j "Whatever. Just get to the good part."
    j "Show em that street where we had an accident."

    scene bg street
    with fade

    play music "audio/libertines.mp3"

    n "You mean this street?"

    show josue

    j "NOOO! Not this one!"

    hide josue

    scene bg joslin

    n "oh you mean this one right?"

    show josue

    j "Yeah. This place"
    j "This place is loco."

    i "Ughhh, these guys are the worst. I'm not going near them, what do you guys want to do?"

    menu:
        "Ask about their bag of money":
            jump askAboutTheMoney
        "Casually walk by without making eye contact":
            jump justWalkBy
        "Get Jaime to approach them":
            jump jaimeApproaches

label askAboutTheMoney:
    show josue at left with easeinleft

    j "Que onda guey? (What's up dude?)"

    jump end

label justWalkBy:

    i "[whisters] These guys are worth the time of the day. Pay em no mind and just walk by."

    n "As they walk by Josue starts to glance over."

    i "OMG, what are you doing! Josue, don't!!!"

    n "One of the loiterers makes eye contact with Josue and immediately stands up. Josue turns to face him."

    jump ends

label jaimeApproaches:

    show jaime at left with easeinleft

    ja "What's up guys? Howabout this weather, pretty nice eh?"

    n "The loitering crew of bangers look up at Jaime. Two of them glance at each other, confused, then stand up."
    n "There's an awkward moment of silence..."
    n "Ivy and Josue both look at each other, then look down, too embarrassed to help him."
    n "Jaime takes a step back"

    ja "Real sunny. You know, such a nice day"
    n "Jaime looks terrified as the two boys approach."

label end:

    n "to be continued..."

    # This ends the game.

    return
