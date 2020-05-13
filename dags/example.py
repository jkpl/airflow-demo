from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator


k = KubernetesPodOperator(
    namespace="default",
    image="debian:10-slim",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    labels={"purpose": "demo"},
    name="demo",
    task_id="task",
    is_delete_operator_pod=True,
    hostnetwork=False,
)

