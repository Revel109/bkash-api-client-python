import logging
from datetime import datetime
from decimal import Decimal

from bkash import intents

logger = logging.getLogger('bkash.checkout')


class Payment:
    transaction_id: str
    update_time: datetime

    payment_id: str
    create_time: datetime
    transaction_status: str
    amount: Decimal
    currency: str
    intent: str
    invoice_number: str

    def __repr__(self) -> str:
        return f'<Payment id={self.payment_id}>'

    def refund(self) -> 'Refund':
        logger.debug(f"Refuding {self.transaction_id}")
        return Refund()

    def query(self):
        logger.debug(f'Querying {self.payment_id}')

    def void(self):
        if not self.intent == intents.AUTHORIZATION:
            raise ValueError('Void is only applicable for AUTHORIZATION intent')
        logger.debug(f'Voiding {self.payment_id}')

    def capture(self):
        if not self.intent == intents.AUTHORIZATION:
            raise ValueError('Capture is only applicable for AUTHORIZATION intent')
        logger.debug(f'Capturing {self.payment_id}')


class PaymentQuery(Payment):
    refund_amount: Decimal


class Refund:
    original_transaction_id: str
    refund_transaction_id: str
    transaction_status: str
    amount: str
    currency: str
    completed_time: datetime

    def __repr__(self):
        return f'<Refund' \
               f'original_trx_id={self.original_transaction_id}' \
               f'refund_trx_id={self.refund_transaction_id}'
