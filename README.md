Assignment 1 - CI/CD Pipeline with Jenkins + Docker
🎯 Objective

Set up a local Jenkins pipeline that builds, tests, and runs a Dockerized Python Flask app.

🧰 Tech Stack

Python 3.11 (Flask App)

Docker

Jenkins (running in Docker)

GitHub (SCM Source)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/beastguhan/one-data-structure.git
cd one-data-structure

2️⃣ Run Jenkins in Docker
docker run -d \
  -u root \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

3️⃣ Configure Jenkins

Install Docker, Pipeline, and Git plugins.

Create a new Pipeline job.

In the job configuration, choose Pipeline script from SCM:

SCM: Git

Repository URL: https://github.com/beastguhan/one-data-structure.git

Branch: main

Script path: assignment/Jenkinsfile

4️⃣ Run the Pipeline

Then run the pipeline in Jenkins.

5️⃣ Verify the Application

Verified by visiting:
 http://localhost:5000

✅ Pipeline successfully executed and Flask app verified
