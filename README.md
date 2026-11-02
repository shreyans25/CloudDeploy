# CloudDeploy: Automated Cloud Deployment Demo

## Project idea
This project demonstrates cloud deployment tool categories from the classroom slide:
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud-native PaaS:** Amazon Elastic Beanstalk (deployment target)
- **Monitoring:** `/health` endpoint as a basic health check

The included workflow automatically checks the app and builds a Docker image on pushes and pull requests to `main`. It does not deploy to AWS automatically; deployment is described in `DEPLOYMENT.md` so cloud credentials are not required to run the starter project.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000` and `http://127.0.0.1:5000/health`.

## Run with Docker
```bash
docker build -t clouddeploy-demo .
docker run --rm -p 5000:5000 clouddeploy-demo
```
Open `http://localhost:5000`.

## CI/CD
1. Create a GitHub repository and upload these files.
2. Ensure the default branch is `main`.
3. Push a commit or open a pull request.
4. Open the repository's **Actions** tab to see the workflow run.
5. The workflow tests that the app imports correctly and builds a Docker image.

## Scope and limitations
This starter is suitable for a student demonstration. The workflow builds and validates the app but does not publish an image or deploy it to AWS. Production deployment requires secure cloud credentials, environment configuration, logging, monitoring, and cost checks.
