

class OrderStatus:
    CREATED = 'Создан'
    IN_PROGRESS = 'В процессе'
    COMPLETED = 'Выполнен'
    CANCELED = 'Отменён'

    choices = (
        (CREATED, CREATED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
        (CANCELED, CANCELED)
    )

