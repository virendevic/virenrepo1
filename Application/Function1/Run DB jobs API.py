from databricks_cli.jobs.api import JobsApi 
from databricks_cli.runs.api import RunsApi
from databricks_cli.sdk.api_client import ApiClient
import os
from databricks_cli.sdk import JobsService
import json


api_client = ApiClient(
  host  = os.getenv('https://adb-3508855055231899.19.azuredatabricks.net'),
  token = os.getenv('dapif6271b73932f290ec7c3fa5f80716549-3')
)


jobs_api = JobsApi(api_client)
runs_api = RunsApi(api_client)


job_payload ={

  "job_id":998581482524751,
  "notebook_params":{
   "myinput":"Hello"
  }
}
RunsApi.submit_run(
    job_payload
)

#print(new_job)

class RunsApi(object):
    def __init__(self, api_client):
        self.client = JobsService(api_client)

    def submit_run(self, json, version=None):
        return self.client.client.perform_query('POST', '/jobs/runs/submit', data=json,
                                                version=version)
