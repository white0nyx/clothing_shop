import datetime
import uuid
from dataclasses import dataclass
from environs import Env
import pyqiwi

env = Env()
env.read_env('clothing_store/.env')
wallet=env.str('WALLET')
token=env.str('QIWI')
pub_key=env.str('QIWI_P_PUB')
sec_key=env.str('QIWI_P_SEC')


wallet = pyqiwi.Wallet(token=token, number=wallet)


class NotEnoughMoney(Exception):
    pass

class NoPaymentFound(Exception):
    pass


@dataclass
class Payment:
    amount : int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date).get("transactions")
        for t in transactions:
            if t.comment:
                if str(self.id) in transactions.comment:
                    if float(transactions.total.amount) >= float(self.amount):
                        return True

                    else:
                        raise NotEnoughMoney

        else:
            raise NoPaymentFound


    @property
    def invoice(self):
        link = f"https://oplata.qiwi.com/create?publicKey={pub_key}&amount={self.amount}&comment={self.id}"
        return link
