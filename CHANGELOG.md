# CHANGELOG

## v2.0.0 (2024-10-05)

### Other

* v2: Revamp pair parsing (#8)

* BREAKING CHANGE: Revamped currency pair to use accepted currency pairs from Kraken (now supports all pairs)
* BREAKING CHANGE: Removed support for Bitcoin as BTC, now only works with XBT ([`0611de2`](https://github.com/marc-at-brightnight/krakenpull/commit/0611de2aa1137b35e7ec2e34ee747e9ae4bbe47c))

## v1.0.0 (2024-09-15)

* BREAKING CHANGE: Removed `get_kraken_client` and abstract client, in favor of mocking data in the tests 

## v0.2.1 (2024-05-04)

* Another small fix to ticker info model validation for pair

## v0.2.0 (2024-05-04)

* Fix to ticker info model validation for pair
* Improvements to getting ticker info

## v0.1.1 (2024-04-20)

Updated README

## v0.1.0 (2024-04-20)

Initial version

* Includes functionality for getting order book, account balance, closed orders and ticket info
* Input and output interfaces use pydantic validation
