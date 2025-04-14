variable "aws_region" {
  default = "us-east-1"
}

variable "app_name" {
  default = "simple-time-service"
}

variable "docker_image" {
  description = "Docker image to deploy"
  default     = "yourusername/simple-time-service:latest"
}
