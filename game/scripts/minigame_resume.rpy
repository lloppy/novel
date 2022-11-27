default mark = [True,False,False,False,False,False,False,False,False,False,False]
default posX = [0.33541,0.16406,0.16875,0.16875,0.16875,0.16875,0.16875,0.16875,0.31562,0.50208,0.58489]
default posY = [0.10185,0.19722,0.22037,0.28981,0.45462,0.50092,0.54722,0.66296,0.75833,0.75833,0.75833]
default num = [0,1,2,3,4,5,6,7,8,9,10]

init python:
    def toggleMark(ind):
        global mark

        if(mark[ind]):
            mark[ind] = False
        else:
            mark[ind] = True
        renpy.restart_interaction()

    ToggleMark = renpy.curry(toggleMark)

label resumeGame:
    show resume
    call screen texts

    jump second_day_contunue_after_game
    return

    
screen texts:
    for i in num:
        imagebutton:
            selected mark[i]
            xpos posX[i]
            ypos posY[i]
            idle "resume_minigame/resume mark" + str(i+1) + ".png"
            hover "resume_minigame/resume mark" + str(i+1) + ".png"
            selected_idle "resume_minigame/resume mark" + str(i+1) + " cross.png"
            selected_hover "resume_minigame/resume mark" + str(i+1) + " cross.png"
            action ToggleMark(i)
            #hovered Cursor("resume_minigame/pen")
            #unhovered Cursor(None)