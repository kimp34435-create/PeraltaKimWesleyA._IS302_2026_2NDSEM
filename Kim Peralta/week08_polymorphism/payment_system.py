class Payment_kwap:
    def pay_kwap(self_kwap):
        print("Processing payment")


class CashPayment_kwap(Payment_kwap):
    def pay_kwap(self_kwap):
        print("Payment made using cash")


class CardPayment_kwap(Payment_kwap):
    def pay_kwap(self_kwap):
        print("Payment made using credit card")


payments_kwap = [CashPayment_kwap(), CardPayment_kwap()]
for p_kwap in payments_kwap:
    p_kwap.pay_kwap()
