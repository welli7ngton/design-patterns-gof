class DiscountStrategy():
    TWENTY_PERCENT_DISCOUNT = 0.2
    THIRTY_PERCENT_DISCOUNT = 0.3
    FIFTY_PERCENT_DISCOUNT = 0.5

    @classmethod
    def _set_custom_discount(cls, discount: int):
        __class__.CUSTOM_DISCOUNT = discount / 100
        return cls

    @classmethod
    def twenty_percent_off(cls, value) -> int | float:
        return value - (value * cls.TWENTY_PERCENT_DISCOUNT)

    @classmethod
    def thirty_percent_off(cls, value) -> int | float:
        return value - (value * cls.THIRTY_PERCENT_DISCOUNT)

    @classmethod
    def fifty_percent_off(cls, value) -> int | float:
        return value - (value * cls.FIFTY_PERCENT_DISCOUNT)

    @classmethod
    def custom_discount(cls, value) -> int | float:
        return value - (value * cls.CUSTOM_DISCOUNT)

    @classmethod
    def no_discount(cls, value) -> int | float:
        return value


class Order:
    def __init__(self, total, discount_method: DiscountStrategy) -> None:
        self.total = total
        self.discount_method = discount_method

    @property
    def discount(self) -> float:
        return self.discount_method(self.total)


if __name__ == '__main__':
    o1 = Order(1000, DiscountStrategy.twenty_percent_off)
    print(o1.discount)

    o2 = Order(1000, DiscountStrategy.thirty_percent_off)
    print(o2.discount)

    o3 = Order(1000, DiscountStrategy.fifty_percent_off)
    print(o3.discount)

    o4 = Order(1000, DiscountStrategy.no_discount)
    print(o4.discount)

    o5 = Order(1000, DiscountStrategy._set_custom_discount(50).custom_discount)
    print(o5.discount)
