# bkash-api-client-python

API Client for connecting with bKash Checkout and Direct.

Note: **Under Very Heavy Development**

## Projected Usage

### Query Example

```python
from bkash.checkout import payment

payment.query("our_payment_id")
```

### Authorization Intent Example

```python
from bkash.checkout import payment

our_payment = payment.execute('my_payment_id')

# capture rights to bill
our_payment.capture()

# release all rights to bill
our_payment.void()
```

```python
from bkash.checkout import payment

payment.capture('my_payment_id')

# or do this
# our_payment = payment.query("payment_id")
# our_payment.capture()
```

```python
from bkash.checkout import payment

payment.void('my_payment_id')

# or do this
# our_payment = payment.query("payment_id")
# our_payment.void()
```

```python
from bkash import currency
from bkash.checkout import payment

payment.refund('our_trx_id', 24.00, currency.BDT)

# or do this
# our_payment = payment.query("payment_id")
# our_payment.refund()

```
