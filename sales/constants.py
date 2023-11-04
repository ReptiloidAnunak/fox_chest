

class OrderStatus:
    CREATED = 'Создан'
    IN_PROGRESS = 'В процессе'
    PAID = 'Оплачен'
    COMPLETED = 'Выполнен'
    CANCELED = 'Отменён'

    choices = (
        (CREATED, CREATED),
        (PAID, PAID),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
        (CANCELED, CANCELED)
    )


class DeliveryMethods:
    PICKUP = "Самовывоз"
    POST_OF_RUSSIA = "Почта России"
    BOXBERRY = "Boxberry"
    SDEK = "CДЭК"
    AVITO = "Авито"
    UNKNOWN = "Неизвестно"

    choices = (
        (PICKUP, PICKUP),
        (POST_OF_RUSSIA, POST_OF_RUSSIA),
        (BOXBERRY, BOXBERRY),
        (SDEK, SDEK),
        (AVITO, AVITO),
        (UNKNOWN, UNKNOWN)
    )


OFFICE_ADDRESS = 'г. Москва, м. Сходненская'