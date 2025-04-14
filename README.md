<h1>SimpleTimeService</h1>

<p>A minimal Flask-based microservice that returns the current UTC timestamp and the client's IP address in JSON format.</p>

<h2>Features</h2>
<ul>
  <li>Lightweight Flask application</li>
  <li>Containerized using Docker</li>
  <li>Deployed on AWS using Terraform</li>
  <li>Follows best practices: non-root Docker user, minimal image size, and clean infrastructure-as-code</li>
</ul>

<h2>📁 Project Structure</h2>
<pre><code>.
├── app
│   ├── app.py         # Flask application
│   └── Dockerfile     # Docker configuration
└── terraform
    ├── main.tf        # AWS infrastructure setup
    ├── variables.tf   # Input variables
    ├── outputs.tf     # Output values
    ├── provider.tf    # AWS provider configuration
    └── terraform.tfvars # Variable definitions
</code></pre>

<h2>🚀 Prerequisites</h2>
<p>Ensure the following tools are installed:</p>
<ul>
  <li><a href="https://docs.docker.com/get-docker/">Docker</a></li>
  <li><a href="https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html">AWS CLI</a></li>
  <li><a href="https://developer.hashicorp.com/terraform/downloads">Terraform</a></li>
</ul>

<p>Authenticate with AWS:</p>
<pre><code>aws configure</code></pre>
<p>Provide your AWS Access Key ID, Secret Access Key, default region (e.g., <code>us-east-1</code>), and output format (e.g., <code>json</code>).</p>

<h2>🐳 Docker Instructions</h2>

<h3>Build the Docker Image</h3>
<p>Navigate to the <code>app</code> directory and build the Docker image:</p>
<pre><code>cd app
docker build -t yourusername/simple-time-service:latest .
</code></pre>

<h3>Run the Docker Container Locally</h3>
<p>Run the container:</p>
<pre><code>docker run -p 8080:8080 yourusername/simple-time-service:latest
</code></pre>
<p>Access the service at <a href="http://localhost:8080">http://localhost:8080</a>.</p>

<h3>Push the Image to Docker Hub</h3>
<p>Log in to Docker Hub and push the image:</p>
<pre><code>docker login
docker push yourusername/simple-time-service:latest
</code></pre>
<p>Replace <code>yourusername</code> with your actual Docker Hub username.</p>

<h2>☁️ AWS Deployment with Terraform</h2>

<h3>Configure Terraform Variables</h3>
<p>In the <code>terraform</code> directory, edit <code>terraform.tfvars</code> to set your Docker image:</p>
<pre><code>aws_region   = "us-east-1"
docker_image = "yourusername/simple-time-service:latest"
</code></pre>

<h3>Initialize Terraform</h3>
<pre><code>cd terraform
terraform init
</code></pre>

<h3>Review the Execution Plan</h3>
<pre><code>terraform plan
</code></pre>

<h3>Apply the Terraform Configuration</h3>
<pre><code>terraform apply
</code></pre>
<p>Confirm the action when prompted.</p>

<h3>Access the Deployed Service</h3>
<p>After deployment, Terraform will output the Load Balancer DNS:</p>
<pre><code>Outputs:

load_balancer_dns = "your-load-balancer-dns.amazonaws.com"
</code></pre>
<p>Visit <a href="http://your-load-balancer-dns.amazonaws.com">http://your-load-balancer-dns.amazonaws.com</a> to access the service.</p>

<h2>🧹 Cleanup</h2>
<p>To destroy the AWS resources created by Terraform:</p>
<pre><code>terraform destroy
</code></pre>
<p>Confirm the action when prompted.</p>

<h2>🔐 Security Considerations</h2>
<ul>
  <li>Ensure that no sensitive information (e.g., AWS credentials) is committed to version control.</li>
  <li>Use environment variables or AWS IAM roles for managing secrets securely.</li>
</ul>

<h2>📝 Notes</h2>
<ul>
  <li>The application runs as a non-root user within the Docker container for enhanced security.</li>
  <li>The Docker image is built using the slim version of Python to minimize size.</li>
  <li>Terraform configurations follow best practices, including the use of variables and outputs.</li>
</ul>

<h2>📬 Contact</h2>
<p>For any questions or support, please contact <a href="mailto:kewaldangore@gmail.com">kewaldangore@gmail.com</a>.</p>
