import time
import boto3
from boto3.dynamodb.conditions import Attr
from settings import BACKEND
from lib.variables import EnvironmentVariable


class DynamoDBBackend:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(BACKEND.get('settings', {}).get('table_name'))

    def query(self):
        result = self.table.scan(
            FilterExpression=Attr('version').eq('LATEST'),
        )

        if not result['Items']:
            return None

        return [EnvironmentVariable(item) for item in result['Items']]

    def get(self, name):
        result = self.table.get_item(
            Key={
                'name': name,
                'version': 'LATEST',
            }
        )

        if 'Item' not in result:
            return None

        return EnvironmentVariable(result['Item'])

    def set(self, name, value):
        old_value = self.get(name)

        if old_value:
            # If an existing variable exists with a different value, archive it.
            if old_value.value == value:
                return False

            self.table.put_item(
                Item={
                    'name': name,
                    'value': old_value.value,
                    'version': 'ARCHIVED_{}'.format(int(time.time())),
                }
            )

        self.table.put_item(
            Item={
                'name': name,
                'value': value,
                'version': 'LATEST',
            }
        )

        return True

backend_class = DynamoDBBackend
