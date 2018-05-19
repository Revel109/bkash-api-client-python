import logging
from decimal import Decimal
from typing import Union

from ._models import Payment, Refund

logger = logging.getLogger('bkash.checkout')


def query(payment: Union[Payment, str]) -> Payment:
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


def execute(payment_id: str) -> Payment:
    """
    Execute a payment
    :param payment_id:
    :return: Payment object
    """
    logger.debug(f"Executing Payment {payment_id}")
    return Payment()


def refund(transaction_id: str, amount: Union[Decimal, float, str], currency: str) -> Refund:
    """
    Provider a refund
    :param transaction_id: The TrxID
    :param amount: The amount as Decimal, float or string
    :param currency: The currency of the denomination
    :return:
    """
    logger.debug(f"Refuding {transaction_id}")
    return Refund()


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
