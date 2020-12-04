from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Каталог',
        # href в списке каталогов сделал временно для наглядности, думаю в дальнейшем будет таблица в БД с категориями и оттуда по pk буду брать ключь и вставлять в url категории
        'catalogs_list': [
            {'href': 'products_new', 'name': 'Новинки'},
            {'href': 'products_dress', 'name': 'Одежда'},
            {'href': 'products_shoes', 'name': 'Обувь'},
            {'href': 'products_accessories', 'name': 'Аксессуары'},
            {'href': 'products_presents', 'name': 'Подарки'},
        ],
        # image_scr сделал для нормального отображения на текущем этапе сайта. В дальнейшем думаю в БД с товарами сделать поле img где будет храниться картинка товара, чтобы нигде не было путей, а только теги в шаблоне типа {{ item.photo.url }}
        'products_list': [
            {
                'title': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6090',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'image_src': 'vendor/img/products/Adidas-hoodie.png',
            }, {
                'title': 'Синяя куртка The North Face',
                'price': '23725',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'image_src': 'vendor/img/products/Blue-jacket-The-North-Face.png',
            }, {
                'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3390',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий',
                'image_src': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            }, {
                'title': 'Черный рюкзак Nike Heritage',
                'price': '2340',
                'description': 'Плотная ткань. Легкий материал.',
                'image_src': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
            }, {
                'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13590',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'image_src': 'vendor/img/products/Black-Dr-Martens-shoes.png',
            }, {
                'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2890',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'image_src': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            },
        ]
    }
    return render(request, 'mainapp/products.html', context)
