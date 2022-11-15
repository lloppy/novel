# Определение персонажей игры.
define kai = Character('Кай', color="#8803fc")
define a = Character('Элли', color="#8803fc", image = "ally")
define v = Character('Виктор', color="#8803fc", image = "victor")
define k = Character('Карэн', color="#8803fc", image = "karen")
define al = Character('Алан', color="#8803fc", image = "alan")
define news = Character('news', color="#8803fc", image = "news")
define news_array = ["first_news", "second_news", "thirg_news", "fourth_news", "fourth_news", "fifth_news"]

#для переписки по телефону
#define m_nvl = Character("Me", kind=nvl, image="nighten", callback=Phone_SendSound)
#define n_nvl = Character("News", kind=nvl, callback=Phone_ReceiveSound)

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
    image blackIm = "intro/first (1).png"

    show splash with dissolve
    $ renpy.pause(3.0)

    show blackIm with dissolve
    $ renpy.pause(2.0)

    image tab_hovered = Animation(
    "images/intro/loader (0).png", phone_transition_speed, 
    "images/intro/loader (1).png", phone_transition_speed, 
    "images/intro/loader (2).png")
    
    return

# screen show tab_minimized:
#     vbox xalign 0.995 yalign 0.98:
#         imagebutton:
#             idle "images/intro/loader (0).png"
#             hover "tab_hovered" 
#             action ui.callsinnewcontext("start")

# Игра начинается здесь:
label start:
    $ point = 0

    jump first_day_bus_news
    
    jump first_day_moring
    return


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
        action [Jump(news_array[point]), SetVariable("point", point + 1)]


# screen keymap_map():
#     key "K_KP_ENTER" action Jump("showmap")
#     # key "K_KP_ENTER" action Hide("nonexistent_screen")

# label showmap:
#     image loader = "intro/loader (0).png"
#     show loader


