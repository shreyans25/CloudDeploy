# Cloud deployment guide (optional extension)

## Target architecture
Developer -> GitHub -> GitHub Actions (test/build) -> Docker image -> Elastic Beanstalk environment -> Browser.

## Before deploying
- Review current AWS Elastic Beanstalk and ECR support and pricing in official AWS documentation.
- Create an AWS budget alert.
- Never commit AWS access keys, passwords, or `.env` files to Git.
- For a class demo, follow the currently supported Elastic Beanstalk Docker platform workflow in AWS documentation; console and platform steps can change.

## Suggested manual deployment path
1. Build and test the app locally with Docker.
2. Create an Elastic Beanstalk application and a Docker-based environment using the current AWS console instructions.
3. Package the application using the deployment format currently required by the selected platform.
4. Deploy the package and wait for environment health to become Green/Healthy.
5. Open the environment URL and verify `/` and `/health`.
6. Record screenshots of GitHub Actions success, Docker build, cloud environment health, and the live app.

## Optional fully automated deployment
Extend `.github/workflows/ci.yml` only after the manual deployment works. Prefer GitHub Actions OIDC role assumption over long-lived AWS access keys when supported and configured. Give the role least-privilege permissions. Store non-sensitive configuration as repository variables and secrets only where required. Do not paste credentials into source code.

## Cleanup
Terminate the test environment and delete any related resources that are no longer needed. Check the AWS billing console afterwards. A budget alert is not a hard spending limit.
