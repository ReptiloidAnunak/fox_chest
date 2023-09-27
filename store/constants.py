class WearSize:
    sizes = ((50, 50),
             (56, 56),
             (62, 62),
             (68, 68),
             (74, 74),
             (80, 90),
             (86, 80),
             (92, 92),
             (98, 98),
             (104, 104),
             (110, 110),
             (116, 116),
             (122, 122),
             (128, 128),
             (134, 134),
             (140, 140),
             (146, 146),
             (152, 152)
             )
    choices = sizes


class WearColor:
    NONE = '-'
    WHITE = 'Белый'
    BLACK = 'Черный'
    YELLOW = 'Желтый'
    GREEN = 'Зеленый'
    BLUE = 'Синий'
    BROWN = 'Коричневый'
    ORANGE = 'Оранжевый'
    VIOLET = 'Фиолетовый'
    GRAY = 'Серый'
    PINK = 'Розовый'
    choices = (
        (WHITE, WHITE),
        (BLACK, BLACK),
        (YELLOW, YELLOW),
        (GREEN, GREEN),
        (BLUE, BLUE),
        (BROWN, BROWN),
        (ORANGE, ORANGE),
        (VIOLET, VIOLET),
        (GRAY, GRAY),
        (PINK, PINK),
        (NONE, NONE),
    )


class WearMaterial:
    pass


class WearSex:
    MALE = 'Male'
    FEMALE = 'Female'
    UNISEX = 'Unisex'
    choices = (
              (MALE, MALE),
              (FEMALE, FEMALE),
              (UNISEX, UNISEX)
              )


class BrandCountry:
    GERMANY = 'Германия'
    TURKEY = 'Турция'
    CHINA = 'Китай'
    NONE = '-'
    choices = (
        (GERMANY, GERMANY),
        (TURKEY, TURKEY),
        (CHINA, CHINA),
        (NONE, NONE)
    )