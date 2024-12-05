import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_github_cicd_pipeline.aws_github_cicd_pipeline_stack import AwsGithubCicdPipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_github_cicd_pipeline/aws_github_cicd_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsGithubCicdPipelineStack(app, "aws-github-cicd-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
