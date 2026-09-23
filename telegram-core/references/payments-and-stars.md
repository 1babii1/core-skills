# Payments and Stars

- Digital goods/services inside Telegram use Stars (`XTR`) when required by Telegram policy.
- Physical-goods flows may use supported external payment providers under current rules.
- Validate invoice payload/product/price/currency on the server.
- Answer pre-checkout within Telegram's required deadline.
- Never fulfill from invoice creation, client redirect, or pre-checkout alone.
- Fulfill only after a verified successful-payment update.
- Persist Telegram charge identifiers with unique constraints.
- Make entitlement granting, delivery, refunds, and reconciliation idempotent.
- Separate billing record, entitlement state, and delivery status.
- Reconcile provider/Telegram transaction history and alert on mismatches.
- Provide terms, support, refund handling, and `/paysupport` where required.

Test duplicates, delayed updates, timeout, cancellation, insufficient balance, partial application failure, refund, and replay.
