import boto3

client = boto3.client('gamelift')


def search():
    response = client.search_game_sessions(AliasId='alias-784566b2-47e5-43e6-b19a-3271e09efd1f')
    return response['GameSessions']
