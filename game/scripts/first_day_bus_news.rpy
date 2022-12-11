label first_day_bus_news:
    scene bus3:
        zoom 2.0
    with dissolve

    """{cps=43}Прошло уже несколько дней, а я все никак не осознаю произошедшее.
    {w}Только заметив новое уведомление, я сразу принял сообщение за спам.
    Но как и любой человеческий интерес, мое желание ознакомиться с содержимым перевесило 
    возможное раздражение от еще одной впустую потраченной минуты.
    Тогда я инстинктивно нажал на экран смартфона и принялся читать...{/cps}

    {cps=43}Уже с первых строк стало понятно, что чутье меня подвело 
    (что случается довольно часто, так что удивлен я совсем не был), 
    и написанное вовсе не является спамом. Собеседник представился HR менеджером компании, 
    занимающейся коммерческой разработкой игр.{/cps}"""

    scene bus2:
        zoom 2.0
    """{cps=43}Сообщение было большое, так что все его  
    вспомнить не могу, но вот его суть я вряд ли смогу забыть:{w} меня позвали на стажировку 
    на должность разработчика в одну из студий корпорации. Первый возникший в голове вопрос 
    - где они меня нашли?{/cps}
    
    {cps=43}Помню, что в начале года разослал десяток заявок по разным компаниям, 
    но я и представить не мог, что хоть кто-то из них откликнется и рассмотрит мою кандидатуру. 
    Да и времени с тех пор столько прошло..{/cps}
    
    {cps=43}Но почему они выбрали именно меня?{/cps}"""
    
    scene bus1:
        zoom 2.0
    """{size=-3}{cps=43}Говоря начистоту, я никак не могу назвать свои способности выдающимися. Я не обрел популярность за первый 
    (и пока мой единственный) год обучения в университете, не одарен творческим талантом, 
    не люблю брать на себя ответственность и ненавижу соблюдать дедлайны, что выливается 
    в мои постоянные долги по тем предметам, где для успешного выполнения работы нужно 
    кропотливо уделять задаче кусочек каждого своего дня.{/cps}{/size}
    
    {cps=43}Одним словом, я всегда балансировал 
    между понятиями “перспективный разработчик” и “бездарный кодер, будущее которого 
    весьма и весьма смутно”.{/cps}

    {cps=43}Но даже если поверить в свою удачу и принять тот факт, 
    что огромная корпорация действительно заинтересовалась первокурсником, во мне остается
    куча переживаний о самой стажировке.{/cps}"""
    
    scene bus3:
        zoom 2.0
    """{cps=43}Еще во время учебного года мой одногруппник, 
    победитель региональных олимпиад по программированию и начинающий разработчик игр, 
    тоже был приглашен в большую компанию, где проходил стажировку несколько недель.{/cps}
    
    {cps=43}Но даже его опыта не хватило, чтобы впечатлить руководство и заполучить должность.{w}
    На что же надеяться мне?{w} Конечно, у меня есть некоторый опыт программирования, 
    в этом году я даже был частью команды, отвечающей за разработку университетского 
    сервиса для работы с абитуриентами. Вот только никакого опыта создания игр у меня нет.{/cps}
    
    {cps=43}Можно сколько угодно смотреть видео по геймдизайну, слушать подкасты и изучать механики 
    в полюбившихся мне играх. Но пока за моей душой нет ни строчки кода игры,{i} разве я могу
    быть уверен, что это мое?{w} Могу ли с уверенностью идти на стажировку, зная, что не облажаюсь?{/i}{/cps}"""
     
    scene bus2:
        zoom 2.0
    """{cps=43}Мысли о провале настолько поглотили меня, что я совсем забыл хоть немного изучить компанию, 
    в которой собираюсь постигать основы разработки игр. А ведь они вполне могут захотеть проверить 
    мои знания об индустрии, и это еще одна возможность показать себя с худшей стороны.{/cps}

    {cps=43}Кажется, я могу успеть освежить в своей памяти, 
    как игровые корпорации стали одной из самых влиятельных частей экономики.{/cps}"""

    jump news
    return



label end_bus:
   
    scene black with circlewipe

    "{cps=43}Еле успел выскочить… Ну, вперед, в счастливое будущее!{/cps}"
    jump first_day_moring
    return




    
    
    
