from aws_cdk import(
    Stack,
    aws_dynamodb as dynamodb_,
)
from constructs import Construct

class ResoureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        table_name = 'pipeline_table'
        table = dynamodb_.TableV2(
            self,
            'Pipelinetable',
            table_name=table_name,
            contributor_insights=True,
            billing=dynamodb_.Billing.on_demand(),
            point_in_time_recovery=True,
            partition_key=dynamodb_.Attribute(
                name='id',
                type=dynamodb_.AttributeType.STRING
            )
        )


