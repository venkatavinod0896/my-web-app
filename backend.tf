terraform {
  backend "s3" {
    bucket         = "gitops-project-tf-state-bucket-us-east-1"
    key            = "eks/gitops-project/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "gitops-project-terraform-lock-table-us-east-1"
    encrypt        = true
  }
}