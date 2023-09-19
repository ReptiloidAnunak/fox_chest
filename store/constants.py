class WearSize:
    '''???'''
    sizes = (50, 56, 62, 68, 74, 80,
             86, 92, 98, 104, 110,
             116, 122, 128, 134,
             140, 146, 152)
    choices = sizes


class WearColor:
    NONE = '-'
    WHITE = 'Белый'
    BLACK = 'Черный'
    YELLOW = 'Желтый'
    GREEN = 'Зеленый'
    BLUE = 'Синий'
    choices = (
        (WHITE, WHITE),
        (BLACK, BLACK),
        (YELLOW, YELLOW),
        (GREEN, GREEN),
        (BLUE, BLUE),
        (NONE, NONE)
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