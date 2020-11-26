import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # TODO implement
    # try:
    ec2 = boto3.client('ec2', region_name='ap-southeast-1')
    response = ec2.describe_instances()
    # except ClientError as e:
    # SNSTrigger(e)

    l1 = {}

    istring = ""
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            ec2r = boto3.resource('ec2', region_name='ap-southeast-1')
            #
            #ec2r.Instance(instance["InstanceId"]).tags[2]['Value']=''

            if instance["PrivateIpAddress"]=='10.0.0.63':  # The instance to which we are adding tags
                t=instance["InstanceId"]
                print(t)
            if instance["PrivateIpAddress"]=="10.0.0.64":  #the tags we are fetching from existing instance
             tag = ec2r.Instance(instance["InstanceId"]).tags # this gives all the existing tags for an instance
             Names = [ i['Value'] for i in tag if i['Key'] == 'Name'] #
             print(Names)
             ec2.create_tags(
                 Resources= [t],
                    Tags= [
                     {
                            'Key' : 'Name1', #This will create new tag and assigns to the instance...
                                             # To change the exising tags use existing tag name as key
                            'Value' : Names[0]
                     }
                 ]

             )









    return "Complete"

lambda_handler(1,1)