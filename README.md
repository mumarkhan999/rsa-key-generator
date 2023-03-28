## Overview
This repo can be used to generate `RSA Keys` pair of private and public keys.

## How to use
1. Clone this repo

```
git clone git@github.com:mumarkhan999/rsa-key-generator.git
cd rsa-key-generator
```
2. Create `virtual environment`

```
virtualenv -p python3.8 venv
```
3. Activate the environment

```
source venv/bin/activate
```
4. Install the `requirements`

```
pip install -r requirements.txt
```
5. Run the script

```
python key-generator.py
```
6. Once the script run successfully, 4 different formats of public and private keys will be generated inside `keys` directory

- `PEM format`
- `YAML format`
- `JWK (JSON) format`
- `JWK String format`
