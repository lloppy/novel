label third_day_second_task:
    show computer second_task
    with dissolve

    pause 1.2    

    show computer _screen second_task
    with dissolve  

    "Задание 2: ознакомьтесь с некоторыми птицами из вашего проекта и подберите цвет для новой, учитывая сочетаемость цветов и другие факторы, описанные ранее"
    call screen button_second_game


label third_day_second_task_correct:
    if computerWrongAnsSecond == 0:
        "Это было очевидно…"
        $ developer += 1
        $ score[1] = 1
        jump third_day_third_task

    else:
        "Ну, хотя бы со второго раза…"
        jump third_day_third_task
        $ developer += 0.5
        $ score[1] = 1
    return




label third_day_second_task_wrong:
    $ computerWrongAnsSecond += 1
    if computerWrongAnsSecond == 2:
        "Я правда не знаю правильный ответ… Остается только пропустить это задание и перейти к следующему."
        jump third_day_third_task 
        
    "Неверно!"

    "Странно… Я был уверен в ответе. Может попросить помощи у Кая?"

    scene office2
    with fade

    "Кай, ты не мог бы мне помочь?"
    show kai serious at left
    with OffsetLeftToLeftSide

    if soleCompany >= 1:
        kai "Ну, сказать ответ я тебе не могу, ты уж извини. Но могу дать подсказку: обрати внимание на то, с чем взаимодействует данная птица. Уверен, ты догадаешься, какой цвет стоит применить."
        "Кажется, я понял, о чем ты."
        show computer _screen second_task
        with dissolve  
        call screen button_second_game

    else:
        kai "Я очень занят, а задание невероятно простое. Вспомни все, чему тебя учили."
        show computer _screen second_task
        with dissolve  
        call screen button_second_game
        


screen button_second_game:
    imagebutton:
        xalign 0.2
        yalign 0.76
        idle "tools/game angry birds/2 задание/btn grey second_task.png"
        hover "tools/game angry birds/2 задание/btn grey second_task.png"
        action Jump("third_day_second_task_correct")
        
    imagebutton:
        xalign 0.4
        yalign 0.76
        idle "tools/game angry birds/2 задание/btn black second_task.png"
        hover "tools/game angry birds/2 задание/btn black second_task.png"
        action Jump("third_day_second_task_wrong")

    imagebutton:
        xalign 0.6
        yalign 0.76
        idle "tools/game angry birds/2 задание/btn brown second_task.png"
        hover "tools/game angry birds/2 задание/btn brown second_task.png"
        action Jump("third_day_second_task_wrong")

    imagebutton:
        xalign 0.8
        yalign 0.76
        idle "tools/game angry birds/2 задание/btn pink second_task.png"
        hover "tools/game angry birds/2 задание/btn pink second_task.png"
        action Jump("third_day_second_task_wrong")