from aws_cdk import (
    Stage,
)
from constructs import Construct
from resource_stack.resource_stack import ResoureStack

class PipelineStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodbstack = ResoureStack(self,'ResourceStack')