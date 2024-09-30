#!/bin/bash

# Move into the correct directory where the FastAPI app is located
cd RCWA1001P1

# Run the FastAPI + Dash app using Uvicorn
uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8002 --workers 1