# Определение персонажей игры.
define k = Character('Кай', color="#8803fc", image = "kai")

define detective = 1

init:
    $ leftCoordinates = Position(xalign = 0.0, yalign = 0.6)



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

    k "{cps=30}Привет, я {i}Кай{/i}, твой новый колллега. Я отучился на разработчика...{/cps}"
    k "{cps=30}... провалил несколько собеседований ...{/cps}"
    k "{cps=30}... Hо однажды тим лид заметил меня и решил провести {i}личное собеседование{/i}, {w}и я {b}прошел{/b}! {w}Ляляля тополя, я прошел, и ты тоже пройдешь!{/cps}"

    hide kai with fade

    "Хм... {w}что за газета лежит на столе?"
    
    menu:
        "Что сделать?"

        "Посмотреть" if detective > 0:
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
    return
    
label dontwatchnewspaper:


    return
