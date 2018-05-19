import logging
from decimal import Decimal
from typing import Union

from ._models import PreparedPayment, Payment, PreparedRefund

logger = logging.getLogger('bkash.checkout')


def create(amount: Union[Decimal, float, int], currency: str, intent: str, invoice_number: str) -> PreparedPayment:
    """
    Create a Payment (Sale or Authorize)

    :param amount: The amount as Decimal or float or int
    :param currency: The current as string
    :param intent: The name of the intent
    :param invoice_number: The invoice number (merchant) as string
    :return:
    """

    payment = PreparedPayment()

    payment.amount = amount
    payment.currency = currency
    payment.intent = intent
    payment.invoice_number = invoice_number

    return payment


def query(payment: Union[Payment, str]):
    """
    Query the transaction status and other details of a Payment
    :param payment:
    :return:
    """

    if isinstance(payment, str):
        logging.debug(f'Querying {payment}')
    elif isinstance(payment, Payment):
        return payment.query()
    else:
        raise ValueError(f'Unexpected type for payment: {type(payment)}')


def refund(transaction_id: str, amount: Union[Decimal, float, str], currency: str) -> PreparedRefund:
    """
    Provider a refund
    :param transaction_id: The TrxID
    :param amount: The amount as Decimal, float or string
    :param currency: The currency of the denomination
    :return:
    """

    prepared_refund = PreparedRefund()

    prepared_refund.transaction_id = transaction_id
    prepared_refund.amount = amount
    prepared_refund.currency = currency

    return prepared_refund


def capture(payment: Union[Payment, str]):
    """
    Capture authorized funds
    :param payment: Payment or Payment ID
    :return:
    """
    if isinstance(payment, str):
        logging.debug(f'Capturing {payment}')
    elif isinstance(payment, Payment):
        payment.void()
    else:
        raise ValueError(f'Unexpected type for payment: {type(payment)}')


def void(payment: Union[Payment, str]):
    """
    Release authorized funds
    :param payment: Payment or Payment ID
    :return:
    """
    if isinstance(payment, str):
        logging.debug(f'Voiding {payment}')
    elif isinstance(payment, Payment):
        payment.void()
    else:
        raise ValueError(f'Unexpected type for payment: {type(payment)}')
