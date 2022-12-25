label fifth_day_root_love:
    scene testing department
    show grace 

    g @ smirk "К счастью, не все до последнего упираются в надежде поступить по совести. Есть и те, кто способен вовремя опомниться, и я таких людей очень уважаю. В конце концов, жизнь дороже."

    show grace at right

    show elly at left:
        linear 0.0 xzoom -1.0 yzoom 1.0
    
    "Элли… Значит ты все-таки выбрала другую сторону… Что же, разве могу я тебя винить. Все-таки Арон был прав. Доверять нельзя никому, а я доверился, а потому проиграл."

    g @ smirk "Так уж и быть. Пусть ты стал немаленькой проблемой для нас, стоит отдать должное твоим стремлениям. Пусть они и привели тебя сюда, но твердостью намерений ты заслужил последнее слово."

    "Как только я увидел тебя здесь, Элли, я начал вспоминать те немногие моменты, которые нам удалось разделить вместе, в стенах этой компании. 
    С самого начала ты тронула меня своими глуповатыми манерами и неидеальностью, которые одновременно сочетались с прекрасными способностями и чутким сердцем." 
    
    "Я видел в тебе человека, способного растопить любые льды переживаний. Но жизнь не всегда складывается так, как нам хочется. 
    Моя, видимо не сложилась. Но я всем сердцем надеюсь, что твоя сложится счастливо. Не вини себя за этот поступок. 
    Я тебя прощаю."

    g @ smirk "Как трогательно. Раз уж ты так зацепился за Элли, пусть именно она и отведет тебя в “последний отдел”. А чтобы все прошло гладко, вас сопроводит этот охранник."
    
    # (рут Элли)  soleCompany = 6 7    loveLine = 3 4  
    if (detective == 5):
        jump detective_root_plus
        return

    else:
        if (loveLine == 3):
            jump love_root_plus
            return
        else:
            jump love_root_minus
            return
    
    return



label detective_root_plus:
    return

label love_root_plus:
    scene testing department

    show guard
    with dissolve

    scene hall
    with dissolve
    pause 1.0

    scene elevator outside 
    with dissolve
    pause 1.0

    scene elevator inside
    with dissolve
    
    show guard at left:
        linear 0.0 xzoom -1.0 yzoom 1.0

    show elly at right

    "Значит такой конец у моей истории… Имей я возможность, многое бы изменил, но теперь поздно об этом рассуждать."

    e @ angry "Эй, [nameM]>!"

    "Чего?"

    hide guard
    show elly

    "Что она только что сделала!? Вырубила охранника!?"

    e @ angry "После твоих слов я задумалась о том, кем хочу быть в этом мире. Уж точно не убийцей! Скорее жми кнопку первого этажа, мы должны бежать."

    return

label love_root_minus:
    scene testing department

    show guard
    with dissolve

    scene hall
    with dissolve
    pause 1.0

    scene elevator outside 
    with dissolve
    pause 1.0

    scene elevator inside
    with dissolve
    
    show guard at left:
        linear 0.0 xzoom -1.0 yzoom 1.0

    show elly at right

    "Совсем не так я представлял конец своей жизни… Доверившись, я получил нож в спину. Хотя я и сказал, что прощаю ее, но на сердце все равно глубокая тоска от предательства человека, который был мне не безразличен."

    scene black:
        zoom 2.0
    with dissolve

    pause 2.0

    scene black:
        zoom 2.0
    pause 2.0

    return