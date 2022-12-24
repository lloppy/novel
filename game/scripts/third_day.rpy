label third_day:
    scene home morning
    with fade
    
    play sound "music/music good.mp3" fadein fadein volume volume

    "Черт. Я снова отключил будильник…"

    # rewrite scene wakeup clock      СЦЕНА С БУДИЛЬНИКОМ

    "Чего?! Да я же опаздываю! Только получил свое место, а уже испытываю терпение начальства… 
    Если потороплюсь, возможно Карэн не сильно разозлится. Я же сам просил у Кая больше ответственности,
    и сам же всем своим видом показываю, что не готов к ней…"

    stop sound fadeout 3.0

    show bg ofis
    with dissolve

    "Ну разумеется, как всегда никого… Видимо, только я так безответственно отношусь к 
    предоставляемым компанией возможностям."
    
    "Что, я все-таки не один?"
    show elly smile
    show elly surprised

    g "Вы чего вы стоите? Забыли, где лифт? Бежим скорее!"
    show elly smile

    "Как скажете…"


    scene elevator outside
    with fade
    play sound "music/elevator.mp3" fadein fadein volume volume

    

    "Значит, в этом мире идеальных сотрудников все же есть такие как я, не способные просыпаться вовремя?"
    show elevator inside
    with dissolve

    show elly smile
    g "Ну почему же… Я очень даже способна проснуться вовремя, но я хватаюсь за столько утренних дел, что выйти вовремя не всегда получается… Извините, но мне пора бежать, хорошего вам дня!"
    show elly smile_ce
    hide elly
    with dissolve
    
    stop sound fadeout 4.0

    "Какая милая девушка, а я даже имя ее не спросил… Правда, сейчас беспокоить меня должно совсем не это, а реакция Карэн на мое опоздание."

    scene office
    with dissolve
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show karen
    "Привет, Карэн…"
    "Я все могу объяснить!"    
    
    show karen angry
    k "Ну попробуй."
    stop sound fadeout 2.0

    menu:
        "Признаться":
            $ soleCompany += 1
            jump third_day_say_true
            return
            
        "Соврать":
            jump third_day_say_false
            return

label third_day_say_true:
    scene office

    show karen angry

    "Если честно, я просто проспал… Понимаю, это очень безответственно с моей стороны, 
    но обещаю, такого больше не повторится! Со мной редко такое бывает, правда, не понимаю, 
    почему именно сегодня так получилось…"
            
    show karen
    k "Спасибо, что честно все сказал. Терпеть не могу, когда люди начинают выдавать 
    очевидную ложь за истину, лишь бы не впасть в немилость начальства."
    k "В этот раз выговоров не будет, но, пожалуйста, если вдруг ситуация повторится, 
    постарайся предупредить меня сразу, ведь мне нужно планировать работу отдела на день. 
    Можешь идти на свое место, Кай объяснит тебе, что было на пропущенном тобой дейли."

    scene office2
    with dissolve
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show kai
    kai "Да нет же, отдел тестирования ничего нам не присылал! Да, мы отправили свежую сборку вчера, 
    но они бы ничего и не сделали за день. А теперь вы звоните мне и требуете протестированный продукт, 
    когда заранее были совершенно другие сроки."
    kai "Какие? Как это какие? Мы же обсуждали, 
    что релиз переносится на два месяца. Не помните? Ну так перепроверьте, а затем обговорим еще раз."

    kai "Все, мне нужно идти. Напишите, как найдете договоренность о новых сроках."

    "Доброе утро, Кай."

    show kai serious
    kai "Доброе утро? Я бы сказал “добрый день”. Ты где пропадал?"
    stop sound fadeout 2.0


    "Извини, не спрашивай как, но я иногда отключаю по утрам будильники, и получаются такие вот ситуации. 
    Я уже поговорил с Карэн, так что пожалуйста, не нужно нравоучений еще и от тебя."

    show kai
    kai "Ладно, забыли. Сегодня важный день, а ты пропустил его очень важное начало. 
    Но тебе повезло, что есть я, который перескажет содержание дейли. Возможно, тебе кажется, 
    что такая большая компания занимается только AAA-проектами, но на самом деле время от времени 
    поступают заказы и на маленькие казуальные игры." 
    
    kai "На них выделяют одну-две команды, 
    и дают небольшой срок на создание. Сегодня как раз поступил заказ на ремейк одной старой игры, 
    в которой нужно птицами стрелять по свиньям."

    "Птицами по свиньям? Стрелять? Это очередная глупая шутка?"

    show kai serious
    kai "Никакая не шутка, я говорю совершенно серьезно."    
    show kai

    "Но это же какой-то бред. В этом и смысла то никакого, кто захочет в это играть?"

    kai "А вот тут ты ошибаешься. Во-первых, в этом есть смысл. Понимаешь, свиньи украли яйца у птиц. 
    Ясное дело, что они хотят вернуть яйца и отомстить зеленым вредителям. 
    А во-вторых, эта игра была невероятна популярна лет так 25 назад."

    "Чего-чего? Мне послышалось, или ты сказал “зеленые”. Я разных свиней видел, но чтобы зеленые…"

    show kai angry
    kai "Вот и чего ты придираешься? Нам не над смыслом надо рассуждать, а садиться и писать. 
    Между прочим, эта та возможность, о которой ты просил вчера. Ты наконец прикоснешься к внутреннему 
    устройству игры и поработаешь не только со мной."
    kai "А теперь отправляйся к Карэн, 
    она расскажет тебе о твоих задачах как программиста на сегодня."
    show kai

    scene office
    with dissolve
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show karen

    # rewrite  add choise at start        ТУТ ДОЛЖНО БЫТЬ ИМЯ ИГРОКА?
    k "О, <>, это снова ты."
    show karen say
    k "Я тебя заждалась. Уверена, ты, как первокурсник, уже знаком с основами программирования, 
    но я все же повторю специально для тебя основы, так тебе проще будет справиться со всеми сегодняшними задачами."
    show karen

    "Ничего себе, от прежнего холодного тона ни следа. Такая Карэн мне по душе!"
    
    show karen say
    k "В процессе создания любой игры разработчик использует константы. 
    Это значения, которые устанавливаются во время компиляции программы и не меняются. 
    Будем говорить о реализации на языке C#, так как именно его тебе нужно будет использовать в проекте."
    stop sound fadeout 2.0

    show karen
    k "Чтобы создать на этом языке константу, тебе нужно написать const, а затем указать тип данной переменной. 
    Если вдруг забыл, переменная - это своеобразный контейнер, используемый для хранения данных 
    и имеющий уникальное имя. Они бывают различных типов, и в языках со статической типизацией 
    ты должен явно это указывать, когда объявляешь переменную."

    show karen smile
    k "Для чисел ты чаще всего будешь использовать два типа данных:  int и double. 
    Первое - сокращение от integer, это тип используется для целых чисел, double, в свою очередь, 
    применяют, когда создают переменную для числа с плавающей точкой. Конечно, ты обязательно будешь работать с символами и строками. 
    Строки в языке C# обозначаются string." 
    
    show karen say  
    k "Главное, не забудь, что в переменную строки можно записать 
    только текст в двойных кавычках. Если используешь одинарные - создашь переменную типа char, 
    а это уже тип данных для символов. Любая string переменная состоит из char символов. 
    Для различных логических значений ты будешь использовать тип bool, который принимает значения true или false."

    "Извини, но не могла бы ты показать пример объявления переменной? У меня небольшой опыт работы с C#, а на слух воспринимать непросто."

    show karen smile
    k "Конечно, пройди к моему компьютеру."

    show karen at right

    show karen:
        zoom 1.25

    show office:
        zoom 1.55
    with dissolve


    show karen say 
    k "На самом деле, в большинстве случаев тебе совсем не нужно указывать тип данных. 
    Знаю, я только что говорила обратное, но дело в том, что в языке C# можно писать вместо типа данных 
    var, и тогда компилятор определит тип данных самостоятельно. Мы называем это “синтаксический сахар”."
    
    show karen
    k "Но будь осторожен! Чтобы не возникло неожиданных ошибок, всегда старайся использовать var с данными, 
    тип которых очевиден. Выглядеть это будет так: var name = “value”; - для строки, var number = 4; - 
    для целых чисел, var number = 4.3; - для чисел с плавающей точкой. Для констант это будет выглядеть 
    так: const int number = 3;." 
    
    show karen smile
    k "Точно, тебе пригодится возможность хранить ряд данных в одной переменной. 
    Тогда просто создай массив вот так: var arr = new int[[3] - для массива целых чисел длиной 3, 
    но аналогично и с другими типами данных. Чтобы добавить значение n-ному элементу массива используй: arr[[n] = 4;."

    "Про переменные все понял. А что кроме этого?"

    show karen say
    k "Кроме этого - оператор условия и циклы, без них у тебя при всем желании не получится написать игру. 
    Оператор условия в C# выглядит так: if (логическое выражение) {{блок кода, если условие истинно} 
    else {{блок кода, если условие ложно}."
    
    show karen
    k "С помощью оператора условия можно сделать ветвление в твоем коде, 
    но часто нужно обрабатывать не просто выбор между true и false, 
    но и выполнять операции с большим количеством повторений. Тогда на помощь приходят циклы."

    show karen say
    k "Цикл while используется для повторений до момента, пока некое условие истинно: while (условие) 
    {{блок кода}. Цикл for, в свою очередь, используют тогда, когда количество повторений заранее известно: 
    for (var i = 0;i < 5; i++) {{блок кода} - переменная i будет последовательно принимать целые значения от 0 включительно до 5 не включительно"
    
    k "То есть шаг будет 1, за это отвечает i++, что означает прибавить к i 1, разумеется, 
    все это можно изменять в зависимости от поставленной задачи."

    show karen smile
    k "Ну как, вспомнил основы программирования, или даже что-то новое узнал?"

    "В основном вспомнил, но многие особенности языка C# я не знал, так что спасибо тебе за лекцию."

    show karen
    k "Это еще не все. Не знаю, доводилось ли тебе раньше работать с системой контроля версий, 
    но в компании без этого никуда. Так что расскажу немного о Git. 
    Это система управления версиями с распределенной архитектурой, 
    позволяющая командам разработчиков создавать проект вместе и успешно синхронизировать все изменения, 
    а также разрешать конфликты в коде." 
    
    k "Для твоей работы хватит трех команд, репозиторий, 
    то есть папка с проектом, уже создана, ты просто должен будешь сохранять и отправлять все важные изменения. 
    Первая команда - git add. В цепочке команд она предписывает «сохранить» снимок текущего состояния проекта 
    в истории коммитов. Когда git add используется как отдельная команда, 
    она переносит ожидающие изменения из рабочего каталога в раздел проиндексированных файлов."

    show karen say
    k "Затем ты будешь использовать git commit. Она делает для проекта снимок текущего состояния изменений, 
    добавленных в раздел проиндексированных файлов. Такие подтвержденные снимки состояния можно 
    рассматривать как «безопасные» версии проекта — Git не будет их менять, 
    пока ты явным образом не попросишь об этом." 
    
    k "Ну и наконец команда git push. 
    Используется для выгрузки содержимого локального репозитория в удаленный репозиторий. 
    Она позволяет передать коммиты из локального репозитория в удаленный."

    show karen smile
    k "На этом у меня все. Теперь Кай добавит немного об оформлении игры, и ты можешь приступать. 
    Удачи тебе, если возникнут трудности, обращайся!"

    scene office
    with dissolve

    show kai smile

    kai "Ну, значит пришло время дать тебе последнюю часть информации перед проектом. Волнуешься?"

    "Ну, вы успели нагнать страха… Так что немного волнуюсь."

    kai "Да всё в порядке будет. Моя часть вообще очень простая, просто расскажу тебе, 
    как правильно сочетать цвета в игре. Ты должен понимать, что цвет играет огромную роль и влияет как на восприятие объектов, 
    так и на направление движения, настроение, физическое состояние да и много еще на что. 
    Он может помогать принимать решения и помогать игроку видеть влияние на мир игры."

    show kai 
    "Но давай более последовательно." 
    
    kai "Во-первых, у цвета функция ориентира. 
    Заметные цвета привлекают внимание игроков к объекту или предмету, скажем, 
    ярко-желтая линия посреди индустриального пейзажа точно будет заметной."

    kai "Во-вторых, цвета предупреждают. Шутеры, RPG, стелс-action, другие подобные жанры содержат много опасностей для персонажа. 
    Разработчик может предусмотреть цветовую индикацию опасности и спокойствия, что, несомненно, 
    улучшит пользовательский опыт." 
    
    kai "Цвет помогает развивать историю. 
    Изменение цвета часто применяют при показе флэшбеков, предысторий, воспоминаний. 
    Таким образом, основную историю отделяют от второстепенной, а игрок не путается с линиями повествования. "
    
    show kai smile
    kai "{size=-4}Наконец, можно использовать различные цвета при отрисовке персонажей, чтобы сделать акцент на каждом из них. 
    Например, твое будущее задание связано с Angry Birds. В этой игре каждая птичка имеет свой цвет, 
    что помогает герою быстро ориентироваться, кто из них бумеранг или бомбочка. 
    Вообще, работа с цветом в геймдеве - очень сложная и кропотливая. Поэтому нельзя сначала создать игру, 
    а затем уже обдумывать основную палитру.{/size}" 
    
    kai "Лучше всего, если в вашей команде изначально будет художник или дизайнер, 
    который займется разработкой визуальной составляющей одновременно с техническими работами."
    
    show kai
    kai "Проблемой могут стать невозможные цвета (или запретные цвета) — это те цвета, 
    которые из-за особенностей сетчатки человек не может воспринимать одновременно. 
    Невозможные цвета — это оттенки, которые похожи на оба цвета, например, «красно-зелёный» или «жёлто-голубой»."
    
    show kai smile_ce
    kai "Надеюсь, я тебя не перегрузил. А теперь можешь приступать к работе, надеюсь, у тебя все получится!"

    jump third_day_end



label third_day_say_false:
    scene office

    show karen angry

    "{size=-3}Понимаешь, я и правда поздновато сегодня встал, потому что живу один, и будить меня некому. 
    И чтобы прибыть вовремя, я решил сесть на автобус, хотя обычно хожу пешком. 
    Но недостаток сна сыграл свою роль, и я уснул прямо на сиденье автобуса. 
    Пока добирался обратно, уже и время много пролетело.{/size}" 
    
    "Извини, что так вышло, больше на автобусах я до офиса добираться не буду…"

    show karen sad
    k "Да, я все понимаю… И все-таки ты пропустил очень важное дейли, 
    а теперь некому и некогда рассказывать тебе о том, что сегодня нужно делать. 
    Единственный вариант - отправить тебя в отдел несколькими этажами ниже."

    show karen say
    k "У них есть очень удобный стенд, там и получишь всю нужную информацию. 
    На лифте доедешь до 93 этажа, а там разберешься сам. Хотя бы в лифте не усни."
    show karen

    scene elevator outside
    with fade

    scene elevator inside
    with dissolve

    "Может, не стоило ей врать? Выглядела она так, будто насквозь меня видела вместе со всем моим враньем. 
    А теперь вообще в другой  отдел отправила, неужели правда так занята, 
    что и нескольких минут на меня не выделить? Или все-таки зла из-за опоздания и лжи?"

    scene bg office
    with fade
    "Сколько же тут дверей. А Карэн говорила, что сам разберусь. И как же я это должен сделать?"

    "Кажется, у меня три варианта. Я заметил один незакрытый кабинет, в котором совсем никого нет. 
    Немного дальше по коридору девушка из лифта пытается что-то сделать с блоком своего компьютера, 
    ну а в конце коридора, видимо, то самое место, куда меня отправила Карэн."

    menu:
        "Зайти в пустой кабинет":
            $ detective += 1
            jump first_option_empty_office
        "Зайти в кабинет к девушке из лифта":
            $ loveLine += 1
            jump second_options_romantic_branch
        "Придерживаться изначальной цели":
            $ developer += 1
            jump third_option_no_action

    return

label first_option_empty_office:
    scene secret office empty
    with fade

    "В самом деле, это неплохая возможность узнать побольше скрытой информации о компании и ее проектах."

    scene secret office screen_with_word
    with dissolve

    "Сколько тут бумажек… Но почему они все какие-то странные? Ни одного понятного слова. Хотя нет, одно понятное есть."

    "“Сутки: Щиь щёвзкъ - жиьщыёзьчгуеёийу. Еь ыёщьзцб еавёдк. Шкыу ёийёзёюье.”"

    "Что это? Какой-то шифр? Как они вообще работают с зашифрованными файлами? 
    Что это за кабинет то такой…"

    scene secret office empty screen_on
    with dissolve

    "Кто-то идет. При чем со стороны кабинета, куда меня отправила Карэн. 
    Вдруг он зайдет прямо сюда? Иного выхода нет, нужно бежать обратно в свой отдел."

    $ detective += 1

    scene elevator outside
    with fade

    scene elevator inside
    with dissolve

    "Что я только что сделал… Ничего не узнал о том, что нужно разрабатывать, так еще и чуть не попался… 
    И как я буду сегодня работать? Карэн явно не собирается помогать, иначе бы не посылала сюда. 
    Кай? Может быть, но никаких гарантий…" 
    
    "Остается надеяться лишь на свои собственные силы."
    jump third_day_end

    return

label second_options_romantic_branch:
    scene bg office
    $ score[4] = True
    
    "Раз уж утром мне не удалось познакомиться с этой милой девушкой, то хотя бы сейчас я сделаю это. 
    К тому же, у меня есть чувство, что ей требуется моя помощь."

    scene elles office day:
        zoom 2.0
    with fade
    
    "Извини, что так без предупреждения, просто проходил по коридору и увидел, 
    что ты пытаешься что-то сделать с компьютером. Может тебе помочь?"

    show elly 
    with dissolve

    show elly angry

    g "Спасибо за беспокойство, конечно. Но я и сама как-нибудь могу…"

    show elly
    g "А впрочем, я потратила на это кучу времени и все равно ничего не получилось, 
    так что раз уж ты все равно тут, то попробуй что-то сделать с этим компьютером. 
    Сегодня утром он просто перестал работать."

    "Кажется, у видеокарты отошел разъем. Сейчас я вставлю его обратно, и все должно заработать."
    scene comp1:
        zoom 2.0
    with dissolve

    "Все как я и сказал, ничего серьезного."
    scene comp2:
        zoom 2.0
    with dissolve

    $ renpy.pause(1.5)

    scene elly office
    with dissolve
    g "Спасибо большое, сама я бы возилась еще неизвестно сколько. 
    Знаешь, я ведь довольно неплохой специалист, возможно скоро я даже получу повышение и отправлюсь в более серьезный отдел, 
    но я почти не разбираюсь в компьютерах и их внутренностях." 

    scene elly office angry
    g "Родители постоянно спрашивают, 
    как же я программирую то, устройство чего толком не знаю, а я отвечаю, 
    что сегодня совсем не обязательно знать все о компьютерах, чтобы создавать игры."

    "Кстати, получила выговор за утро? Моя тимлид оказалась весьма расстроена моим опозданием, 
    а я еще и умудрился наврать ей…"

    scene elly office smash
    g "Да нет, как я уже сказала, я на довольно хорошем счету в отделе, так что все давно привыкли к небольшим моим изъянам. 
    В конце концов, моя ценность для компании определяется объемом и качеством выполненной мною работы, 
    а я в конечном счете всегда со всем справляюсь." 
    
    scene elly office
    g "Возможно, если заслужишь доверие твоего тимлида, то она тоже станет более лояльна к тебе."
 
    scene elly office surprise
    with dissolve
    g "Как я могла забыть?! У меня же созвон прямо сейчас. Как вовремя включился компьютер! 
    Пожалуйста, оставь меня, я просто обязана присоединиться. Еще увидимся…"

    scene elly office smash
    "Ну, тогда удачной работы…"

    scene hall
    with fade

    "Я опять не спросил ее имя…"
    "Я надеюсь это не…"

    show message_from_karen
    with dissolve

    "Да как же мне не везет, я был уверен, что провел в кабинете не так уж много времени. 
    Но выбора у меня не остается, придется возвращаться…"

    scene office
    with fade

    "И снова мое желание помочь другим принесло мне одни проблемы. 
    Как я буду работать над проектом, если даже не выслушал, что должен сделать?"
    
    jump third_day_end
    return

label third_option_no_action:
    "Не могу я отвлекаться, рискуя не справится со своим первым крупным заданием. 
    Нужно идти прямиком в конец коридора."

    scene project office
    with fade
    # Большой кабинет наполняют несколько стажеров, собравшиеся у интерактивной доски.

    "Всем добрый день."
    $ renpy.pause(2.0)
    ". . ."

    "Ну ладно… Раз все тут такие…"

    scene project office board
    with dissolve

    show text "Ну, все наконец тут. Начнем. \nВсе, что нужно, чтобы справиться с сегодняшним проектом, я сейчас вам расскажу. \nСтарайтесь запомнить хоть что-то, и успешное выполнение вам практически гарантировано. В процессе создания любой игры разработчик использует константы.\nЭто значения, которые устанавливаются во время компиляции программы и не меняются. " at truecenter
    with dissolve
    pause 40.0
   
    show text text_desk_first at truecenter:
        zoom 0.93
    with dissolve
    pause 40.0

    show text text_desk_second at truecenter
    with dissolve
    pause 40.0

    show text text_desk_third at truecenter:
        zoom 0.85
    with dissolve
    pause 40.0

    show text text_desk_forth at truecenter:
        zoom 0.94
    with dissolve
    pause 40.0

    show text text_desk_fifth at truecenter:
        zoom 0.84
    with dissolve
    pause 40.0

    show text text_desk_sixth at truecenter:
        zoom 0.82
    with dissolve
    pause 40.0

    show text "Теперь приступайте к работе. Удачи." at truecenter
    with dissolve
    pause 4.0
    
    scene elevator outside
    with fade
    
    show elevator inside
    with dissolve
    "Столько информации… Не забыть бы ее, пока доберусь до места и начну работу. Надеюсь, в случае чего Кай и Карэн помогут мне, 
    в конце концов это же стажировка, а не полноценная работа."

    jump third_day_end
    return
