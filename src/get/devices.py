import json

def get_devices(context, event): 
    return { 
        "statusCode": 400, 
        "body": json.dumps([
            {"deviceId": "a", "deviceType": "co2", "deviceName": "device1"}, 
            {"deviceId": "b", "deviceType": "pir", "deviceName": "device2"}]), 
        "headers": {'Access-Control-Allow-Origin': '*'} 
 } 


