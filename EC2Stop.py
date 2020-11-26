import boto3
from botocore.exceptions import ClientError

    # TODO implement
def SNSTrigger(s1):
      try:
            sns=boto3.client('sns',region_name='ap-southeast-1')

            response=sns.publish(
            TopicArn='arn:aws:sns:ap-southeast-1:330256686372:ec2alert',
            #PhoneNumber='+917097025585',
            Message="Unable to stop Instances"+s1,
            Subject='EC2_status',
            MessageStructure='string',
          )
      except ClientError as e:
         print e.response['Error']['Code']

try:
    ec2 = boto3.client('ec2', region_name='ap-southeast-1')
    response = ec2.describe_instances()
except ClientError as e:
    SNSTrigger(e)

l1 = {}
istring = ""
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        ec2r = boto3.resource('ec2', region_name='ap-southeast-1')
        state = ec2r.Instance(instance["InstanceId"]).state
        if (state["Name"] == "running"):
            if instance["PrivateIpAddress"]!= "10.0.0.30":
              l1[instance["InstanceId"]] = instance["PrivateIpAddress"]

if not l1:
    print ("no instances Running")
#if '10.0.0.30' in l1.values():


print(l1.values())
#sresponse = ec2.stop_instances(
 #       InstanceIds=  l1.keys(),
  #        Force=True
   #    )
#print(sresponse)




