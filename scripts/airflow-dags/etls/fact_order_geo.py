import os
from datetime import timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

from contrib.operators.PostgreSQLOperator import PostgreSQLOperator

config = {
    "script_name": "fact_order_geo",
    "script_path": Variable.get("etl_script"),
    "conn_id": "ds_warehouse_postgres_local"
}

with DAG(
    "_".join(["etl", config["script_name"]]),
    description="DAG for Order Geo Fact ETL",
    schedule_interval=None,
    start_date=days_ago(1),
    tags=["fact", "etl"]
) as dag:
    start = DummyOperator(
        task_id="start"
    )

    fact_order_geo = PostgreSQLOperator(
        task_id="fact_order_geo",
        conn_id=config["conn_id"],
        script_path=os.path.join(config["script_path"],
                                    ".".join([config["script_name"], "sql"]))
    )

    finish =  DummyOperator(
        task_id="finish"
    )

    start >> fact_order_geo >> finish