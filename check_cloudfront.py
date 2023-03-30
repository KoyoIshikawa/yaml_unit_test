import yaml
import os
import sys
import cheke_func

dir = os.getcwd()
account_env = sys.argv[1]

env, account_env = cheke_func.setup_value(account_env)
system = 'system'
section = 'section'
name_prefix = '{}-{}-{}'.format(system, env, section)

taraget = [
    {'file': '/Users/koyoishikawa/Desktop/python_yaml/list-distributions.yaml',
      'parameters': [
        {'elements': [' "DistributionList", "Items", 0, "ARN" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Aliases", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "CachedMethods", "Items", 0 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "CachedMethods", "Items", 1 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "CachedMethods", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "Items", 0 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "Items", 1 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "AllowedMethods", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "CachePolicyId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "Compress" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "FieldLevelEncryptionId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "FunctionAssociations", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "LambdaFunctionAssociations", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "PathPattern" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "SmoothStreaming" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "TargetOriginId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "TrustedKeyGroups", "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "TrustedKeyGroups", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "TrustedSigners", "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "TrustedSigners", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Items", 0, "ViewerProtocolPolicy" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CacheBehaviors", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Comment" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "CustomErrorResponses", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "CachedMethods", "Items", 0 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "CachedMethods", "Items", 1 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "CachedMethods", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "Items", 0 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "Items", 1 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "AllowedMethods", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "CachePolicyId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "Compress" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "FieldLevelEncryptionId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "FunctionAssociations", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "LambdaFunctionAssociations", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "SmoothStreaming" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "TargetOriginId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "TrustedKeyGroups", "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "TrustedKeyGroups", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "TrustedSigners", "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "TrustedSigners", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DefaultCacheBehavior", "ViewerProtocolPolicy" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "DomainName" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "HttpVersion" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Id" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "IsIPV6Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "LastModifiedTime" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "OriginGroups", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "ConnectionAttempts" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "ConnectionTimeout" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomHeaders", "Items", 0, "HeaderName" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomHeaders", "Items", 0, "HeaderValue" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomHeaders", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "HTTPPort" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "HTTPSPort" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "OriginKeepaliveTimeout" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "OriginProtocolPolicy" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "OriginReadTimeout" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "OriginSslProtocols", "Items", 0 '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "CustomOriginConfig", "OriginSslProtocols", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "DomainName" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "Id" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "OriginAccessControlId" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "OriginPath" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Items", 0, "OriginShield", "Enabled" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Origins", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "PriceClass" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Restrictions", "GeoRestriction", "Quantity" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Restrictions", "GeoRestriction", "RestrictionType" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Staging" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "Status" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "ViewerCertificate", "CertificateSource" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "ViewerCertificate", "CloudFrontDefaultCertificate" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "ViewerCertificate", "MinimumProtocolVersion" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "ViewerCertificate", "SSLSupportMethod" '], 'expected_value': ''},
        {'elements': [' "DistributionList", "Items", 0, "WebACLId" '], 'expected_value': ''},
     ]
    }
]