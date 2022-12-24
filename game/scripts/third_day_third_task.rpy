label third_day_third_task:
    scene computer one three_task
    with fade    

    pause 1.0

    show computer screen1 three_task
    with dissolve  

    "Задание 3: наконец, синхронизируйте все с помощью git. Для этого вспомните все изученные команды и примените их в правильной последовательности"

    "Так, это должно быть нетрудно."
    call screen git_commands

    
screen git_commands:
    imagebutton:
        xalign 0.93
        yalign 0.15
        idle "tools/game angry birds/3 задание/btn push three_task.png"
        if tap == 3:
            hover "tools/game angry birds/3 задание/btn push right three_task.png"
        else:
            hover "tools/game angry birds/3 задание/btn push wrong three_task.png"
        action Jump("computer_screen4_three_task")

    imagebutton:
        xalign 0.93
        yalign 0.30
        idle "tools/game angry birds/3 задание/btn add three_task.png"
        if tap == 1:
            hover "tools/game angry birds/3 задание/btn add right three_task.png"
        else:
            hover "tools/game angry birds/3 задание/btn add wrong three_task.png"
        action Jump("computer_screen2_three_task")

    imagebutton:
        xalign 0.93
        yalign 0.45
        idle "tools/game angry birds/3 задание/btn commit three_task.png"
        if tap == 2:
            hover "tools/game angry birds/3 задание/btn commit right three_task.png"
        else:
            hover "tools/game angry birds/3 задание/btn commit wrong three_task.png"
        action Jump("computer_screen3_three_task")

label computer_screen2_three_task:
    scene computer_screen2_three_task
    with dissolve
    $ tap += 1
    call screen git_commands

label computer_screen3_three_task:
    scene computer screen3 three_task
    with dissolve
    $ tap += 1
    call screen git_commands
    
label computer_screen4_three_task:
    scene computer screen4 three_task
    with dissolve
    $ tap += 1
    $ score[2] = 1
    $ developer += 1    
    jump end_second_game

label end_second_game:
    scene office2
    with fade
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show kai 
    "Кай, я вроде как закончил. Кто-то должен меня оценить?"

    kai "Да, сейчас я подойду к Карэн, и мы посмотрим, как ты справился."
    stop sound fadeout 2.0

    "Страшновато…"

    show kai  serious
    kai "Обсудим твою работу втроем, пойдем."

    scene office
    with fade
    play sound "music/keyboard.mp3" fadein fadein volume volume
     

    show karen at right
    show kai at left
    $ totalScore  = score[0] + score[1] + score[2]
    stop sound fadeout 2.0

    if (totalScore == 3 and score[3] == True ):
        k "Ты приятно удивил нас результатом работы над проектом. Все задания решены верно. 
        Конечно, ты прибегнул к нашей помощи, но ведь так и должна работать команда!"
        $ soleCompany += 1

        show karen smile
        k "Ты старался уважительно относиться к нам и прислушиваться к нашим советам - взамен мы старались помогать тебе по мере наших возможностей. 
        Обсуждая с Каем твое пребывание тут, мы сошлись на мнении, что хотели бы поработать с тобой снова когда-нибудь."

        show kai smile
        kai "Это правда, мне было приятно учить тебя и наблюдать, как ты погружаешься в наш мир. Надеюсь, доведется поработать вместе еще!"
    
    if (totalScore == 3 and score[3] == False ):
        $ developer += 1
        show karen smile
        k "Не буду скрывать, нас поразило, что ты справился со всеми заданиями, но при этом ни разу не воспользовался нашей помощью. 
        Впечатляет, что первокурсник так успешно выполнил не самые простые задания."

        show karen smile_ce_blush
        k "Мне кажется, с твоими навыками и способностями к обучению тебя ждет большое будущее в любой компании, но было бы славно, 
        если бы ты продолжил изучение геймдева в нашей компании. Я сделаю все, что в моих силах, 
        чтобы ты получил приглашение на работу. Кай, есть что добавить?"
        show karen smile

        kai "Да! Знаешь, я ведь не из самой продвинутых программистов нашего отдела. 
        Поэтому я даже сейчас чувствую, что в чем-то начинаю тебе уступать. А ведь ты всего три дня провел у нас. 
        Чего же ты добьешься за более значительный срок?" 
        show kai smile
        kai "Одним словом, я тоже в предвкушении того, что тебя позовут к нам, но уже как полноценного работника."
    if ( totalScore >= 1 and score[4] == True ):
        show karen
        k "Честно говоря, мы сидели с Каем и обсуждали то, что тебе не удалось справиться со всем. 
        Рассуждали, насколько сами в этом виноваты, но нас прервало сообщение одной моей знакомой из отдела на 93-м. 
        Она рассказала, что ты вместо прослушивания лекции у доски потратил время, помогая ей с компьютером."

        k "Не знаю, насколько это перекрывает не очень успешно выполненный тобой проект, 
        но не отметить твое стремление помогать окружающим я просто не могу. 
        Возможно, именно такие, готовые всегда прийти на помощь, люди и нужны нашему отделу."
        show karen smile
        k "Я думаю, ты смог бы сделать нашу работу чуточку лучше, а уж знания подтянуть всегда можно, было бы желание. 
        Одним словом, я надеюсь, что еще доведется поработать вместе."
        show kai smile
        kai "Присоединяюсь ко всем словам Карэн. Ты хороший человек, а хорошего специалиста еще можно успеть сделать. Верю, что еще увидимся."

    else:
        k "Мы обсудили с Каем твой проект. Думаю скрывать тут нечего, ты и правда не очень хорошо справился. 
        Но наша задача как твоих наставников сохранить в тебе стремление продолжать изучать геймдев, несмотря на неудачи."
        k "Сегодня ты не справился, а завтра все получится. Ключевой фактор - твои желания, стремления и цели. 
        Упорно занимаясь, ты рано или поздно добьешься того, к чему стремишься. 
        И это упорство и есть главная черта самых лучших специалистов."
        show karen smile
        k "Я верю, что она не чужда тебе, а потому со временем ты раскроешься как профессионал в области геймдева. 
        Хочу пожелать тебе целеустремленности и терпения."
        show kai smile
        kai "Знаешь, когда-то я ходил по собеседованиям и все время получал отказы. Но я не терял огня в глазах, и в конце концов меня заметили, и вот я тут, сижу перед тобой и наставляю уже тебя. Не теряй и ты веру в себя."

    show karen say
    k "И еще кое-что. Можно сказать, напутственный совет. Не забывай, что для любого специалиста важно иметь портфолио с может и небольшими, 
    но раскрывающими его способности работами. Попробуй набить руку на маленьких проектах, 
    а чтобы работать было чуточку проще, используй готовые игровые движки: RPGMaker VX, CraftStudio, Quest."
    show karen

    "Спасибо вам огромное. Эти три дня открыли для меня окно в огромный мир, масштаб которого, наверное, 
    я до сих пор не осознал. Я ценю потраченное вами на меня время и обещаю, что потрачено оно было не зря. 
    Я продолжу развиваться и, надеюсь, когда-нибудь вернусь к вам и узнаю вас получше. А теперь я пойду, до свидания!"

    show karen smile_ce_blush
    "Пока-пока!"

    show kai smile
    "Удачи!"


    scene bus3:
        zoom 2.0
    with fade

    play sound "music/autobus.mp3" fadein fadein fadeout 3.0 volume 0.1

    "Кажется, что столько всего произошло, хотя прошло всего три дня. 
    Все еще свежи воспоминания о всех моих страхах в автобусе по пути в корпорацию. 
    А теперь я уже знаком с некоторыми ее работниками, которые прежде казались какими-то особенными, лучшими из лучших."
    play sound "music/music good.mp3" fadein 3.0 volume 0.2

    scene bus1:
        zoom 2.0
     
    "Конечно, они действительно хорошие специалисты, но такие же люди, со своими переживаниями и эмоциями. 
    Самое главное, что я сделал - разрушил барьер между собой и геймдевом, сотканный из моих страхов. 
    Теперь во мне осталось лишь желание совершенствоваться, которое никак не зависит от неудач на моем пути."
    
    "Я буду работать, чтобы стать лучше, чтобы вернуться в команду."
    stop sound fadeout 0.1

    return