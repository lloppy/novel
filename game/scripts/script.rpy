# Определение персонажей игры.
define kai = Character('Кай', color="#8803fc")
define a = Character('Элли', color="#8803fc", image = "ally")
define v = Character('Виктор', color="#8803fc", image = "victor")
define k = Character('Карэн', color="#8803fc", image = "karen")
define al = Character('Алан', color="#8803fc", image = "alan")
define news = Character('news', color="#8803fc", image = "news")
define loaders_array = ["intro/loader (0).png", "intro/loader (1).png", "intro/loader (2).png",
"intro/loader (3).png","intro/loader (4).png","intro/loader (5).png","intro/loader (6).png",
"intro/loader (7).png","intro/loader (8).png","intro/loader (9).png","intro/loader (10).png","intro/loader (11).png"]

#для переписки по телефону
#define m_nvl = Character("Me", kind=nvl, image="nighten", callback=Phone_SendSound)
#define n_nvl = Character("News", kind=nvl, callback=Phone_ReceiveSound)

define currNews = -1
define newsImage = ["one" , "two", "three", "three", "four", "four", "four", "four", "four", "five"]
define newsText = ["Все началось в июле 2039 года, когда в Японии научились воздействовать на мозг человека напрямую с компьютера. Не сказать, что 6 числа это казалось грандиозным открытием. Где-то в научных кругах, конечно, многие считали технологию прорывной, но для обычного человека, погруженного в ежедневную рутину, это было просто “еще одно научное открытие”.",
"На следующий день волна споров и противоречивых прогнозов накрыла уже область экономики, когда японский рынок резко прыгнул на такую отметку, какую не достигал десятилетиями.",

"Через четыре месяца все только и делали, что обсуждали грядущий выход первого массового компьютера, работающего по этой новой технологии. Кто-то в страхе рассказывал каждому встречному, что нельзя пользоваться новым изобретением, потому что оно наносит непоправимый вред организму, кто-то воодушевленно рассуждал о перспективах, открывающихся благодаря транслированию сигнала прямо в мозг.",
"Но объединяло всех одно:{w} уже никто не оставался в стороне от обсуждения Neuroconnect.",

"Полгода мы наблюдали, как мир меняется прямо на наших глазах. Игровая индустрия росла как на дрожжах, разработчик игр стал одной из самых желанных профессий. Если ты работаешь в крупной игровой корпорации, тебе не нужно задумываться о деньгах, тебя окружают лучшие из лучших, а из твоего офиса в самом центре города открывается превосходный вид на тех, кому не так сильно повезло с местом работы.",
"Помню, как все мои знакомые разделились на два лагеря: тех, кто буквально стал зависим от транслируемых прямо в разум игр, и тех, кто мечтал однажды получить приглашение на работу хотя бы в самой крошечной игровой студии.",
"Я никогда не причислял себя к какой-то из этих групп, мне одновременно было приятно погружаться в мир игры, словно самостоятельно переживая десятки чужих жизней и тысячи ситуаций, и изучать устройство таких игр, слушать об интересных механиках, делающих игровой опыт настолько интересным, и придумывать собственные геймдизайнерские решения. И все же мое увлечение играми никогда не доходило до непосредственного создания чего-то своего.",
"А сейчас я еду на встречу собственной мечте и переживаю, что ничего из себя не представляю."
"Кажется, уже пора готовиться к выходу. Хотя я могу успеть прочитать еще одну статью. Возможно, это поможет мне в первый день стажировки - все-таки я хочу как можно лучше подготовиться.",

"Я никогда об этом не задумывался. Действительно, хотя многие люди стали затворниками и бросили свои прежние занятия, просто чтобы дома сутками проходить игры, правительство никак не реагирует.{w} Интересно, чем же все это может быть выгодно?"
]

define detective = 0
define soleCompany = 0
define developer = 0

init:
    $ leftCoordinates = Position(xalign = 0.0, yalign = 0.6)
    $ leftDownCoordinates = Position(xalign = 0.0, yalign = - 1.6)
    $ rightCenterCoordinates = Position(xalign = 0.6, yalign = - 1.0)
    $ leftCenterCoordinates = Position(xalign = 0.3, yalign = - 2.0)
    $ phone_transition_speed = 0.05 #Using a variable to make testing different speeds easier.

 
label splashscreen:
    image splash = "intro/first.png"
    image blackIm = "intro/black.png"
    image enterPressed = "intro/center_text.png"

    show splash with dissolve
    $ renpy.pause(3.0)

    show blackIm with dissolve
    $ renpy.pause(2.0)

    show enterPressed at truecenter
    with dissolve 
    
    call screen keypress

    return

screen keypress():
    key "K_SPACE" action Jump("succeeded")
    timer 4.0 action Jump("splashscreen")

label succeeded:
    image loader0 = "intro/loader (0).png"
    image loader1 = "intro/loader (1).png"
    image loader2 = "intro/loader (2).png"
    image loader3 = "intro/loader (3).png"
    image loader4 = "intro/loader (4).png"
    image loader5 = "intro/loader (5).png"
    image loader6 = "intro/loader (6).png"
    image loader7 = "intro/loader (7).png"
    image loader8 = "intro/loader (8).png"
    image loader9 = "intro/loader (9).png"
    image loader10 = "intro/loader (10).png"
    image loader11 = "intro/loader (11).png"

    show loader0 at right
    pause 0.3
    show loader1 at right
    pause 0.3
    show loader2 at right
    pause 0.3
    show loader3 at right
    pause 0.3
    show loader4 at right
    pause 0.3
    show loader5 at right
    pause 0.3
    show loader6 at right
    pause 0.3
    show loader7 at right
    pause 0.3
    show loader8 at right
    pause 0.3
    show loader9 at right
    pause 0.3
    show loader10 at right
    pause 0.3
    show loader11 at right
    pause 4.0


    return


# Игра начинается здесь:
label start:

    $ point = 0
    jump first_day_bus_news
    
    jump first_day_moring
    return


label news:
    $ currNews += 1

    $ renpy.show("news " + newsImage[currNews])
    $ textC = newsText[currNews]

    "{size=-6}{cps=43}[textC]{/cps}{/size}"

    if currNews == 5:
        $ detective += 1
        jump end_bus

    call screen closebutton

screen closebutton:
    imagebutton:
        xalign 0.714
        yalign 0.259
        idle "closebutton.png"
        hover "closebutton.png"
        action Jump("end_bus")

    imagebutton:
        xalign 0.258
        yalign 0.47
        idle "nextbutton.png"
        hover "nextbutton.png"
        action Jump("news")