# Определение персонажей игры.
define ki = Character('Кай', color="#8803fc", image = "kai")
define a = Character('Элли', color="#8803fc", image = "ally")
define v = Character('Виктор', color="#8803fc", image = "victor")
define k = Character('Карен', color="#8803fc", image = "karen")
define al = Character('Алан', color="#8803fc", image = "alan")

define detective = 0
define soleCompany = 0
define developer = 0

init:
    $ leftCoordinates = Position(xalign = 0.0, yalign = 0.6)
    $ leftDownCoordinates = Position(xalign = 0.0, yalign = - 1.6)
    $ rightCenterCoordinates = Position(xalign = 0.6, yalign = - 1.0)
    $ leftCenterCoordinates = Position(xalign = 0.3, yalign = - 2.0)




# Игра начинается здесь:
label start:
    
    scene bg ofis
    with fade
    #with blinds  #эффект жалюзи
    #with wipeleft
    #with pushleft

    "{s}lllallalalalala vhodim v lor lalalallalalalalala kak vse kruto{/s}"
    "{s}lllallalalalala  lalalallalalalalala kak vse kruto{/s}"
    with fade

    show kai at leftCoordinates
    with dissolve
    #with easeinleft

    ki "{cps=30}Привет, я {i}Кай{/i}, твой новый колллега. Я отучился на разработчика...{/cps}"
    ki "{cps=30}... провалил несколько собеседований ...{/cps}"
    ki "{cps=30}... Hо однажды тим лид заметил меня и решил провести {i}личное собеседование{/i}, {w}и я {b}прошел{/b}! {w}Ляляля тополя, я прошел, и ты тоже пройдешь!{/cps}"

    hide kai with fade

    "Хм... {w}что за газета лежит на столе?"
    
    menu:
        "Что сделать?"

        "Посмотреть" if detective > -1:
            jump newspaper

        "Игнорировать":
            jump dontwatchnewspaper

    return

label newspaper:

    show newspaper at truecenter
    with fade

    "6 июля 2039 года: {w}{cps=35}Японский суперкомпьютер нашел способ оказывать непосредственное влияние на нейроны человеческого организма{/cps}"
    "7 июля 2039 года: {w}{cps=35}Фондовый рынок Японии достиг 20-летнего максимума всего за сутки{/cps}"
    "7 ноября  2039 года: {w} {cps=35}Япония и США впервые продемонстрируют прототип нейронного микрокомпьютера{/cps}"
    "12 мая 2040 года: {w}{cps=35}Нашумевшая технология Neuroconnect: как пустить все амбиции на бесперспективное будущее{/cps}"
    "27 июня 2040 года: {w} {cps=35}Стало известно, чем так выгодны видеоигры нового поколения{/cps}"

    $ detective += 1

    hide newspaper with fade
    "kakoy zhe tut pizdec tvoritsa"

    jump acquaintance
    return
    
label dontwatchnewspaper:   

    jump acquaintance
    return

label acquaintance:

    scene bg office
    with fade

    show ally normal at right
    with dissolve

    a "{cps=30}Me, I died for him{/cps}"
    a crazy "{cps=30}no , Я предам тебя)))...{/cps}"


    show victor normal at leftDownCoordinates
    with easeinleft
    v "{cps=30}Me, {/cps}"
    v closeyes "{cps=30}I trusted him{/cps}"


    show karen smile at rightCenterCoordinates
    with dissolve
    k "{cps=30}Me, {w}I loved him{/cps}"

    show alan angry at leftCenterCoordinates
    with dissolve
    al "{cps=35}And me, {w}I'm the damn fool that shot him (shot him, shot him){/cps}"


    jump profession
    return


label profession:

    "vremya ohuitelnih istoriy"

    $ soleCompany += 1

    jump askGame
    return


label askGame:

    scene bg ofis with fade

    show karen smile with dissolve

    k "can i ask a question?"

    menu:
        "сколько зарабатывает программист???"

        "1000000000000000000000000 млн долларов":
            jump trueAnswer

        "программисты бомжи":
            jump falseAnswer

    return

label trueAnswer:
    $ developer += 1

    jump street
    return

label falseAnswer:
    jump street
    return


label street:
    scene bg cloudcity with fade

    "LALISA LALISA LALISA LALISA LALALALLAL WHATS MY NAME?!"
    return