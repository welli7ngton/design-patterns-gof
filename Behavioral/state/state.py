"""
O padrão de projeto State é um padrão comportamental que tem a intenção de
permitir a um objeto mudar seu comportamento quando o seu estado interno muda.

O objeto parecerá ter mudado sua classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def approved(self): pass

    @abstractmethod
    def pending(self): pass

    @abstractmethod
    def rejected(self): pass


class PaymentPending(OrderState):
    def approved(self):
        print('O pagamento foi aprovado.')
        self.order.state = PaymentApproved(self.order)

    def pending(self):
        print('O pagamento já está pendente, não posso fazer nada.')

    def rejected(self):
        print('O pagamento foi recusado.')
        self.order.state = PaymentRejected(self.order)


class PaymentApproved(OrderState):
    def approved(self):
        print('O pagamento já está aprovado, não posso fazer nada.')

    def pending(self):
        print('O pagamento está pendente.')
        self.order.state = PaymentPending(self.order)

    def rejected(self):
        print('O pagamento está rejeitado.')
        self.order.state = PaymentRejected(self.order)


class PaymentRejected(OrderState):
    def approved(self):
        print('O pagamento está rejeitado, não pode ser aprovado.')

    def pending(self):
        print('O pagamento está rejeitado, não pode ficar pendente.')

    def rejected(self):
        print('O pagamento já estava rejeitado.')


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approved(self):
        self.state.approved()

    def rejected(self):
        self.state.rejected()


if __name__ == '__main__':
    order = Order()
    order.state.approved()
    order.state.rejected()
    order.state.pending()
