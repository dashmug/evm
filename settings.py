import os

TABLE_NAME = os.environ.get('ENVIRONMENT_MANAGER_TABLE')

BACKEND = {
    'name': 'dynamodb',
    'settings': {
        'table_name': os.environ.get('ENVIRONMENT_MANAGER_TABLE')
    }
}
