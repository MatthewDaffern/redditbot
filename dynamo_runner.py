import re, requests, log, API_keys, time, random, functools, itertools, json, boto

def config_loader(json_input):
    json_file = open(json_input, 'r+')
    return json.load(json_file)


def api_bible_json_getter(config, rest_api_input):
    headers = {'api-key': str(api_key)}
    requests.get('https://api.scripture.api.bible/v1/bibles', headers=headers)
    return requests.text


def rest_text_to_json_list(rest_api_input):
    json_object = json.loads(rest_api_input)
    return json_object['data']

def check_for_table_existence(boto_instance, table_name):
    tables = boto_instance.list_tables()
    if table_name in tables.values():
        return table_name:
    else:
        return None

def create_table_if_none_exists(boto_instance, table_name, table_config):
    if table_name == None:
        boto_instance.create_table(TableName=table_name, 
                                   KeySchema=table_config['KeySchema'],
                                   AttributeDefinitions=table_config['AttributeDefinitions'],
                                   ProvisionedThroughput=table_config['ProvisionedThroughput'])
        boto_instance.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        return table_name
    else:
        return table_name

def key_collection(boto_instance, table_name, item_to_add):
    # create a list of ids
    # make sure they match
