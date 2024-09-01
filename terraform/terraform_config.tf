# terraform {
#   required_version = ">= 1.0"

#   required_providers {
#     aws = {
#       source  = "hashicorp/aws"
#       version = ">= 5.30"
#     }
#   }
#   backend "s3" {
#     bucket         = "terraform-state-278141495250"
#     key            = "prod/eks.tfstate"
#     region         = "eu-west-3"
#     acl            = "bucket-owner-full-control"

#   }
# }