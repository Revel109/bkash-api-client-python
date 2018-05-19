import logging
from datetime import datetime
from decimal import Decimal
from typing import Union

logger = logging.getLogger('bkash.checkout')


class PreparedPayment:
    amount: Union[Decimal, float, int]
    currency: str
    intent: str
    invoice_number: str

    def __str__(self) -> str:
        return f'<PreparedPayment invoice={self.invoice_number}, intent={self.intent}>'

    def send(self) -> 'Payment':
        logger.debug(f'Sending checkout Request for {self.invoice_number}')
        return Payment()


class Payment:
    payment_id: str
    create_time: datetime
    transaction_status: str
    amount: Decimal
    currency: str
    intent: str
    invoice_number: str

    def __str__(self) -> str:
        return f'<Payment id={self.payment_id}>'

    def execute(self) -> 'Payment':
        logger.debug(f'Executing checkout Request for {self.invoice_number}')
        return Payment()

    def query(self):
        logger.debug(f'Querying {self.payment_id}')

    def void(self):
        logger.debug(f'Voiding {self.payment_id}')

    def capture(self):
        logger.debug(f'Capturing {self.payment_id}')


class ProcessedPayment:
    transaction_id: str
    payment_id: str
    create_time: datetime
    update_time: datetime
    transaction_status: str
    amount: Decimal
    currency: str
    intent: str
    invoice_number: str

    def refund(self) -> 'PreparedRefund':
        refund = PreparedRefund()
        refund.amount = self.amount
        refund.currency = self.currency
        refund.transaction_id = self.transaction_id
        return refund


class PreparedRefund:
    transaction_id: str
    amount: Union[Decimal, float, str]
    currency: str

    def __repr__(self):
        return f'<PreparedRefund transaction_id={self.transaction_id}'

    def send(self):
        logger.debug(f'Sending refund for {self.transaction_id}')


class Refund:
    original_transaction_id: str
    refund_transaction_id: str
    transaction_status: str
    amount: str
    currency: str
    completed_time: datetime

    def __repr__(self):
        return f'<PreparedRefund' \
               f'original_transaction_id={self.original_transaction_id}' \
               f'refund_transaction_id={self.refund_transaction_id}'
