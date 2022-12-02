from databricks_cli.jobs.api import JobsApi 
from databricks_cli.runs.api import RunsApi
from databricks_cli.sdk.api_client import ApiClient
import os
from databricks_cli.sdk import JobsService
import json

print("Hello world")

api_client =   ApiClient(
  host  = os.getenv('https://adb-3508855055231899.19.azuredatabricks.net'),
  token = os.getenv('dapif6271b73932f290ec7c3fa5f80716549-3')
)


jobs_api = JobsApi(api_client)
runs_api = RunsApi(api_client)


job_payload  ={
  "run_name": 'just_a_run',
  "existing_cluster_id": '1023-113851-42v0p07',
  "notebook_task": 
    {
      "notebook_path": '/Users/viren-pravinchandra.devi@capgemini.com/vdtest'
    }
}

new_job = jobs_api.create_job(json=job_payload)

print(new_job)
class JobsApi(object):
  

  def __init__(self, api_client):
        self.client = JobsService(api_client)

  def create_job(self, json, headers=None, version=None):
        return self.client.client.perform_query('POST', '/jobs/create', data=json, headers=headers,
                                                version=version)