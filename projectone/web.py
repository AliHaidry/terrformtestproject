import boto3

client = boto3.client('sts')

arn = 'arn:aws:iam::877950674958:role/WebIdFed_Amazon'
session_name = 'web-identity-federation'
token = 'Atza|IwEBIMcL9zirk_bYGa8Fa7e_AVE32hi0arGqpfzBRRBvGLJJxFfcIvub6Hye4Hc99d1LyukMH5liWgLzH7umV2Bsj6SkzXZsJSO9yhkq1uGdsOO26L5mn0MVZdFnK7NKcnRjWNX9tsSKod1DiLY2dt6k8BtfCltwT9xDofqrm_YxKCWb-HER3nyiaD3JDH2y0zJnsxAFSBppjzTLj5bduZcq0YXZ4_f6DyJN9i8D7nnSkSOd_u_6D8R7KqjkGQD4Pc1ED-xvfPxvvJbmfORjn6vt_vjeSbqI1CA9noeQx6EOB5uztCy-_x9EiPfvHos8Z0RsRNbll8DD7Uyzj5banmbKtjsCvKYdfHMA-k1uEcBfc0mEihgd-jAbCyiWv5CbTeCjYY1Dc5njy5r24W4FSun59uPveRX8a7VQ6wKtPlxw2OLZ1Q'

creds = client.assume_role_with_web_identity(
    RoleArn=arn,
    RoleSessionName=session_name,
    WebIdentityToken=token,
    ProviderId='www.amazon.com',
)

print creds['AssumedRoleUser']['Arn']
print creds['AssumedRoleUser']['AssumedRoleId']