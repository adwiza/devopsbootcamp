# provider "aws" {
#   region = local.region
# }

# data "terraform_remote_state" "vpc" {
#   backend = "s3"
#   config = {
#     bucket = "terraform-state-278141495250"
#     key = "prod/vpc.tfstate" 
#     region = "us-east-1" 
#   }
# }

# data "terraform_remote_state" "ec2" {
#   backend = "s3"
#   config = {
#     bucket = "terraform-state-278141495250"
#     key = "prod/ec2.tfstate" 
#     region = "us-east-1" 
#   }
# }

# data "terraform_remote_state" "sso" {
#   backend = "s3"
#   config = {
#     bucket = "terraform-state-278141495250"
#     key = "prod/sso.tfstate" 
#     region = "us-east-1" 
#   }
# }

# data "aws_availability_zones" "available" {}

# locals {
#   name   = "prod"
#   region = "us-east-1"

#   vpc_cidr = "10.0.0.0/16"
#   azs      = slice(data.aws_availability_zones.available.names, 0, 3)

#   tags = {
#     Name    = local.name
#     Env = "prod"
#     Product  = "Sociala"
#   }
# }

# provider "kubernetes" {
#   host                   = module.prod-eks.cluster_endpoint
#   cluster_ca_certificate = base64decode(module.prod-eks.cluster_certificate_authority_data)

#   exec {
#     api_version = "client.authentication.k8s.io/v1beta1"
#     command     = "aws"
#     # This requires the awscli to be installed locally where Terraform is executed
#     args = ["eks", "get-token", "--cluster-name", module.prod-eks.cluster_name]
#   }
# }

