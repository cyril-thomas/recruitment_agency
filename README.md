# Recruitment Agency Crew

Welcome to the Recruitment Agency Crew project, powered by [crewAI](https://crewai.com). This is my attempt at building services and utilizing agentic AI to perform RAG tasks.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Environment variables needed

**Add the following API keys into the `.env` file**
- `OPENAI_API_KEY`
- `SERPER_API_KEY`


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the recruitment_agency Crew, assembling the agents and assigning them tasks as defined in your configuration.
**Ensure you add resumes with .pdf extension to the /files folder**
As a pre-requist, have a server running on `localhost:8000/users`

## The Recruitmet Agency Crew details


### Agents
The recruitment agency crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
- `recruitment_data_analyst` Agent who analysis the resumes provided to capture information about the candidates that are relavant to jobs.
-  `sr_python_dev` Agent who performs coding tasks to digitalize the candidate information to allow for future lookups.

### Tasks
The agency performs the following tasks
- `data_extraction_task` Agents analyze the resumes to extract relevant information and santize the data by looking up information on the internet.
- `rest_development_task` Agent utilizes custom tool to publish candidate information to a service to store in the database.

### Tools
- `PostToAPITool` Leveraging python's requests module to `POST` data to an REST API endpoint.
