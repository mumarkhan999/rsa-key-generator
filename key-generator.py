import json
import yaml
from Cryptodome.PublicKey import RSA
from jwt.algorithms import get_default_algorithms

private_rsa_key = RSA.generate(2048)
public_rsa_key = private_rsa_key.publickey()

private_rsa_pem_key = private_rsa_key.export_key('PEM')
public_rsa_pem_key = public_rsa_key.export_key('PEM')


##############################
# Storing keys in PEM format #
##############################
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


###################################
# Storing keys in JWK JSON format #
###################################
with open('keys/private_jwk_key.json', 'w') as f:
    json.dump(private_jwk_key_dict, f, indent=4, sort_keys=True)

with open('keys/public_jwk_key.json', 'w') as f:
    json.dump(public_jwk_key_dict, f, indent=4, sort_keys=True)


##########################################
# Storing keys in JWK JSON string format #
##########################################
def store_keys_in_jwk_json_string_format(input_filepath, output_filepath, is_private_key=False):
    with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
        output_file.write('##### Two formats are available. Pick one as per your configuration file\n')
        output_file.write('##### Storing key in single line string\n')
        if is_private_key:
            output = json.dumps(private_jwk_key_dict, sort_keys=True)
        else:
            output = json.dumps(public_jwk_key_dict, sort_keys=True)
        output_file.write(f"'{output}'")
        output_file.write('\n\n\n')

        # Loop through each line of the input file
        output_file.write('##### Storing key in multiline string')
        output_file.write('\n(\n')
        for line in input_file:
            # Surround the line with single quotes and write it to the output file
            output_file.write(f"'{line.strip()}'\n")
        output_file.write(')')


store_keys_in_jwk_json_string_format('keys/private_jwk_key.json', 'keys/private_jwk_key.txt', True)
store_keys_in_jwk_json_string_format('keys/public_jwk_key.json', 'keys/public_jwk_key.txt', False)

##############################
# Storing keys in yml format #
##############################

def store_keys_in_jwk_yml_format(input_filepath, output_filepath):
    with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
        json_data =  json.load(input_file)
        yaml_data = yaml.dump(json_data)
        output_file.write(yaml_data)


store_keys_in_jwk_yml_format('keys/private_jwk_key.json', 'keys/private_jwk_key.yml')
store_keys_in_jwk_yml_format('keys/public_jwk_key.json', 'keys/public_jwk_key.yml')
