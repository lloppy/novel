label third_day_end:
    scene office computer
    with fade

    show computer first_task
    with dissolve        
    "В ходе работы над проектом вам нужно будет реализовать функцию для поиска нужного угла, подобрать правильную цветовую палитру, а также сохранить все в git репозитории)"
    
    show computer _screen first_task
    with dissolve  

    # style.window.background = Image("images/tools/tool/black.png", xalign=0.5, yalign=1.0)

    jump check_answer
    return
    
label checked_answer:
    if (ans_angry_birds == "0.5 * Math.Asin(distance * 9.8 / (v * v));" or ans_angry_birds == "0.5 * Math.Asin(distance * 9.8 / (v * v))" or  ans_angry_birds == "1/2 * asin(g * distance / v^2)" or ans_angry_birds == "1/2 * asin(g * distance / v^2);" or ans_angry_birds == "0.5 * Math.Asin(distance * 9.8 / (v^2));" or ans_angry_birds == "0.5 * Math.Asin(distance * 9.8 / (v^2))" ):
        show computer _screen first_task right
        with dissolve
        
        # show bird1 at truecenter_custom:
        #     zoom 0.85
        # $ renpy.pause(0.15)
        # show bird2 at truecenter_custom:
        #     zoom 0.85
        # $ renpy.pause(0.15)
        # show bird3 at truecenter_custom:
        #     zoom 0.85
        # $ renpy.pause(0.15)
        # show bird4 at truecenter_custom:
        #     zoom 0.85
        # $ renpy.pause(0.15)
        # show bird5 at truecenter_custom:
        #     zoom 0.85
        # $ renpy.pause(0.15)

        if computerWrongAns == 0:
            "С первого раза! Как же я хорош… Если следующие задания такие же простые, то я зря волновался."
            $ developer +=2
            $ score[0] = 1
            jump third_day_second_task

        else:
            "Было не так уж просто, но я справился. Можно продолжать проект."
            $ score[0] = 1
            jump third_day_second_task
    else:
        jump not_check_answer


label check_answer:
    scene computer _screen first_task

    $ ans_angry_birds = renpy.input("Задание 1: реализуйте функцию расчета угла прицеливания, в зависимости от начальной скорости снаряда и дальности до цели")
    call screen run_game


        


label not_check_answer:
    $ computerWrongAns +=1
    show computer _screen first_task wrong
    with dissolve

    if computerWrongAns == 5:
        scene office2
        with fade

        show kai serious
        kai "Да что же такое! Ну разве это сложно? Дай я напишу по-быстрому, и будешь работать дальше. А то такими темпами ты проект не закончишь."
        kai "0.5 * Math.Asin(distance * 9.8 / (v * v))"

        show computer _screen first_task right
        with dissolve
        $ developer -=1
        $ score[3] = True

        "Спасибо, конечно… Но я и сам как-нибудь справился бы."

        show kai smile_with_disbelief
        kai "Несомненно"
        
        jump third_day_second_task
        return

    "Не работает… И где я мог ошибиться?"


    menu:
        "Поискать ответ самостоятельно":
            jump check_answer
        "Воспользоваться телефоном":
            show phone task _help at left
            with dissolve
            $ score[3] = True


            if computerWrongAns >= 1:
                call screen btn_help_karen
            else: 
                call screen btn_help



label ask_help_Karen:
    scene office
    with fade
    play sound "music/keyboard.mp3" fadein fadein volume volume 

    show karen

    "Карэн, у меня проблема с первым заданием. Не могла бы ты мне помочь?"
    $ score[3] = True
    if soleCompany >= 1:
        k "Ну, на тебя немного времени выделю. Что именно тебе подсказать?"
        "Я не могу написать формулу. Не могла бы ты мне ее напомнить?"
        stop sound fadeout 2.0


        show karen smile
        k "Конечно. Если тебе нужна формула для угла прицеливания, то это одна вторая на арксинус частного произведения ускорения свободного падения на дистанцию и начальной скорости в квадрате"
        k "1/2 * asin(g * distance / v^2)"

        "Спасибо!"

        scene computer _screen first_task
        with fade

        show computer _screen first_task right
        with dissolve

        "Фух,  все получилось, спасибо Карэн."
        $ developer += 1
        jump third_day_second_task

    else:
        k "Прости, я очень занята сейчас. Попробуй посидеть и подумать еще, уверена, все получится. А теперь возвращайся к своему месту. "
        stop sound fadeout 2.0
        jump check_answer
    return

label ask_help_Internet:
    "Найдена правильная формула:  0.5 * Math.Asin(distance * 9.8 / (v * v))"
    $ developer -= 1
    jump third_day_second_task
    return

    
screen run_game:
    imagebutton:
        xalign 0.864
        yalign 0.809
        idle "tools/game angry birds/1 задание/btn first_task.png"
        hover "tools/game angry birds/1 задание/btn first_task.png"
        action Jump("checked_answer")

screen btn_help:
    imagebutton:
        xalign 0.517
        yalign 0.31
        idle "tools/game angry birds/btn task _help internet.png"
        hover "tools/game angry birds/btn task _help internet.png"
        action Jump("ask_help_Internet")

screen btn_help_karen:
    imagebutton:
        xalign 0.517
        yalign 0.36
        idle "tools/game angry birds/btn task _help karen.png"
        hover "tools/game angry birds/btn task _help karen.png"
        action Jump("ask_help_Karen")

    imagebutton:
        xalign 0.517
        yalign 0.31
        idle "tools/game angry birds/btn task _help internet.png"
        hover "tools/game angry birds/btn task _help internet.png"
        action Jump("ask_help_Internet")