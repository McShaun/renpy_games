#Intro Sequence

label start:
#Intro Paperwork
    scene black
    #sound of somebody walking in

    ra "...alright, so. You are here for new job at Crystaline, da?"

    ra "Well, you'll have go to through paperwork before being accepted."

    scene bg papers-intro-test
    with Dissolve(.7)
    #sound of papers rustling, papers background
    #this is a random comment by Shaun
    play music "audio/Fluorescent-sound_effect.mp3" loop

    ra "It will tell you how to fill out. You can figure rest out without me."

    ra "I am assuming you can read and write, so you should be fine."

    #fillout paperwork

    "Hello, fellow citizen. If you are reading this, you have complied with
    the ToS of Crystaline Corp, and have been accepted for a job application."

    "However if you think you have gotten this by mistake, or haven't read ToS, then
    you are to either ask an employer about the issue, or return this paper immediately."

    "If you do not return immediately, you will be fined."

    "This paperwork is for citizens interested in being employed for the {b}Crystaline Outpost
    and Furnished Settlement{/b}, a small building located outside the Main Complex."

    "Food and water will be provided during work hours, and you will also be provided
    warming clothes from Crytaline Corp."

    "Your job in the Outpost is to make sure no prisoners escape, and no citizens wander
    into the Main Complex grounds."

    "It will however not interfere with your ability to access the Complex as being an employee..."

    "You start to skip through all the boring stuff, you only noted weather conditions are frigid,
    and prisoners can be hostile."

    "Ah, here's where you sign up."

    python:
            name = renpy.input(_("Please sign your name on the line below."))

            name = name.strip() or __("New Guy")

    "Please note employees do not have to call you by this name, as they have a right not to.
    The Convicts however must call you by the name you have provided."

    "If you have signed this paper with a satire name, it is highly advised you go back and change it to your actual name."
