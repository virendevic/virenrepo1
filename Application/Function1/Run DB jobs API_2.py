import requests
import json

job_payload = {
    "job_id": 998581482524751,
    "tasks": [
            {
                "task_key": "vdjob",
                "notebook_task": {
                    "notebook_path": "/Users/viren-pravinchandra.devi@capgemini.com/vdtest",
                    "base_parameters": {
                        "myinput": ""
                    },
                    "source": "WORKSPACE"
                },
                "existing_cluster_id": '1023-113851-42v0p07',
                "timeout_seconds": 0,
                "email_notifications": {}
            }
        ],
        
        }


hed = {'Authorization': 'Bearer ' + 'dapif6271b73932f290ec7c3fa5f80716549-3'}

resp = requests.post('https://adb-3508855055231899.19.azuredatabricks.net/api/2.1/jobs/runs/submit', json=job_payload, headers=hed)

print(resp.status_code)

print(resp.text)