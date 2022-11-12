# Определение персонажей игры.
define kai = Character('Кай', color="#8803fc")
define a = Character('Элли', color="#8803fc", image = "ally")
define v = Character('Виктор', color="#8803fc", image = "victor")
define k = Character('Карэн', color="#8803fc", image = "karen")
define al = Character('Алан', color="#8803fc", image = "alan")

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

# Игра начинается здесь:
label start:
    $ point = 0

    jump first_day_bus_news
    
    jump first_day_moring
    return




 
