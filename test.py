from bkash.checkout import payment

from bkash import currency, intents

req = payment.create(10.00, currency.BDT, intents.SALE,
                     '123123123').send()
req.execute()

payment.query('MyPaymentID')

req = payment.create(10.00, currency.BDT,
                     intents.AUTHORIZATION, '123123123').send()
req.execute()
req.capture()
req.void()

payment.query('MyPaymentID')
