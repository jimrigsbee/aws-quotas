import boto3
import argparse

def get_quotas(profile):

    session = boto3.Session(profile_name=profile)
    print('Using profile: ' + profile + ' and region: '+session.region_name)
    cquotas = session.client('service-quotas')
    quotas = [
    { 'quotacode': 'L-0263D0A3', 'svc': 'ec2', 'ssvc': 'ec2', 'desc': 'VPC elastic IPs', 'value': 0},
    { 'quotacode': 'L-1216C47A', 'svc': 'ec2', 'ssvc': 'ec2', 'desc': 'On-Demand standard vCPUs', 'value': 0},
    { 'quotacode': 'L-E79EC296', 'svc': 'ec2', 'ssvc': 'ec2', 'desc': 'Security groups', 'value': 0},
    { 'quotacode': 'L-F678F1CE', 'svc': 'vpc', 'ssvc': 'vpc', 'desc': 'VPCs/region', 'value': 0},
    { 'quotacode': 'L-DF5E4CA3', 'svc': 'vpc', 'ssvc': 'vpc', 'desc': 'NICs/region', 'value': 0},
    { 'quotacode': 'L-A4707A72', 'svc': 'vpc', 'ssvc': 'vpc', 'desc': 'Internet Gateways', 'value': 0},
    { 'quotacode': 'L-1B52E74A', 'svc': 'vpc', 'ssvc': 'vpc', 'desc': 'GW VPC endpoints', 'value': 0},
    { 'quotacode': 'L-FE5A380F', 'svc': 'vpc', 'ssvc': 'vpc', 'desc': 'NAT Gateways (?)', 'value': 0},
    { 'quotacode': 'L-4EA4796A', 'svc': 'route53', 'ssvc': 'dns', 'desc': 'Hosted Zones', 'value': 0},
    { 'quotacode': 'L-C61EE368', 'svc': 'iam', 'ssvc': 'iam', 'desc': 'Users/account', 'value': 0},
    { 'quotacode': 'L-912C8688', 'svc': 'iam', 'ssvc': 'iam', 'desc': 'Roles/account', 'value': 0},
    { 'quotacode': 'L-970C25A9', 'svc': 'iam', 'ssvc': 'iam', 'desc': 'Instance Profiles/account', 'value': 0},
    { 'quotacode': 'L-0485CB21', 'svc': 'cloudformation', 'ssvc': 'cf', 'desc': 'Stacks', 'value': 0},
    { 'quotacode': 'L-E9E9831D', 'svc': 'elasticloadbalancing', 'ssvc': 'elb', 'desc': 'Classic LBs', 'value': 0},
    { 'quotacode': 'unknown', 'svc': 'elasticloadbalancing', 'ssvc': 'elb', 'desc': 'Network LBs', 'value': 0},
    { 'quotacode': 'L-DC2B2D3D', 'svc': 's3', 'ssvc': 's3', 'desc': 'S3 buckets', 'value': 0}
    ]

    for quota in quotas:
        try:
          response = cquotas.get_service_quota(ServiceCode=quota['svc'], QuotaCode=quota['quotacode'])
          quota['value'] = response['Quota']['Value']
        except Exception:
            print('Quota '+quota['desc']+ ' could not be looked up.')
            quota['value'] = -1

    print('-----------------------------------------------------')
    print('| Service | Description               | Quota Limit |')
    print('-----------------------------------------------------')
    for quota in quotas:
        print(quota['ssvc'].ljust(10)+' '+quota['desc'].ljust(27)+' '+str(quota['value']).ljust(13))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Amazon AWS quotas for an account')
    parser.add_argument('--profile', help='Name AWS credential profile')
    args = parser.parse_args()
    get_quotas(args.profile)
