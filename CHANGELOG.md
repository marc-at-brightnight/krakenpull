# CHANGELOG


## v2.0.4 (2024-11-08)

### :bug:

* :bug: Add SWELL to accepted currencies (#15) ([`1c7769a`](https://github.com/marc-at-brightnight/krakenpull/commit/1c7769a5bc4ab0c5d051777b580271b99f9a6aee))


## v2.0.3 (2024-11-06)

### :bug:

* :bug: Add USDG to accepted currencies (#14)

- Remove MPL ([`ece0d83`](https://github.com/marc-at-brightnight/krakenpull/commit/ece0d83bdcdaf5b27584ee43a92b04e7e109060a))

### Other

* chore(release): v2.0.3 [skip ci] ([`f5d16b8`](https://github.com/marc-at-brightnight/krakenpull/commit/f5d16b82e851937bf5110aa738caae4e564adde0))


## v2.0.2 (2024-10-30)

### :bug:

* :bug: Add GIGA to accepted currencies (#13) ([`9b59852`](https://github.com/marc-at-brightnight/krakenpull/commit/9b598522133e1ed1785c28b5d94cb24ae02ae236))

### Other

* chore(release): v2.0.2 [skip ci] ([`9663c7b`](https://github.com/marc-at-brightnight/krakenpull/commit/9663c7b53040e76f32fa55297ff5de5ff899c669))

* ✏️ Fix pyproject.toml (#12)

Update pyproject.toml version variable ([`6d33cb7`](https://github.com/marc-at-brightnight/krakenpull/commit/6d33cb7c519bd4db54b6ce628b5aeb4ddd55b76b))

* 🐛 Fix bug with deployment (#11)

- Pull from branch before deployment to get version changes
- Update pyproject toml version ([`b26ed57`](https://github.com/marc-at-brightnight/krakenpull/commit/b26ed5702f44821c8a99ac19749fc2a58d61a7ae))


## v2.0.1 (2024-10-20)

### :bug:

* :bug: Update supported currencies to latest (#9) ([`21b7997`](https://github.com/marc-at-brightnight/krakenpull/commit/21b79971f1eda1c74e360a75b3b37392ef1f1af9))

### Other

* chore(release): v2.0.1 [skip ci] ([`a3d3c28`](https://github.com/marc-at-brightnight/krakenpull/commit/a3d3c284666e95cd307d810cebd5b97dcf5e3d6b))

* 🚀 Fix deployment (#10)

Deploy after publishing step ([`c24e08b`](https://github.com/marc-at-brightnight/krakenpull/commit/c24e08bf078e6431035978eba2a70daf2219d944))


## v2.0.0 (2024-10-05)

### Other

* v2: Revamp pair parsing (#8)

* BREAKING CHANGE: Revamped currency pair to use accepted currency pairs from Kraken (now supports all pairs)
* BREAKING CHANGE: Removed support for Bitcoin as BTC, now only works with XBT ([`0611de2`](https://github.com/marc-at-brightnight/krakenpull/commit/0611de2aa1137b35e7ec2e34ee747e9ae4bbe47c))

* Get rid of abstract client (#7)

- Now mocking data in the tests ([`6908eac`](https://github.com/marc-at-brightnight/krakenpull/commit/6908eac80de8e451f6250b3122251e68dea64251))

* Small fix to parsing ticker pair (#5) ([`3cfc63c`](https://github.com/marc-at-brightnight/krakenpull/commit/3cfc63ce12be2555034e3350e3d5290b2921d855))

* Fix to get ticker info endpoint (#4) ([`6ac9264`](https://github.com/marc-at-brightnight/krakenpull/commit/6ac92643ff4e15efeea800c03701807d2f07e9c8))

* Update README (#3) ([`1a841ef`](https://github.com/marc-at-brightnight/krakenpull/commit/1a841eff321eb4ff79fb6de0e1ecc1f934c6aedd))

* Add ci/cd (#2) ([`cea8e79`](https://github.com/marc-at-brightnight/krakenpull/commit/cea8e79b5f05011839830b47e5c4a8c1d19eeeca))

* Initial (#1) ([`5ba2974`](https://github.com/marc-at-brightnight/krakenpull/commit/5ba2974b8a863f054c91492a206bab607d982406))

* Initial commit ([`4967070`](https://github.com/marc-at-brightnight/krakenpull/commit/4967070b3653171322e80575edf7ff927631096e))
