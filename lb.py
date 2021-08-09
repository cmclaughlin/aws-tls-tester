import boto3

client = boto3.client('elbv2')

lbs = client.describe_load_balancers()

for lb in lbs['LoadBalancers']:
    listener_descriptions = client.describe_listeners(
        LoadBalancerArn=lb['LoadBalancerArn'])
    for listener in listener_descriptions['Listeners']:
        if 'SslPolicy' in listener.keys():
            ssl_policy = client.describe_ssl_policies(
                Names=[listener['SslPolicy']])
            for policy in ssl_policy['SslPolicies']:
                print(listener['SslPolicy'], lb['LoadBalancerName'])
