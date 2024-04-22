##### Amazon ECR ######

resource "aws_ecr_repository" "ecr-modeltraining" {
  name                 = "modeltraining"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}