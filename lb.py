import boto3

# ELBs
elb_client = boto3.client('elb')
elbs = elb_client.describe_load_balancers()
for lb in elbs['LoadBalancerDescriptions']:
    for listener_description in lb['ListenerDescriptions']:
        security_policy = listener_description['PolicyNames']
        if security_policy:
            print(security_policy, lb['LoadBalancerName'])

# ALBs
alb_client = boto3.client('elbv2')
albs = alb_client.describe_load_balancers()
for lb in albs['LoadBalancers']:
    listener_descriptions = alb_client.describe_listeners(
        LoadBalancerArn=lb['LoadBalancerArn'])
    for listener in listener_descriptions['Listeners']:
        if 'SslPolicy' in listener.keys():
            ssl_policy = alb_client.describe_ssl_policies(
                Names=[listener['SslPolicy']])
            for policy in ssl_policy['SslPolicies']:
                print(listener['SslPolicy'], lb['LoadBalancerName'])
