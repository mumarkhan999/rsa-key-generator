import json
from Cryptodome.PublicKey import RSA
from jwt.algorithms import get_default_algorithms

private_rsa_key = RSA.generate(2048)
public_rsa_key = private_rsa_key.publickey()

private_rsa_pem_key = private_rsa_key.export_key('PEM')
public_rsa_pem_key = public_rsa_key.export_key('PEM')


with open('keys/private_rsa_key.pem', 'wb') as f:
    f.write(private_rsa_pem_key)

with open('keys/public_rsa_key.pem', 'wb') as f:
    f.write(public_rsa_pem_key)


alg = 'RS512'
algo = get_default_algorithms()[alg]

private_key = algo.prepare_key(private_rsa_pem_key)
public_key = algo.prepare_key(public_rsa_pem_key)

private_jwk_key_str = algo.to_jwk(private_key)
public_jwk_key_str = algo.to_jwk(public_key)

private_jwk_key_dict = json.loads(private_jwk_key_str)
public_jwk_key_dict = json.loads(public_jwk_key_str)


with open('keys/private_jwk_key.json', 'w') as f:
    json.dump(private_jwk_key_dict, f, indent=4)

with open('keys/public_jwk_key.json', 'w') as f:
    json.dump(public_jwk_key_dict, f, indent=4)



with open('keys/private_jwk_key.json', 'r') as input_file, open('keys/private_jwk_key.txt', 'w') as output_file:
    # Loop through each line of the input file
    output_file.write('(')
    for line in input_file:
        # Surround the line with single quotes and write it to the output file
        output_file.write(f"'{line.strip()}'\n")
    output_file.write(')')





with open('keys/public_jwk_key.json', 'r') as input_file, open('keys/public_jwk_key.txt', 'w') as output_file:
    # Loop through each line of the input file
    output_file.write('(')
    for line in input_file:
        # Surround the line with single quotes and write it to the output file
        output_file.write(f"'{line.strip()}'\n")
    output_file.write(')')
