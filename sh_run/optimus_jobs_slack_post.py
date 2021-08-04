from __future__ import print_function
from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow import settings
from airflow.hooks.hdfs_hook import HDFSHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.sensors.hdfs_sensor import HdfsSensor
from datetime import datetime
from datetime import timedelta
from airflow.models import Variable
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.utils.trigger_rule import TriggerRule
from jinja2 import Template
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# ------Python Function ---------


def fn_on_failure_callback(context):
    print("Dag Failed-{0}, Task failed - {1}".format(context['dag'], context['task_instance_key_str']))
    message = " :alert: Airflow Failure - {0}".format(DAG_NAME)
    task_on_failure_callback = BashOperator(
        task_id='task_on_failure_callback',
        bash_command="""curl -X POST -H 'Content-type: application/json' --data '{"text": " """ + """{0}""".format(message) + """ " }' """ + Variable.get("slack_channel_ima_engteam")
    )
    return task_on_failure_callback.execute(context=context)

# --- Default parameters -----


default_args = {
    'owner': 'smukherjee',
    'start_date': datetime(2021, 4, 1),
    'email': ['smukherjee@groupon.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
    'depends_on_past': True,
    'ignore_first_depends_on_past': True
}

# ---- Variables ---------------
# BASE_PATH = str(Path(__file__).Parent.Parent)


SCRIPT_PATH = '/home/svc_ima/projects'
TMP_PATH = '/tmp'
JAR_PATH = '/home/svc_ima/common/TeraJDBC'
WAREHOUSE_DIR = '/user/svc_ima/'
LOG_PATH = '/tmp/log'
DAG_NAME = 'optimus_jobs_slack_post'
CONNECTION = 'ssh_svc_ima_cerebro4'


utc_datetime = datetime.strftime(datetime.utcnow(), '%Y-%m-%d %H:%M:%S')
execution_date = """ {{ ds }} """
run_id = """ {{ run_id }} """
dag_run = """ {{ dag_run }} """

# ------- DAG ----------------

with DAG('{}'.format(DAG_NAME),
         schedule_interval="*/5 * * * *",
         default_args=default_args,
         max_active_runs=1,
         catchup=False
         ) as dag:

    task_optimus_jobs_slack_post = SSHOperator(
        task_id='task_optimus_jobs_slack_post',
        ssh_conn_id='{}'.format(CONNECTION),
        command="sh /home/svc_ima/optimus_slack_post.sh ",
        trigger_rule=TriggerRule.ALL_DONE,
        on_failure_callback=fn_on_failure_callback,
        provide_context=True
    )

if __name__ == "__main__":
    dag.cli()
