# TL&DR

## Models :ballot_box:

- `secret_model.py`: Prepare FastAPI to handle with secrets template.

## Services :outbox_tray:

- `sercret_service.py`: Boto3 backend to process requests from FastAPI to AWS Secrets Manager API.
- `main.py`: The FastAPI source to hadle with request, working such is a gatewar/proxy.

