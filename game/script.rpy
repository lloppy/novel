# Определение персонажей игры.
define ki = Character('Кай', color="#8803fc", image = "kai")
define a = Character('Элли', color="#8803fc", image = "ally")
define v = Character('Виктор', color="#8803fc", image = "victor")
define k = Character('Карен', color="#8803fc", image = "karen")
define al = Character('Алан', color="#8803fc", image = "alan")
define phone = Character('phone', color="#8803fc", image = "phone")

define m_nvl = Character("Me", kind=nvl, image="nighten", callback=Phone_SendSound)
define n_nvl = Character("News", kind=nvl, callback=Phone_ReceiveSound)


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
      

    "{size=-6}{cps=43}Прошло уже несколько дней, а я все никак не осознаю произошедшее.{w}
     Только заметив новое уведомление, я сразу принял сообщение за спам.
     Но как и любой человеческий интерес, мое желание ознакомиться с содержимым перевесило 
     возможное раздражение от еще одной впустую потраченной минуты.
     Тогда я инстинктивно нажал на экран смартфона и принялся читать...{/cps}{/size}"



    show phone:
        zoom 2.0 

    "{size=-6}{cps=43}Уже с первых строк стало понятно, что чутье меня подвело 
    (что случается довольно часто, так что удивлен я совсем не был), 
    и написанное вовсе не является спамом. Собеседник представился HR менеджером компании, 
    занимающейся коммерческой разработкой игр.{/cps}{/size}"

    scene bus2:
        zoom 2.0

    "{size=-6}{cps=43}Сообщение было большое, так что все его  
    вспомнить не могу, но вот его суть я вряд ли смогу забыть:{w} меня позвали на стажировку 
    на должность разработчика в одну из студий корпорации. Первый возникший в голове вопрос 
    - где они меня нашли?{/cps}{/size}" 
    
    "{size=-6}{cps=43}Помню, что в начале года разослал десяток заявок по разным компаниям, 
    но я и представить не мог, что хоть кто-то из них откликнется и рассмотрит мою кандидатуру. 
    Да и времени с тех пор столько прошло..{/cps}{/size}" 
    
    "{cps=43}Но почему они выбрали именно меня?{/cps}" 
    
    scene bus1:
        zoom 2.0

    "{size=-9}{cps=43}Говоря начистоту, я никак не могу назвать свои способности выдающимися. Я не обрел популярность за первый 
    (и пока мой единственный) год обучения в университете, не одарен творческим талантом, 
    не люблю брать на себя ответственность и ненавижу соблюдать дедлайны, что выливается 
    в мои постоянные долги по тем предметам, где для успешного выполнения работы нужно 
    кропотливо уделять задаче кусочек каждого своего дня.{/cps}{/size}" 
    
    "{size=-6}{cps=43}Одним словом, я всегда балансировал 
    между понятиями “перспективный разработчик” и “бездарный кодер, будущее которого 
    весьма и весьма смутно”.{/cps}{/size}" 

    "{size=-6}{cps=43}Но даже если поверить в свою удачу и принять тот факт, 
    что огромная корпорация действительно заинтересовалась первокурсником, во мне остается
    куча переживаний о самой стажировке.{/cps}{/size}" 
    
    scene bus3:
        zoom 2.0

    "{size=-6}{cps=43}Еще во время учебного года мой одногруппник, 
    победитель региональных олимпиад по программированию и начинающий разработчик игр, 
    тоже был приглашен в большую компанию, где проходил стажировку несколько недель.{/cps}{/size}"
    
    "{size=-6}{cps=43}Но даже его опыта не хватило, чтобы впечатлить руководство и заполучить должность.{w}
    На что же надеяться мне?{w} Конечно, у меня есть некоторый опыт программирования, 
    в этом году я даже был частью команды, отвечающей за разработку университетского 
    сервиса для работы с абитуриентами. Вот только никакого опыта создания игр у меня нет.{/cps}{/size}"
    
    "{size=-6}{cps=43}Можно сколько угодно смотреть видео по геймдизайну, слушать подкасты и изучать механики 
    в полюбившихся мне играх. Но пока за моей душой нет ни строчки кода игры,{i} разве я могу
     быть уверен, что это мое?{w} Могу ли с уверенностью идти на стажировку, зная, что не облажаюсь?{/i}{/cps}{/size}"
     
    scene bus2:
        zoom 2.0

    "{size=-6}{cps=43}Мысли о провале настолько поглотили меня, что я совсем забыл хоть немного изучить компанию, 
     в которой собираюсь постигать основы разработки игр. А ведь они вполне могут захотеть проверить 
     мои знания об индустрии, и это еще одна возможность показать себя с худшей стороны.{/cps}{/size}"

    "{size=-6}{cps=43}Кажется, я могу успеть освежить в своей памяти, 
    как игровые корпорации стали одной из самых влиятельных частей экономики."


    #n_nvl "В Японии научились воздействовать на мозг человека напрямую с компьютера"

    "{size=-6}{cps=43}Все началось в июле 2039 года, когда в Японии научились воздействовать на мозг человека 
    напрямую с компьютера. Не сказать, что 6 числа это казалось грандиозным открытием. 
    Где-то в научных кругах, конечно, многие считали технологию прорывной, но для обычного человека, 
    погруженного в ежедневную рутину, это было просто “еще одно научное открытие”.{/cps}{/size}"

    #n_nvl "Японский рынок вышел на первое место в мире по уровню ВВП"

    "{size=-6}{cps=43}На следующий день волна споров и противоречивых прогнозов накрыла уже область экономики, 
    когда японский рынок резко прыгнул на такую отметку, какую не достигал десятилетиями.{/cps}{/size}"

    #n_nvl "Компьютер, управляющий человеческим мозгом, поступает в продажу!"

    "{size=-6}{cps=43}Через четыре месяца все только и делали, что обсуждали грядущий выход первого массового компьютера, 
    работающего по этой новой технологии. Кто-то в страхе рассказывал каждому встречному, 
    что нельзя пользоваться новым изобретением, потому что оно наносит непоправимый вред организму, 
    кто-то воодушевленно рассуждал о перспективах, открывающихся благодаря транслированию сигнала прямо в мозг.{/cps}{/size}"

    "{size=-6}{cps=43}Но объединяло всех одно:{w} уже никто не оставался в стороне от обсуждения Neuroconnect.{/cps}{/size}"

    scene bus3:
        zoom 2.0
    with fade

    return