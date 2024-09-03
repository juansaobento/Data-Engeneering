import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
from modules import Creacion_dataframe, Conexion_RS, Obtencion_datos
from datetime import datetime, timedelta

default_args={
    'owner': 'juansaobento',
    'retries':3,
    'retry_delay': timedelta(minutes=5)
}   

with DAG (
    default_args=default_args,
    dag_id="etl-cocktails",
    schedule="@daily",
    start_date=dt.datetime(year=2024, month=8, day=25),
    end_date=None,
    catchup=True,
    tags=["etl", "cocktails"],
    doc_md="Este dag permite extraer y cargar cocktails"
    ) as dag:

    obtencion_datos= PythonOperator(
            dag= dag,
            task_id="obtencion-operator",
            python_callable= Obtencion_datos
            )
    
    creacion_df= PythonOperator(
            dag= dag,
            task_id="creacion-data-frame",
            python_callable= Creacion_dataframe
            )
    
    conexion_RS= PythonOperator(
            dag= dag,
            task_id="conexion-rs",
            python_callable= Conexion_RS
            )
    
    obtencion_datos>>creacion_df>>conexion_RS