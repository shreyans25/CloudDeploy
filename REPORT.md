# CLOUD COMPUTING PROJECT REPORT
## CloudDeploy: Automated Deployment of a Containerized Web Application Using Docker and GitHub Actions

**Student Name:** ______________________________  
**Register Number:** ___________________________  
**Department:** Computer Science and Engineering  
**Institution:** ________________________________  
**Faculty:** ____________________________________  
**Course:** Cloud Computing  

## 1. Project Title
CloudDeploy: Automated Deployment of a Containerized Web Application Using Docker and GitHub Actions.

## 2. Student Details
Complete the student and institution fields on the cover page before submission.

## 3. Abstract (approximately 300 words)
Modern applications are updated frequently, and manually testing and deploying every change can be slow and error-prone. Cloud-native development practices address this challenge by combining containerization, continuous integration, and cloud platforms. This project, CloudDeploy, demonstrates a basic automated workflow for packaging and validating a web application before cloud deployment.

The application is a small Python Flask website that explains its own deployment pipeline and provides a health-check endpoint. Docker packages the application and its dependencies into a container image, making the runtime environment more consistent across development and deployment machines. GitHub Actions runs automatically when code is pushed to the main branch or a pull request is opened. The workflow checks out the source code, sets up Python, installs dependencies, verifies that the application can be imported, and builds the Docker image. This provides an early indication of basic errors before the application is released.

The project connects three categories of cloud deployment tools presented in class: containerization through Docker, CI/CD through GitHub Actions, and cloud-native Platform as a Service through a proposed deployment target such as Amazon Elastic Beanstalk. A health endpoint provides a simple way to verify that the application responds after it is started. The deployment guide describes a manual cloud deployment path and outlines how a secure automated deployment could be added later.

The implementation is intentionally small so students can understand each stage and demonstrate it in a laboratory setting. The included starter workflow builds and validates the application but does not deploy to a live cloud account by itself. Actual cloud deployment must be completed separately, using current provider instructions and properly configured permissions. Evaluation can include a successful local run, a Docker container run, a passing GitHub Actions workflow, and—if deployed—a screenshot of the live cloud application. The project also emphasizes secure handling of credentials, least-privilege access, budget alerts, and resource cleanup. It offers a foundation for extending the pipeline with container registries, infrastructure as code, monitoring dashboards, and automated releases.

## 4. Problem Statement
Manual deployment often requires repeating setup and validation steps after each code change. Differences between development environments can cause failures, and mistakes may not be discovered until the application is deployed. The objective is to demonstrate a repeatable workflow that validates source code and packages an application into a portable container before cloud deployment.

### Objectives
1. Build a small web application.
2. Package it using Docker.
3. Automate basic checks and image building with GitHub Actions.
4. Demonstrate a health endpoint.
5. Document a cloud deployment path and security considerations.

## 5. Technologies Required
| Tool | Category | Use |
|---|---|---|
| Python + Flask | Application framework | Serves the demo website and health endpoint |
| Docker | Containerization | Packages app and dependencies |
| GitHub Actions | CI/CD | Runs checks and builds the image on code changes |
| Amazon Elastic Beanstalk | Cloud-native PaaS target | Optional hosting/deployment environment |
| Browser | Testing | Verifies the app and health endpoint |

## 6. Implementation and Results

### 6.1 Architecture
Developer commits code to GitHub. GitHub Actions checks out the code, installs Python dependencies, checks that the Flask app imports, and builds a Docker image. The image can then be deployed to a compatible cloud runtime. In this starter version, the cloud deployment is a documented optional step rather than an automated workflow stage.

### 6.2 Implementation files
- `app.py`: Flask website and `/health` endpoint.
- `requirements.txt`: application dependencies.
- `Dockerfile`: container build instructions.
- `.github/workflows/ci.yml`: automated build and validation workflow.
- `DEPLOYMENT.md`: cloud deployment and cleanup guide.

### 6.3 Run and test
1. Install Python 3.12 or a compatible version.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `python app.py` and open `http://127.0.0.1:5000`.
4. Open `/health`; expected response is JSON containing a healthy status.
5. Build and run the Docker image using the commands in README.md.
6. Push the files to a GitHub repository on branch `main`.
7. Open the Actions tab and verify the workflow succeeds.
8. If deploying to a cloud platform, capture the real deployed URL and health status.

### 6.4 Expected results
- The website opens locally.
- The `/health` endpoint returns HTTP 200 and a JSON status.
- Docker builds the image without errors.
- GitHub Actions runs on pushes and pull requests and reports a passing job when all steps succeed.
- If the optional cloud deployment is completed, the public environment URL serves the app.

Do not report cloud deployment as completed until you have deployed it and verified the live URL.

### 6.5 Screenshots to add
1. Local website open in a browser.
2. `/health` endpoint output.
3. Successful Docker build in terminal.
4. GitHub Actions workflow showing success.
5. Optional: cloud platform environment health and live website.

### 6.6 Security and cost
Never commit credentials to the repository. Use least-privilege permissions and short-lived credentials where possible. Configure a budget alert and check provider pricing. Delete unused cloud resources after evaluation.

## 7. Conclusion
CloudDeploy demonstrates how containerization and CI/CD can make an application workflow more repeatable. Docker packages the app, while GitHub Actions automates basic validation and image building whenever code changes. The project also illustrates how a cloud-native PaaS can be used as a deployment target. Its modular structure makes it suitable for extensions such as publishing images to a registry, automated deployment, infrastructure as code with Terraform, and monitoring with Prometheus and Grafana.

## 8. References
1. Docker documentation: https://docs.docker.com/
2. GitHub Actions documentation: https://docs.github.com/actions
3. Flask documentation: https://flask.palletsprojects.com/
4. AWS Elastic Beanstalk documentation: https://docs.aws.amazon.com/elasticbeanstalk/
5. AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/
