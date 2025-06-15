# log-playground

Self contained log flow tester for Datadog

## Prerequisites

Make sure Docker and Docker Compose are installed. On Ubuntu you can install
them with:

```bash
sudo apt-get update && sudo apt-get install -y docker docker-compose
```

## Usage

1. Build and start the environment with Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. Containers:
   - **log-generator**: Emits log messages continuously (about 10 lines per second).
   - **datadog-agent**: Collects logs from all containers and forwards them to the
     Observability Pipelines container using HTTP.
   - **observability-pipelines**: Receives logs and writes them to a file in the
     `bitbucket` directory (`output.log`).
   - **viewer**: Tails `output.log` so you can watch the log flow.

3. Stop the stack with `Ctrl+C` and `docker-compose down`.

> **Note**: The Observability Pipelines container image requires a valid
> Datadog license. Ensure you have access to `gcr.io/datadoghq/observability-pipelines`
> or replace it with your own image.
