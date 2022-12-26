label fifth_day_root_team:
    scene testing department
    show grace

    g @ smirk "Жаль, что из-за твоих идеалов погибнет еще один человек, который больше стал жертвой обстоятельств, чем борцом за справедливость."

    show grace at right

    show karen scared at left:
        linear 0.0 xzoom -1.0 yzoom 1.0

    "Нет, не трогайте Карэн! Она не при чем… Вся вина лежит на мне, она даже ничего не знает."

    show kai at left
    show grace at right
    show karen scared

    kai @ angry "Уверен? А я своими ушами слышал, как ты рассказывал вчера о нейрочипах и влиянии игр на выработку адреналина, за счет чего падает агрессия. Или мне показалось?"

    "Кай… Да как ты можешь так поступать? Помнишь первый день? Как ты рассказал мне о Карэн.
    Я тогда не смог разглядеть ее доброту, а ты убеждал, что я просто должен получше ее узнать?"
    "Куда же это все пропало? Ведь если бы не она, ты бы не попал в компанию, твоя судьба вообще могла сложиться куда трагичнее."

    kai @ smile_ce "К счастью для меня, в итоге трагичной оказалась только твоя судьба. Выведите его в “последний отдел”, охрана."
    

    # (рут команды - Карэн) soleCompany = 5 6 7    loveLine = 3  
    if (detective == 5):
        jump detective_root_plus
        return

    else:
        if (soleCompany >= 6):
            jump team_root_plus
            return
        else:
            jump worst_root
            return

    return


label team_root_plus:
    scene testing department

    show kai at left
    show grace at right
    show karen scared
    
    g @ smirk "Постойте. Раз уж ты так беспокоишься за Карэн, я оставлю ее в живых. Не обещаю ей легкую судьбу, 
    но жива останется. Чего не могу сказать про тебя. Ты поступил как джентльмен, но пришло время прощаться."

    show guard
    with dissolve

    scene hall
    with dissolve
    pause 0.6

    scene elevator outside 
    with dissolve
    pause 0.6

    scene elevator inside
    with dissolve
    
    show guard at right

    "Совсем не так я представлял конец своей жизни… Доверившись, я получил нож в спину. {w}
    Я считал Кая своим другом, а отдел чем-то вроде своего второго дома. {w}К сожалению, получилось спасти только Карэн. {w}
    Но я рад, что хотя бы она увидит свет будущих дней…"

    scene black:
        zoom 2.0

    pause 2.0

    jump end

    return

label worst_root:
    scene testing department

    scene elevator inside
    with dissolve
    
    show guard at right
    with dissolve

    "Вот и все.{w} Я не был готов уходить так рано, но судьба распорядилась иначе."
    
    scene elevator inside
    show guard at right
    pause 0.5

    "Кто бы знал, что такое событие, как стажировка, в конце концов приведет меня к гибели."

    "Я о многом жалею: я не смог никого спасти.{w} Мир не изменился."
    
    "Люди сами сделали предательства и ложь частью своих жизней. {w}
    Может и не стоит жалеть об упущенных возможностях в таком мире?"
    
    "Но я не оставил о себе никакой памяти."

    "Вроде и не было никогда никакого Макса." 
    
    "Страшно."

    scene black:
        zoom 2.0

    pause 2.0

    jump end
    
    return