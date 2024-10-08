# Changelog

## 2.0.0 (10/04/2024)

* BREAKING CHANGE: Revamped currency pair to use accepted currency pairs from Kraken (now supports all pairs)
* BREAKING CHANGE: Removed support for Bitcoin as BTC, now only works with XBT

## 1.0.0 (9/15/2024)

* BREAKING CHANGE: Removed `get_kraken_client` and abstract client, in favor of mocking data in the tests 

## 0.2.1 (5/4/2024)

* Another small fix to ticker info model validation for pair

## 0.2.0 (5/4/2024)

* Fix to ticker info model validation for pair
* Improvements to getting ticker info

## 0.1.1 (4/20/2024)

Updated README

## 0.1.0 (4/20/2024)

Initial version

* Includes functionality for getting order book, account balance, closed orders and ticket info
* Input and output interfaces use pydantic validation
