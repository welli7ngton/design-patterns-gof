def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self, name_) -> None:
        self.theme = 'dark'
        self.n = name_


@singleton
class Test:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    as1 = AppSettings('well')
    as1.theme = 'light'
    print(as1.theme)

    as2 = AppSettings()
    print(as1.theme)
    print(as1.n)
    print(as2.n)

    t1 = Test()
    t2 = Test()
    print(t1 == t2)
