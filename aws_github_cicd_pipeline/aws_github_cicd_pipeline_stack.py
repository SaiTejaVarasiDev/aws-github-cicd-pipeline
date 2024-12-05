from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

class AwsGithubCicdPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, 
                                "Pipeline",
                                pipeline_name="MyPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub("SaiTejaVarasiDev/aws-github-cicd-pipeline","main",connection_arn="arn:aws:codeconnections:ap-south-1:332781466400:connection/6cf28f10-5deb-4879-b584-b90724473245"),
                                commands=["npm install -g aws-cdk",
                                          "python -m pip install -r requirements.txt",
                                          "cdk synth"]
                                )
                                
                                )
