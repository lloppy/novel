label fourth_day_morning:
    scene home morning
    with fade
    play sound "music/music good.mp3" fadein fadein volume volume

    "Хотя бы сегодня я встал вовремя… Я даже успею проверить сообщения за ночь."

    show morning message
    with dissolve
    
    "Ого, и чего это Карэн понадобилось от меня в нерабочее время?"

    show morning message invite
    with dissolve
    
    "Вечер в компании Кая, Карэн и других? Звучит неплохо, но я пока не знаю наверняка, свободен ли вечером. Наверное, отвечу немного позже, когда точно буду уверен в том, чем займусь в завершение дня."
    stop sound fadeout 3.0

    scene street
    with fade

    if score[4]==True:
        show elly
        with dissolve

        "А не Элли ли это идет?"

        show elly smile_ce
        e "Утречка! Не ожидала встретить тебя по пути сюда, но я очень рада. Пойдем вместе?"

        "И тебе доброе утро. Ну раз уж нам в одно место, то конечно пойдем."

        show elly smile
        e "Слушай, <>, я долго тебя не видела у нас. Куда пропадал?"

        "Ну, я же в компании был всего лишь на стажировке. Но она была очень недолгой, 
        после проекта меня отправили домой - тренироваться в создании игр самостоятельно. 
        А вчера вот пришло приглашение на продолжение стажировки."

        show elly smirk
        e "Поздравляю! Это нужно отметить, давай сходим вечером в ресторан на крыше нашего здания. 
        Обещаю красивый вид и, возможно, интересный диалог."

        menu:
            "Прости, я уже договорился с ребятами из отдела":

                "Прости, я уже договорился с ребятами из отдела"
                $ soleCompany += 1

                show elly sad
                e "А, вот как получается… Ну ладно, не повезло мне быть первой получается. Что же, хорошо вам отдохнуть. 
                Знаешь, я вспомнила, что забыла заскочить перед работой в одно место. В общем, мне в другую сторону нужно, иди дальше один. До встречи."
            
                "Но Элли, подожди! Я совсем не хотел…"
                hide elly

                "Ну и зачем я так прямо… Теперь точно будет меня избегать. До работы еще есть время. Может в кофейню заскочить?"

                scene scenes cafee
                with fade

                show karen at right
                with dissolve

                show lloyd 
                with dissolve

                k "Ну-ка, давай еще раз про этот заговор."

                show lloyd smile_angry_wide_ce
                l "А чего ты в первый раз так плохо слушала? Говорю же, я, Эрнест, был уволен из игровой корпорации за то, что полез туда, 
                куда лезть не должен был. Я узнал слишком много!!! Я вообще каждый день жизнью рискую, рассказывая всем об этом тут. Понимаешь???" 
                
                l "Меня могут и убрать. Заговор. Их шпионы кругом. Живешь, работаешь, а потом бац - и твой лучший надежный друг уже и никакой не друг вовсе! 
                А корпораты не дремлют. Они ищут всех, кто хоть каплю их тайн узнал. Всего каплю, понимаешь?!
                И тут не одна компания замешана." 

                show lloyd furious                
                l "Десятки, сотни, быть может. А за всеми ними государство стоит, разумеется!"   

                show lloyd smile_wide

                show karen smile_ce_blush
                k "Ну, а за государствами рептилоиды стоят, не так ли?"
                show karen smile

                show lloyd smile_wide                

                l "Шути-шути. Когда станет не до шуток, уже никуда не убежать будет."
                show lloyd angry

                "Не смею прерывать ваш интеллектуальный диалог, но Карэн, не пора ли нам на работу? Кофе себе я уже взял."

                show karen smile_ce_blush
                show lloyd at left

                k "О, <>, приятная встреча! А я тут теорию господина Эрнеста выслушивала. Вернее, историю, никакую не теорию, прости за ошибочку, Эрнест."
                
                show lloyd surprise
                l " . . . "

                show karen smile
                k "В целом, я тоже готова идти. В путь!"

                scene street 
                with fade

                show karen say
                k "Знаешь, я ведь раньше была именно такой, какой кажусь незнакомцам."

                "Да, и какой же?"

                show karen
                k "Бесчеловечной. Строгой. Думающей только об успешном выполнении дедлайнов. Не способной разглядеть в подчиненных личности."

                "Я вовсе не считаю тебя такой. И при первой встрече не считал, разве что самую малость. 
                Но Кай с первых минут старался развеять такой твой образ в моей голове. Откуда в нем столько уважения к тебе?"

                show karen say
                k "Я не могу сказать точно про уважение Кая, но могу рассказать о событии, 
                которое изменило взгляды многих ребят из компании на работу и взаимодействие внутри коллектива."
                show karen 

                "Я очень хотел бы послушать."

                k "Хорошо. В общем, когда-то у нас в отделе работал один парень, имени называть не буду, даже не столько из-за секретности и чего-то такого, 
                сколько из-за эмоций, которые возвращаются, когда все снова прокручиваю в голове." 
                show karen say

                k "Тогда у компании были не самые лучшие времена, Кай только пришел к нам, и мы все старательно пытались пробиться на новый рынок. 
                Руководство доверило нам проект, от которого во многом зависело, будет ли старт на свежей платформе успешным. 
                Как это часто бывает в геймдеве, одни не до конца рассчитали необходимое на разработку время, другие криво распределили деньги и ресурсы." 
                show karen 
                
                k "Когда проект попал в наши руки - сроки и объем предстоящей работы уже были нереальными, никак не для небольшого отдела, 
                в котором половина работников были совсем новичками. Не знаю, был ли это вызов для нас, или так сложились обстоятельства, 
                но работать нам пришлось днями и ночами. Кранчи преследовали нас везде, от них мы просто не могли скрыться." 
                
                k "Тогда то один из нас и оказался крайним. Понимаешь, уставшие от нескончаемой работы люди всегда ищут, на ком им сорваться. 
                Очевидно, что срываться на руководство мы позволить себе не могли. Поэтому весь гнев, недовольство и вся злоба отдела легла на одного человека, 
                который совсем не был готов к такой непосильной ноше. Он не выдержал и одним декабрьским вечером покончил с собой." 
                show karen say
                
                k "Руководство, разумеется, все списало на несчастный случай, и всех проверок им удалось избежать. 
                Но ментальное здоровье команды не вернуть так просто, как замять “неприятную историю”. Каждый из нас считал себя виноватым, 
                но я тяжелее всех переживала эту потерю. Именно тогда я пообещала себе, что в моем отделе больше не будет места токсичности и выгораниям сотрудников." 
                show karen 
                
                k "С тех пор я готова отстоять любого, кто попал под мою опеку и кто также, как и я, ценит дружеское отношение между нами."

                "Даже представить не могу, как тяжело было вам всем… Знаешь, теперь я лучше понимаю, что имел в виду Кай."

                show karen smile_ce_blush
                k "Раз уж ты снова работаешь с нами, все правда были бы рады провести с тобой время вне стен корпорации. Надеюсь, вечером увидимся."
                jump fourth_day_office_morning
                return



            "Отличная идея":
                
                $ loveLine += 1

                show elly smile
                e "Правда? Я очень рада, что ты согласился."

                "Я не против узнать тебя получше. К тому же, уверен, что у тебя  можно перенять много опыта."

                show elly disbelief
                e "Так вот кого ты видишь во мне?"

                "Забудь, я просто не всегда четко выражаю то, что хочу сказать. Кстати, как прошел остаток вчерашнего дня?"

                show elly smile
                e "Все не так плохо. По крайней мере, меня не закидывали секретными разработками и запатентованными технологиями, 
                а к остальному я была готова. Не хочешь зайти в кофейню? До начала дня еще есть время."

                "Почему бы и нет."

                scene scenes cafee
                with fade

                show elly at right
                with dissolv

                show lloyd at left
                with dissolve

                e "Так значит, сегодня будет продолжение твоей стажировки. Сильно тебя нагружают?"

                "Не сказал бы, пока все было…"
                
                show lloyd smile_angry_wide_ce
                l "А вот и вы! Послушайте хоть вы меня! Я, Эрнест, был таким же белым воротничком." 
                
                l "Узнал слишком много! Слишком много узнал!"
                show lloyd furious
                l "Меня поймали, пока пытался узнать больше, чем следовало." 
                l "Реальность обманчива! Не верьте ничему и никому, если хотите остаться в живых." 
                show lloyd smile_angry_wide_ce

                l "Никто не верит, а вы поверьте!"

                "Ладно, достаточно. Твои бредни не интересны и до жути скучны, подходи, когда придумаешь что-нибудь более оригинальное. Элли, идем."

                scene street
                with fade

                show elly disbelief
                e "Тебе совсем не интересно, как он стал таким? Я бы не сказала, что он говорит самые банальные вещи для безумца. 
                Все-таки из них можно сложить какую-никакую картинку."

                "Неужели ты веришь, что хоть капля из его бредней может быть правдой? Он же явно не в себе."

                show elly
                e "Но судить людей лишь по первому впечатлению неправильно. Даже те, кого, как тебе кажется, ты хорошо знаешь, 
                могут быть совсем другими людьми глубоко внутри. Чего уж тут говорить о незнакомцах."

                "Я просто стараюсь не придавать лишний раз смысл тому, что скорее всего смысла не имеет. Слишком много фантазий можно создать, 
                размышляя над гипотетическими ситуациями. Я же привык оперировать фактами."

                show elly disbelief
                e "Мне кажется, ты слишком серьезно ко всему относишься. Мне просто было любопытно."

                "А вообще, тебе ли задавать вопросы о подозрительных вещах? В конце концов, это тебя перевели в отдел тайных разработок, 
                так что если кто-то из нас двоих и должен что-то знать, то это ты."

                show elly
                e "Я знаю не так много, как тебе кажется. Но даже это с тобой обсуждать не могу, прости уж меня… Но кажется, что мы пришли. Надеюсь, вечером увидимся."

                "Продуктивного дня, Элли."

                show elly smile_ce
                e "До скорого!"
                jump fourth_day_office_morning
                return


            "Прости, я не фанат людных мест":

                show elly sad
                e "Вот оно как… Жаль, я думала, ты будешь рад отметить. Ладно, тогда как-нибудь в другой раз, может будет более подходящий для тебя вариант. 
                Знаешь, я вспомнила, что мне еще нужно заскочить в одно место перед работой, так что иди дальше один."

                "Постой, все в порядке? Просто ощущение, что я огорчил тебя…"

                show elly 
                e "Что ты, вовсе нет… Правда, все хорошо. Ну, я побегу тогда. Пока-пока."

                "Снова все испортил…"
                jump fourth_day_office_morning
                return



label fourth_day_office_morning:
    # scene street
    # with dissolve
    # pause 1.0 
    
    scene bg ofis
    with dissolve
    pause 1.0 

    scene elevator outside
    with dissolve
    pause 1.0 

    scene elevator inside
    with dissolve
    pause 1.0 

    scene office
    with dissolve

    show kai smile
    kai "Доброе утро, проходи к своему рабочему месту, сейчас расскажу план на сегодня."

    "Без проблем."

    scene office2
    with dissolve

    show kai at left

    kai "Так вот. Не сказал бы, что на сегодня заготовлено много материала, но вот в его сложности относительно прошлого материала я уверен. 
    Придется действительно подумать, чтобы со всем справиться. Готов?"

    "Да, начинаем."

    kai "Итак, речь пойдет об алгоритмах. На алгоритмах построена не только любая игра, но и любая программа, уверен, ты это и без меня знаешь. 
    Существует много различных алгоритмов, и для поиска наиболее эффективного ты должен знать, когда какой тип можно и нужно применять. 
    Алгоритмы разделяют на 4 основных типа:"     
    kai "1 - линейный алгоритм, который описывает действие, которое будет выполняться много раз в определенном порядке;" 
    kai "2 - разветвляющийся алгоритм, определяющий несколько последовательностей действий в зависимости от каких-нибудь условий;"
    kai "3 - циклический алгоритм, который определяет действия, которые должны выполняться какое-то количество раз подряд, пока не закончится заданный порядок" 
    kai "И, наконец, вспомогательный алгоритм, определяющий действия, которые могут исполняться в других алгоритмах." 
    kai "Если переходить непосредственно к алгоритмам, то самые популярные из них это: сортировочные алгоритмы, среди которых выделяют 3 подвида - 
    сортировка слиянием, быстрая сортировка, пирамидальная сортировка." 
    kai "{size=-3}Данный вид алгоритмов эффективно используется искусственным интеллектом; преобразование Фурье, 
    в основном применяемое в вычислительных устройствах: компьютерах, смартфонах; алгоритм Дейкстры, 
    суть которого — поиск кратчайшего пути решения задачи. Это один из основных алгоритмов, по которым работает современный интернет; 
    RSA-алгоритм, применяющийся в программах, где существуют неочевидные решения.{/size}" 
    kai "Самый распространенный пример — это программы для шифрования данных; алгоритм безопасного хэширования. 
    Один из самый важных алгоритмов на сегодняшний день. Используется антивирусами, e-mail, интернет-магазинами, браузерами и т. д. 
    Основная его задача — безопасность в сети; алгоритм связей, ищущий связи между заданными элементами." 
    kai "Самый известный пример применения — это ранжирование страниц в поисковой системе или ранжирование новостей в соцсети или на новостной ленте" 
    kai "Дифференцирующий алгоритм. Часто такой алгоритм применяется в автоматизированных механизмах: 
    роботах, станках, автомобилях, самолетах; алгоритм сжатия данных; алгоритм случайных чисел."
    kai "А теперь запиши названия алгоритмов, которые неплохо было бы изучить в свободное время, чтобы быстро находить эффективные решения для твоих проектов. 
    Это такие алгоритмы, как:"

    scene office computer
    show text "•Алгоритм бинарного поиска \n •Алгоритм поиска в ширину (BFS) \n •Алгоритм поиска в глубину (DFS) \n •Сортировка вставками, Сортировка выбором, Сортировка слиянием, \n Быстрая сортировка, Сортировка подсчетом, Сортировка кучей\n •Алгоритм Крускала\n •Алгоритм Флойда Уоршелла\n •Алгоритм Дейкстры\n •Алгоритм Беллмана Форда\n •Алгоритм Кадане\n •Алгоритм Ли\n •Алгоритм заливки \n •Алгоритм обнаружения цикла Флойда\n•Топологическая сортировка в DAG \n •Алгоритм поиска союза \n \n \n \n \n \n \n"
    with dissolve   
    pause 40.0

    "Я должен знать все эти алгоритмы наизусть?"

    scene office2
    with dissolve

    show kai smile
    kai "Нет, вовсе не обязательно. Главное, ты должен примерно понимать, когда нужно использовать тот или иной алгоритм, и примерно представлять себе его реализацию. Так что мучиться и заучивать нет никакого смысла."
    
    "Спасибо, я уже начал было волноваться, потому что все-таки их очень много."
    
    show kai ce
    # kai "Ничего, постепенно все освоишь. Ну а теперь время для теста по пройденному материалу. Тебе нужно соотнести тип алгоритма, его описание и схему. Уверен, ты справишься."
    kai "Ты молодец, не все способны с ходу понять эту тему, но у тебя получилось."

    show kai 
    kai "Ну вот и конец дня близится. Слышал, Карэн пригласила тебя на сегодняшний вечер. Что ты решил в итоге?"
    menu:
        "Я хочу провести вечер с командой":
            $ soleCompany += 1
            jump day_with_command
        "Я хочу еще немного поработать":
            jump day_with_job
        "Я слишком устал, время отправиться домой":
            jump day_along

        "Я хочу провести вечер с Элли" if score[4] == True:
            $ loveLine += 1
            jump day_with_elly
    return



label day_with_command:
    show kai ce
    kai "Знал, что ты захочешь провести с нами время! Тогда собирайся, через несколько минут выдвигаемся в кафе недалеко от офиса."

    scene roof cafe view evening
    with fade
    pause 1.0

    scene roof cafe evening
    with dissolve
    pause 1.0

    show karen at right
    with dissolve

    show kai at left
    with dissolve

    k "Итак, я надеюсь, все знают, по какому поводу мы сегодня собрались. В нашу команду возвращается <>, и, как мне кажется, 
    пришло время встретить его не только как работника нашей компании, но и как личность, часть отдела, как нашего друга, наконец."

    kai "Пусть пока мы и не провели много времени вместе, но ты уже кажешься нам своим. Все беспокоятся о том, как ты себя чувствуешь у нас, насколько тебе комфортно обучаться."

    menu:
        "Мне готовы прийти на помощь, поэтому даже трудные задачи оказываются мне под силу":
            "Мне готовы прийти на помощь, поэтому даже трудные задачи оказываются мне под силу"
            show kai smile
            kai "Рад это слышать. Именно такую атмосферу внутри команды мы стараемся сохранять. "

        "Бывают непростые моменты, но в целом меня все устраивает":
            "Бывают непростые моменты, но в целом меня все устраивает"
            show kai ce
            kai "Не стесняйся просить у других помощи. Конечно, мы можем быть очень заняты, но мы правда стараемся не бросать друг друга в беде."

    "Знаю, что несмотря на всю престижность в наши дни работы в геймдеве, вы наверняка часто сталкиваетесь с выгораниями?"

    show karen say
    k "Не без этого, конечно. Хотя в офисе и созданы все условия для отдыха, но иногда времени на это просто не бывает. Так что переработки случаются, нужно быть к этому готовым."
    
    show kai 
    kai "Но знаешь, если ты действительно чувствуешь в себе желание творить и создавать игры, то ощущение от завершения проекта перекрывает все потраченные нервы и часы неустанной работы."

    show karen 
    k "Согласна, ничто не сравнится с этими эмоциями. Для меня так точно."

    show kai smile_ce
    kai "Ладно, выпьем за нашего стажера, и за его будущее, надеюсь, что в нашем отделе!"

    k smile_ce_blush "Выпьем!"

    "Да чего вы, ребят…"

    scene roof cafe view evening
    with dissolve
    pause 1.0

    scene roof cafe view night
    with fade
    pause 1.0

    scene roof cafe night
    with dissolve
    pause 1.0

    show kai at left
    show karen  
    show lloyd smile_angry_wide_ce at right

    kai "…я говорю: “До ближайшего дедлайна 30 минут. Если не можешь делать из багов фичи, значит тебе крышка!” И тут вдруг отовсюду тикеты как повыскакивают, а у меня из устройств один ноутбук. Но делать то нечего… Надо фиксить!"

    ar "Извините, что прерываю. Я Арон, работал раньше в игровой корпорации. Я вас знаю, вы тоже в одном из отделов игры делаете. Что, еще не вскрылась всем правда то? Про государственное финансирование правда то? Нет? Я вот все знаю, все знаю,  за то меня и уволили. Слишком много знал! Ой как много!"

    kai @ angry "Кто пустил его в кафе!? Охрана, выведите этого безумца, пожалуйста. Неужели никто ничего не может с ним сделать? Изо дня в день он донимает людей в этой районе, но никто так и не может привлечь его к ответственности?"
    
    k @ say "Чего завелся то так? Может, и прав он… Я не много об этом слышала, но все-таки слухов об этом среди руководителей среднего звена много, а потом очень уж все похоже на правду. Приходят наверх большие контракты от правительства. На что - никто сказать не может."
    
    kai @ angry "Карэн, ты! Тебе не кажется, что распускать слухи среди подчиненных - не лучшая идея? К тому же такие, которые вполне за какое-то обвинение принять можно."

    k @ say "А чего ты вдруг так стал беспокоиться об этом? Просто сплетничаю в кругу близких знакомых, разве это так уж плохо?"
        
    kai @ serious "Мне кажется, достаточно тебе на сегодня выпивки. Давай я отвезу тебя домой."

    k "Да совсем я еще не…"

    show kai smile
    kai "Мы поехали. Увидимся завтра."

    "Пока…"


    scene roof cafe view night
    with fade

    "И чего это он так распереживался? Словно Карэн ляпнула действительно что-то важное, что-то, 
    что остальные знать не должны. Но почему Кай? Он вообще подчиненный Карэн, да и сам же в конце концов ей восхищался, 
    а сейчас вел себя с ней совсем по-другому. Нужно попытаться понять, что он не договаривает."
    return

label day_with_elly:
    show kai
    kai @ serious "Элли? Кто это?"

    "Ну, одна моя знакомая из другого отдела. Мы договорились с ней о встрече еще днем, так что…"

    kai @ sad "Печально конечно, все хотели провести с тобой время за стенами офиса, чтобы получше тебя узнать, но если ты уже договорился, то ничего не поделать. Тогда приятного вечера, мы с ребятами уходим."

    "Да, тогда я тоже буду собираться. И вам хорошо провести время."
 
    scene roof cafe evening
    with fade
    pause 1.0

    scene roof cafe view evening
    with dissolve
    pause 1.0
    play sound "music/music good.mp3" fadein fadein volume volume

    "Элли была права… Вид отсюда и без того шикарный, но ночью все кажется еще более завораживающим."

    show elly
    with dissolve

    e smile "Еще бы! Это одно из моих любимых мест в городе… Я заняла нам столик, пойдем?"

    "Не пугай меня так, я не ожидал такого резкого появления. Конечно, пойдем."

    scene roof cafe evening
    with fade

    show elly smirk

    "Тебе нравится эта работа? Все вокруг только и мечтают, что стать работником геймдева. Но они и отдаленно не представляют, что работа тут не отдых и не миллионы в секунду за прохождение игр."
    
    e @ disbelief "Знаешь, на самом деле и ни разу не пожалела, что выбрала этот путь. Когда я еще училась в школе, и настало время определяться, 
    кем я хочу стать, я долго не могла решить. Родители, пользуясь моей нерешительностью, настаивали на том, 
    чтобы я стала государственным деятелем." 
    e @ angry "Они видели во мне человека, который прославит нашу фамилию, человека, который обретет власть, 
    которая и не снилась моему отцу. Я долго готовилась к поступлению, заучивала варианты и верила, 
    что это желание - мое, а не чье-либо еще." 
    e @ sad "Я поступила. Родители были вне себя от радости, 
    а я не могла выйти из оцепенения от ощущения бесполезности всех моих усилий."

    "И как же ты начала делать игры?"

    e disbelief "К середине первого курса, я поняла, что больше не вынесу этого. И примерно тогда же я всерьез заинтересовалась геймдевом. 
    Когда объявила родителям, что бросаю учебу и начинаю делать игры, был большой скандал. 
    Все их надежды рушились, а я впервые ощущала, что поступаю так, как хочу сама." 
    
    e smile "Меня приютила подруга, и все мое обучение началось с нуля, но на этот раз я жила тем, чем занималась, поэтому трудности и препятствия казались преодолимыми."

    "Вот значит каков твой путь сюда. Наверное тебе было очень тяжело от ощущения, что родители бросили тебя."

    e @ smile_ce "Это то, что мне пришлось перерасти. Но благодаря этому же я стала самостоятельной. Так что я не соврала, сказав, что ни о чем не жалею. А как ты попал к нам?"

    "Можно сказать, я чем-то похож на тебя. Я тоже долго не мог понять, чем хочу заниматься. 
    Но мою судьбу больше определил случай, когда я решил подать заявку на стажировку." 
    
    "Представь себе, как я удивился, когда получил приглашение. В первый день переживал, смогу ли стать частью этой индустрии, 
    получится ли у меня заинтересовать руководство и быть полезным. Но я встретил тут много открытых людей, 
    которые переживают за мою судьбу, поэтому я счастлив учиться и работать в этой компании."
    stop sound fadeout 3.0

    scene roof cafe view evening
    with dissolve
    pause 1.0

    scene black
    with dissolve
    pause 1.0   

    scene roof cafe view night
    with fade
    pause 1.0

    scene roof cafe night
    with dissolve
    pause 1.0

    show elly smirk
    play sound "music/music good.mp3" fadein fadein volume volume

    "Спасибо, что показала это место в такое время. Было приятно узнать тебя получше, да еще и наслаждаясь таким видом на ночной город."

    e @ smile "Я тоже рада, что ты согласился провести вечер вместе…"
    
    "Уже поздно, наверное пора отправляться по домам?"

    e "И правда, не заметила, как пролетело время. Вызови лифт, пожалуйста."
    stop sound fadeout 3.0


    scene elevator outside
    with dissolve
    pause 1.0

    scene elevator inside 
    with dissolve
    pause 1.0

    show elly
    if (loveLine == 4):
        "Подожди, но мы же собирались на первый этаж, выходить из офиса. Почему ты нажала кнопку с номером этажа твоего нового отдела?"
        
        e "<>, сегодня я поняла, что могу доверять тебе. Меня долго мучили сомнения, но теперь я уверена, что показать тебе то, что я нашла, не будет ошибкой."

        "Нашла? В новом отделе, где не на каждом файле гриф секретности? И ты уверена, что я должен это видеть?"

        e "Тебя наверняка пугали сказками про корпоративную тайну. Знаю наверняка, потому что и сама все это выслушала. Но все зашло куда дальше, чем просто дорогие игры, слитая информация о которых может дорого стоить. Теперь просто дождись и пока не задавай вопросов."

        "Пока у меня нет ничего, кроме вопросов, но если ты просишь, то я отложу их на какое-то время."

        scene secret floor
        with dissolve
        pause 1.0

        show secret office empty
        with dissolve
        pause 1.0

        show secret office empty screen_on
        with dissolve
        pause 1.0

        scene elly office angry 
        e "А теперь смотри: они довольно хорошо спрятаны, но при желании можно раскопать все данные. Тут десятки госконтрактов на создание игр. С каких пор государство интересуется созданием игр? И почему вся эта информация засекречена?"

        "Может, они не хотят раскрывать сумму? "

        scene elly office  
        e "Я рассматривала все варианты, связанные с деньгами. Думала даже об отмывании, но все равно не сходится. Тут явно что-то более серьезное."

        "Что может быть серьезнее отмывания денег?"

        scene elly office angry 
        e "Я не знаю! Понимаешь? Я правда не знаю, поэтому я и искала кого-то, с кем смогу поделиться. Но что-то нужно сделать. Чему я научилась за полгода своего обучения государственному делу, так это тому, что за засекреченной информацией часто стоят не самые добрые помыслы."

        "В таком случае, я хочу помочь тебе. Мы должны разобраться, но для этого никто не должен нас раскрыть. Ты должна быть очень аккуратна, чтобы мы не потеряли возможность изучать местные файлы."

        e "Хорошо. Тогда давай встретимся завтра, и в спокойной обстановке обсудим план действий. Боюсь, что сейчас мы ничего толкового не придумаем."

        "Хорошо, тогда завтра мы начнем наше расследование."

    else:
        play sound "music/music good.mp3" fadein fadein volume volume

        scene night town
        with dissolve

        show elly 
    
        "Ну вот и твое такси."

        e disbelief "Уверен, что не поедешь тоже? Нам в одну сторону, можно было бы попросить остановиться рядом с твоим домом."

        "Не стоит, правда. Хочу немного прогуляться, погода прекрасная."

        e smile "Как знаешь. Спасибо за вечер еще раз. Увидимся."

        "Хорошей дороги и спокойной ночи."

        "А мне нужно вернуться в отдел…"
        stop sound fadeout 3.0


        jump secrect_label

    return  


label day_with_job:
    show kai 
    kai @ surprise "Поработать? Как скажешь. Ты меня даже немного удивил. Не каждый день увидишь кого-то, добровольно меняющего отдых на работу."

    "Просто сейчас такое время, когда мне стоит больше времени уделять обучению."

    kai smile "Дело твое. Ну, хорошего вечера тогда, мы ушли в кафе."

    "Да, удачно вам посидеть."

    "Как только все уйдут, я смогу исследовать корпоративную сеть и наконец узнать, какие секреты хранит в себе компания."

    jump secrect_label

    return


label day_along:
    show kai 
    kai @ surprise "Уже? Еще весь вечер впереди же. Но дело твое, если устал, то отдых дома и правда лучший вариант."

    "Да, я пойду наверное. Хорошо вам провести время."

    show kai smile
    kai "Отдыхай, увидимся завтра."

    scene black:
        zoom 2.0
    with dissolve

    scene night town
    with dissolve
    play sound "music/music good.mp3" fadein fadein volume volume


    "Как-то одиноко… Зайти что-ли в кафе на крыше?"
    scene roof cafe night
    with dissolve
    pause 1.0

    scene roof cafe view night
    with fade
    pause 1.0

    "И почему я всегда отказываюсь от предложений провести время с кем-то? Почему я так люблю одиночество, 
    если в конечном счете оно приносит лишь боль? Моя зона комфорта - мое главное проклятие."

    "В зависимости от того, смогу ли я из нее выйти, будет зависеть все мое будущее. Ведь нельзя постоянно сторониться людей. 
    Жить - значит доверять другим. Но чтобы начать доверять, было бы неплохо хотя бы просто узнать кого-нибудь получше."

    show lloyd at right
    ar "Добрый вечер. Извините, что прерываю явно глубокие размышления, но позвольте представиться: Арон."

    stop sound fadeout 3.0

    if (see_lloyd == True):
        "Арон? Но я уверен, что тебя не так зовут."

        show lloyd smile_wide_ce
        ar "Очень даже так! Как же иначе меня могут звать?"
        show lloyd

    show lloyd at center
    with dissolve
    ar @ ce"Я работал в игровой корпорации больше десяти лет."

    "Да-да, а еще ты раскрыл заговор, и за это тебя уволили. Если хочешь рассказать что-нибудь полезное, то давай. А иначе оставь меня в покое, у меня ужасное настроение."

    ar @ surprise "Вижу, вы не очень настроены на разговор. Но я вот вам что поведаю: я своими глазами видел контракты корпорации с государством. Через подставные фирмы чиновники переводят миллионы на их счета, взамен корпорации обязуются создавать игры по их заказу. Что это за игры - никто не знает."

    "Ты же понимаешь, насколько глупо звучат твои слова? Зачем им нужны игры? И зачем это скрывать? У тебя хоть какие-то доказательства то есть?"

    ar @ angry "Вы думаете, что с доказательствами на руках я бы еще оставался жив?"

    "Тогда я больше не желаю это выслушивать. Всего хорошего."

    scene night town 
    with dissolve

    "И все-таки. Такое явно не выдумать на пустом месте. Даже если считать, что он насочинял большую часть своего рассказа, то вопросы все равно остаются. Если бы я только мог узнать больше. Но я смогу поверить только своим глазам. Нельзя доверять чьим-либо словам. Если вдруг вся секретность корпорации хоть сколько-нибудь несет опасность, я могу стать первым кандидатом на вылет за свое любопытство."

    return


label secrect_label:
    scene night office off
    with dissolve
    pause 1.0 

    scene night office _on
    with dissolve
    pause 1.0 

    "Уверен, что большинство файлов будут зашифрованы, но может быть что-то раскопать у меня все-таки получится."

    "Кажется, что-то есть. Точно, какие-то счета. Указаны как счета заказчика, но сумма просто поражает. Не думал, что у кого-то есть столько денег, которые к тому же он готов отдать на разработку игры. Нужно узнать, кому принадлежит счет."

    "Судя по всему, это оформленные через подставные фонды счета крупнейших политических деятелей страны. 
    Но что им понадобилось от нашей компании? Игры? И для этого рисковать и переводить деньги через офшоры?"
    
    "Я должен узнать больше, но что, если меня обнаружат?"
    
    "Наверняка тут полно систем контроля, если даже правительство доверяет корпорации. 
    Мне нужно срочно закрыть все и тщательно обдумать найденное незамутненным сознанием, завтра. 
    А сейчас нужно бежать домой, пока никто меня не поймал."

    return