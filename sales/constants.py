

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

