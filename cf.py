import boto3

client = boto3.client('cloudfront')

distros = client.list_distributions()

for distro in distros['DistributionList']['Items']:
    print (distro['ViewerCertificate']['MinimumProtocolVersion'],
           distro['Id'], distro['Comment'].rstrip())
