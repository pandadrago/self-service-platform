# self-service-platform
Web Server that allows users to deploy infrastructure

# What is this?
A simple self-service platform that allows users to request and manage infrastructure and applications through a simple interface

# Why am I building it?
This is a personal project for learning how to design and build  a developer platform from ground up

# What will it do?
Will create applications, databases, manage environments, view deployments, view logs, delete resources, authentication, and automated provisionging

# Technology Road Map
Planned:
- Python
- FastAPI
- PostgreSQL
- Docker
- Terraform
- Kubernetes
- GitHub Actions

# What I learned today
- Virtual environments -> allow for per project dependecies so one doesn't install on user or system level
- How to build a pyproject.toml
- How to build a python project and make it repeatable for others
- The difference between packages, modules, and functions
-- main.py is a module, self_service_platform is a package and typically we are importing main by utilziing the pyproject.toml scripts section. 
--- The scripts section connects a CLI command to a python function
