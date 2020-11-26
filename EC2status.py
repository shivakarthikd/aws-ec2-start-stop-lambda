import timeit
#import re

code_to_test= """
from datetime import datetime
import boto3
import botocore

ec2=boto3.resource('ec2',region_name='')
#def SNSTrigger(s1):
 #           sns=boto3.client('sns',region_name='ap-southeast-1')
#
 #           response=sns.publish(
  #          TopicArn='arn:aws:sns:ap-southeast-1:330256686372:ec2alert',
   #         #PhoneNumber='+917097025585',
    #        Message=s1,
     #       Subject='EC2_status',
      #      MessageStructure='string',
       #   )
        #    print(response)
         #   if(response['ResponseMetadata']['HTTPStatusCode']==200):
          #      print("sucessfull")
           # else:
            #   print("Failed")


ec2=boto3.client('ec2',region_name='ap-southeast-1')
if(ec2==None):
    print("unable to connect to EC2")
response = ec2.describe_instances()
#print(list(response["Reservations"]))
if(response==None):
    print("No instances")
l1={}
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        #for monitoring in instance["Monitoring"]:
        # print(instance)
        # v1=instance["Monitoring"]
        # This sample print will output entire Dictionary obj
         l1[instance["InstanceId"]]=instance["PrivateIpAddress"]

        # This will print will output the value of the Dictionary key 'InstanceId'
#print(instance["InstanceId"])


istring=""
for instanceid in l1.keys():

    ec2r=boto3.resource('ec2',region_name='ap-southeast-1')
    instance=ec2r.Instance(instanceid).state
    if(instance["Name"]=="running"):
        istring=istring+instanceid+"-"+l1[instanceid]+","
if(istring==""):
    print("unable to fetch running instances")
else:
    print("instance that are running"+istring)
    print(datetime.fromtimestamp(1570744800))
#"""

#z=re.match("(201\w+)\-.*\-.*\W(22\:00\:.*)",datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)
