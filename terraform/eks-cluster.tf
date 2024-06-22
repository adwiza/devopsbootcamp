provider "kubernetes" {
  host  = data.aws_eks_cluster.myapp-cluster.endpoint
  token = data.aws_eks_cluster_auth.myapp-cluster.token
  #   cluster_ca_certificate = base64decode(data.aws_eks_cluster.myapp-cluster.certificate_authority.0.data)
}

data "aws_eks_cluster" "myapp-cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "myapp-cluster" {
  name = module.eks.cluster_id
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.14.0"

  cluster_name    = "myapp-eks-cluster"
  cluster_version = "1.29"

  subnet_ids = module.myapp-vpc.private_subnets
  vpc_id     = module.myapp-vpc.vgw_id

  tags = {
    environment = "development"
    application = "myapp"
  }

  eks_managed_node_groups = [

    {
      instance_type = ["t2.small"]
      name          = "worker-group-1"
      desired_size  = 3
    },
    {
      instance_type = ["t2.medium"]
      name          = "worker-group-2"
      desired_size  = 1
    }
  ]

}