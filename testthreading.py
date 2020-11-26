import boto3
import threading

Class test(threading.Thread):
    def run(self):
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
             l1[instance["InstanceId"]]=instance["PrivateIpAddress"]

        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])
