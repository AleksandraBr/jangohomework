from symbol import return_stmt

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html')


# Create your views here.
signs = {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'}

objects_array = [
{"id": 1,
"title": "Меркурий",
"info": "Самая близкая к Солнцу и самая маленькая планета солнечной системы",
"all_info": "Меркурий получает в семь раз больше тепла и света, чем Земля, поэтому температура его поверхности колеблется от +430°C днём до −190°C ночью. Это самый большой температурный перепад в солнечной системе. Атмосфера практически отсутствует — возможно, причиной тому солнечное излучение, а может быть, небесное тело такого размера просто не в состоянии удерживать плотную газовую оболочку. ",
"img": "https://i.pinimg.com/736x/c4/89/7a/c4897a21988a66ebe9d6740b5a540bf7.jpg"},

{"id": 2,
"title": "Венера",
"info": "Венера — вторая планета от Солнца и ближайшая к Земле. Венеру иногда называют «близнецом» нашей планеты: её размеры и масса очень близки к земным. ",
"all_info": "Венера окутана очень плотным слоем облаков, за которыми невозможно разглядеть поверхность. Из-за парникового эффекта она нагревается до 480°C — абсолютный рекорд для солнечной системы. Облака проливаются кислотными дождями и пропускают только 40% солнечного света, поэтому на планете царит вечный сумрак. Из-за сильнейшего атмосферного давления (как на глубине 900 метров в земных океанах) ни один исследовательский аппарат, отправленный на Венеру, не просуществовал дольше двух часов. Тем не менее учёным удалось узнать, что атмосфера планеты на 94% состоит из углекислого газа, а состав грунта не отличается от других планет земной группы. На Венере много вулканов, но почти нет кратеров — все метеориты сгорают в плотной атмосфере.",
"img": "https://avatars.dzeninfra.ru/get-zen_doc/5241527/pub_60f92c16bbe8c109b047c929_60f92fef97e0ae33695c4f32/scale_1200"},

{"id": 3,
"title": "Земля",
"info": "Земля — третья планета от Солнца и крупнейшая в земной группе. Уникальные условия Земли позволили развиться на планете жизни.",
"all_info": "70% поверхности Земли покрыты водой. В отличие от Луны и Меркурия, на Земле очень мало кратеров. Учёные считают, что они исчезли под воздействием ветра и эрозии почвы. Из-за наклона Земной оси (23,45°) на Земле хорошо различимы сезоны года. Для оборота вокруг своей оси Земле требуется чуть менее 24 часов — это самый короткий день среди планет земной группы.",
"img": "https://cdn.culture.ru/images/0ce556b1-e072-5210-a7f1-cf6b932b60ad"},

{"id": 4,
"title": "Марс",
"info": "Марс — четвертая планета от Солнца — меньше Земли почти в два раза. ",
"all_info": "Долгое время считалось, что на красной планете существует жизнь. Люди наблюдали на его поверхности объекты, казавшиеся им постройками, дорогами и даже гигантскими скульптурами. Однако на поверку марсианская цивилизация оказалась обманом зрения. Многочисленные исследовательские миссии пока тоже не подтвердили наличие какой-либо жизни на поверхности планеты.",
"img": "https://avatars.mds.yandex.net/i?id=7630b1155a7e6e38909646f054de93a7_l-9266849-images-thumbs&ref=rim&n=13&w=1600&h=1200"},

{"id": 5,
"title": "Юпитер",
"info": "Юпитер, самая большая из планет-гигантов. ",
"all_info": "Масса Юпитера в два раза больше, чем масса всех остальных планет, лун, комет и астероидов системы вместе взятых. По яркости на земном небе он уступает только Венере. Люди наблюдали его с древнейших времён и связывали с сильнейшими богами своих пантеонов. Юпитер — имя римского царя богов. ",
"img": "https://avatars.dzeninfra.ru/get-zen_doc/5286086/pub_610698b39bd3fc59f0b72372_610698e9b4685518d3730986/scale_1200"},

{"id": 6,
"title": "Сатурн",
"info": "Шестая планета от Солнца. На сегодняшний день эта планета остаётся одной из наименее изученных. ",
"all_info": "Главная особенность Сатурна — впечатляющая система из семи колец. Они состоят из миллиардов ледяных осколков, которые отлично отражают свет, а потому хорошо заметны. Радиус колец огромен — 73 000 километров, а толщина — всего 1 километр. Считается, что эти кольца — осколки спутника, разрушенного гравитацией планеты.",
"img": "https://upload.wikimedia.org/wikipedia/commons/2/25/Saturn_PIA06077.jpg"},

{"id": 7,
"title": "Уран",
"info": "Уран был открыт сравнительно недавно — в 1781 году. В 1986 году его достиг единственный космический аппарат — «Вояджер-2». ",
"all_info": "Атмосфера планеты окрашена в однородный сине-зелёный цвет. Учёные предполагают, что такой её делает метан. Ядра Урана и Нептуна предположительно состоят изо льдов, поэтому их называют «ледяными гигантами». Уран — самая холодная планета в системе: средняя температура его поверхности составляет −224°C. Скорость ветра на Уране достигает 900 км/ч. Солнечный свет летит до Урана чуть менее трёх часов, а год на планете равен 84 земным. ",
"img": "https://naked-science.ru/wp-content/uploads/2016/10/field_image_uran-kosmos.jpg"},

{"id": 8,
"title": "Нептун",
"info": "Нептун находится так далеко, что его нельзя увидеть с Земли невооружённым глазом. ",
"all_info": "Раз в несколько лет в атмосфере планеты появляются и исчезают тёмные пятна штормов. Предположительно в центре Нептуна — ледяное ядро, а мантия состоит из жидкой смеси воды и аммиака. Средняя температура поверхности — −214°С. ",
"img": "https://i.pinimg.com/736x/4b/b5/32/4bb532a69ed674f5c10f2b25a0c5f15e.jpg"},
]

data=[
{"ФИО": "Бурлуцкая Александра Евгеньевна",
"Фото": "https://i.pinimg.com/originals/e8/8f/30/e88f3028afe762960b7a2c11837b34d1.jpg",
"Почта": "aeburlutskaya@edu.hse.ru",
"Телефон": "+79876789343"},

{"ФИО": "Петров Петр Петрович",
"Фото": "https://i.pinimg.com/736x/9c/da/09/9cda09354396590f3e18460d40e8b347.jpg",
"Почта": "lhhhncsakd@mail.ru",
"Телефон": "None"},

{"ФИО": "Иванов Иван Иванович",
"Фото": "https://i.pinimg.com/736x/79/31/74/793174f1ac03568631148f08d0ac58aa.jpg",
"Почта": "ckanhksnckj@mail.ru",
"Телефон": "None"},

{"ФИО": "Сергеев Сергей Сергеевич",
"Фото": "https://lastfm.freetls.fastly.net/i/u/ar0/97b81e650d45b46be60bd4d9416ba216.png",
"Почта": "ksahjhcfl@mail.ru",
"Телефон": "+7237654638"},

{"ФИО": "Васильев Василий Васильевич",
"Фото": "https://i.pinimg.com/736x/85/cf/59/85cf59e7734c98a95767cdd23d5528be.jpg",
"Почта": "jaklhxdklk@mail.ru",
"Телефон": "+79876543"}
]

def get_sign_info(request, sign:str):
    return HttpResponse(signs.get(sign, f'Знак зодиака {sign} не обнаружен'))

def get_sign_info_by_num(request, sign: int):
    if 0 < sign < len(signs):
        cur_sign = list(signs)[sign-1]
        return HttpResponse(f'{signs[cur_sign]}')
    return HttpResponse(signs.get(sign, f'Знак зодиака {sign} не обнаружен'))

def signs_2(request, sign: str):
    data = {'signs': signs.get(sign, f'Знак зодиака {sign} не обнаружен')}
    #data = {'signs': signs}
    return render(request, 'signs_3.html', context=data)

def signs_3(request):
    #data = {'signs': signs.get(sign, f'Знак зодиака {sign} не обнаружен')}
    data = {'signs': signs.keys()}
    return render(request, 'signs_3.html', context=data)

def get_sign_one(request, sign: int):
    if 0 < sign < len(objects_array)+1:
        error = ''
        cur_sign = objects_array[sign-1]
        context = {'cur_sign': cur_sign, 'error': error}
        return render(request, 'show1.html', context)
    else:
        error = 'Такого знака нет :('
        context = {'error': error}
        return render(request, 'show1.html', context)

def show_all(request):
    #data = {'signs': signs.get(sign, f'Знак зодиака {sign} не обнаружен')}
    context = {'objects_array': objects_array}
    return render(request, 'show_all.html', context)



def form(request):
    context = {'data': data}
    return render(request, 'form.html', context)


def task(request):
    if request.method == 'POST':
        data = request.POST.get('paintings')
        budget = 500
        paintings = data.split(', ')
        affordable_paintings = []
        for painting in paintings:
            name, price = painting.rsplit('-', 1)
            price = int(price)
            if price%budget == 0:
                affordable_paintings.append(name)
        affordable_paintings.sort()
        result = ', '.join(affordable_paintings)
        return render(request, 'task.html', {'result': result})
    return render(request, 'task.html')