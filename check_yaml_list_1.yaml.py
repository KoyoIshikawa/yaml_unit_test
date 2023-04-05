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
    {'file': 'yaml_list/yaml_list_1.yaml',
      'parameters': [
        {'elements': ['DistributionList', 'Items', 0, 'ARN'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 0], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 0, 1], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 0], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 0, 1], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachedMethods', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'Enabled', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'Enabled', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 0, 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'PathPattern', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'ViewerProtocolPolicy'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 0], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 0, 1], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 0], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 0, 1], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachedMethods', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'Enabled', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'Enabled', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'AllowedMethods', 'CachePolicyId', 'Compress', 'FieldLevelEncryptionId', 'FunctionAssociations', 'LambdaFunctionAssociations', 'SmoothStreaming', 'TargetOriginId', 'TrustedKeyGroups', 'TrustedSigners', 'ViewerProtocolPolicy'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'Items', 0, 'HeaderName'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'Items', 0, 'HeaderName', 'HeaderValue'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort', 'OriginKeepaliveTimeout'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy', 'OriginReadTimeout'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy', 'OriginReadTimeout', 'OriginSslProtocols', 'Items', 0], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'HTTPPort', 'HTTPSPort', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy', 'OriginReadTimeout', 'OriginSslProtocols', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'DomainName'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'DomainName', 'Id'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'DomainName', 'Id', 'OriginAccessControlId'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'DomainName', 'Id', 'OriginAccessControlId', 'OriginPath'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 0, 'ConnectionAttempts', 'ConnectionTimeout', 'CustomHeaders', 'CustomOriginConfig', 'DomainName', 'Id', 'OriginAccessControlId', 'OriginPath', 'OriginShield', 'Enabled'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'Items', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'GeoRestriction', 'Quantity'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'GeoRestriction', 'Quantity', 'RestrictionType'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status', 'ViewerCertificate', 'CertificateSource'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status', 'ViewerCertificate', 'CertificateSource', 'CloudFrontDefaultCertificate'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status', 'ViewerCertificate', 'CertificateSource', 'CloudFrontDefaultCertificate', 'MinimumProtocolVersion'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status', 'ViewerCertificate', 'CertificateSource', 'CloudFrontDefaultCertificate', 'MinimumProtocolVersion', 'SSLSupportMethod'], 'expected_value': ''},
        {'elements': ['DistributionList', 'Items', 0, 'ARN', 'Aliases', 'CacheBehaviors', 'Comment', 'CustomErrorResponses', 'DefaultCacheBehavior', 'DomainName', 'Enabled', 'HttpVersion', 'Id', 'IsIPV6Enabled', 'LastModifiedTime', 'OriginGroups', 'Origins', 'PriceClass', 'Restrictions', 'Staging', 'Status', 'ViewerCertificate', 'WebACLId'], 'expected_value': ''},
     ]
    }
]