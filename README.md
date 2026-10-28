# SecureFlow — Automated DevSecOps Security Pipeline

SecureFlow is a Python Flask application integrated with GitLab CI/CD to automate testing, security scanning, code quality analysis, and Docker image publishing.

## Tech Stack

- **Application:** Python, Flask, Pytest
- **SAST:** Semgrep
- **Secret Detection:** Gitleaks
- **Code Quality:** SonarQube Cloud
- **Container Scanning:** Trivy
- **Containerization:** Docker
- **CI/CD & Registry:** GitLab CI/CD, GitLab Container Registry

## Pipeline Workflow

```text
Git Push
   |
   v
Test (Pytest)
   |
   v
Security Scans
   |-- Semgrep
   |-- Gitleaks
   |-- Trivy
   |-- SonarQube Cloud
   |
   v
Build & Publish Docker Image