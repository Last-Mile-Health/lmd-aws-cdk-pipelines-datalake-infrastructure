from constructs import Construct
from aws_cdk import Stack
# from constructs import Construct

from aws_cdk import aws_redshiftserverless as redshiftserverless

from .redshift_serverless_namespace_stack import RedshiftServerlessNamespaceStack


class RedshiftServerlessWorkgroupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, target_environment: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        namespace_name = f"{target_environment}-lmd-v2".lower()
        workgroup_name = f"{target_environment}-lmd-v2".lower()

        BASE_CAPACITY = 8
        MAX_CAPACITY = 16

        workgroup_configuration = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
            "publicly_accessible": True,
            "base_capacity": BASE_CAPACITY,
            # "max_capacity": MAX_CAPACITY,
            "tags": [{"key": "type", "value": "lmd-2"}]
        }
        redshift_namespace_stack = RedshiftServerlessNamespaceStack(
            self,
            f'{target_environment}rednspace'.lower(),
            target_environment,
            **kwargs,
        )
        self.add_dependency(redshift_namespace_stack)
        redshift_sls_workgroup = redshiftserverless.CfnWorkgroup(
            self, f'{target_environment}lmdworkgroupid'.lower(), **workgroup_configuration)
