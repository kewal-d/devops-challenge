# devops-challenge
SimpleTimeService
A minimal Flask-based microservice that returns the current UTC timestamp and the client's IP address in JSON format.​

Features
Lightweight Flask application​

Containerized using Docker​

Deployed on AWS using Terraform​
GitHub

Follows best practices: non-root Docker user, minimal image size, and clean infrastructure-as-code​

📁 Project Structure
.
├── app
│   ├── app.py         # Flask application
│   └── Dockerfile     # Docker configuration
└── terraform
    ├── main.tf        # AWS infrastructure setup
    ├── variables.tf   # Input variables
    ├── outputs.tf     # Output values
    ├── provider.tf    # AWS provider configuration
    └── terraform.tfvars # Variable definitions

🚀 Prerequisites
Ensure the following tools are installed:

Docker​

AWS CLI​

Terraform​

Authenticate with AWS:​

aws configure

Provide your AWS Access Key ID, Secret Access Key, default region (e.g., us-east-1), and output format (e.g., json).​

🐳 Docker Instructions
Build the Docker Image
Navigate to the app directory and build the Docker image:​

cd app
docker build -t yourusername/simple-time-service:latest .
Run the Docker Container Locally
Run the container:​


docker run -p 8080:8080 yourusername/simple-time-service:latest
Access the service at http://localhost:8080.​

Push the Image to Docker Hub
Log in to Docker Hub and push the image:​


docker login
docker push yourusername/simple-time-service:latest
Replace yourusername with your actual Docker Hub username.​

☁️ AWS Deployment with Terraform
Configure Terraform Variables
In the terraform directory, edit terraform.tfvars to set your Docker image:​


aws_region   = "us-east-1"
docker_image = "yourusername/simple-time-service:latest"
Initialize Terraform

cd terraform
terraform init
Review the Execution Plan

terraform plan
Apply the Terraform Configuration

terraform apply
Confirm the action when prompted.​

Access the Deployed Service
After deployment, Terraform will output the Load Balancer DNS:​


Outputs:

load_balancer_dns = "your-load-balancer-dns.amazonaws.com"
Visit http://your-load-balancer-dns.amazonaws.com to access the service.​

🧹 Cleanup
To destroy the AWS resources created by Terraform:​


terraform destroy
Confirm the action when prompted.​

🔐 Security Considerations
Ensure that no sensitive information (e.g., AWS credentials) is committed to version control.​

Use environment variables or AWS IAM roles for managing secrets securely.​

📝 Notes
The application runs as a non-root user within the Docker container for enhanced security.​

The Docker image is built using the slim version of Python to minimize size.​

Terraform configurations follow best practices, including the use of variables and outputs.​

📬 Contact
For any questions or support, please contact kewaldangore@gmail.com.​
