# Stock Data Fetcher

A Python application that fetches stock data from Yahoo Finance and stores it in InfluxDB for time-series analysis.

## Overview

This project provides a data pipeline that:
1. Fetches real-time stock data using the Yahoo Finance API
2. Processes and transforms the data into a suitable format
3. Stores the data in InfluxDB for time-series analysis and visualization

## Features

- Fetches stock data at 1-minute intervals
- Supports multiple stock tickers
- Stores open, high, low, close, and volume data
- Containerized with Docker for easy deployment
- Includes InfluxDB setup for time-series storage

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- InfluxDB 2.x

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd stock_test
   ```

2. Create a `.env` file based on the sample:
   ```bash
   cp env.sample .env
   ```

3. Edit the `.env` file to add your stock tickers:
   ```
   TICKERS=AAPL,MSFT,GOOGL
   ```

4. Start the application with Docker Compose:
   ```bash
   docker compose up --build
   ```

5. Access InfluxDB at http://localhost:8086 with:
   - Username: admin
   - Password: 12345678

## Configuration

The following environment variables can be configured:

| Variable | Description | Default |
|----------|-------------|---------|
| TICKERS | Comma-separated list of stock tickers | (Required) |
| INFLUX_DB_TOKEN | InfluxDB authentication token | admin-token |
| INFLUX_DB_ORG | InfluxDB organization name | stock-ab |
| INFLUX_DB_BUCKET | InfluxDB bucket name | home |
| INFLUX_DB_URL | InfluxDB URL | http://influxdb2:8086 |

## Project Structure

```
stock_test/
├── data_fetcher/         # Main application code
│   ├── main.py           # Entry point for the application
│   └── utils/            # Helper functions
│       └── helpers.py    # Data transformation utilities
├── dockerfile            # Docker configuration
├── docker-compose.yaml   # Docker Compose configuration
├── requirements.txt      # Python dependencies
└── env.sample            # Sample environment variables
```

## Running Without Docker

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   export TICKERS=AAPL,MSFT,GOOGL
   export INFLUX_DB_TOKEN=admin-token
   export INFLUX_DB_ORG=stock-ab
   export INFLUX_DB_BUCKET=home
   export INFLUX_DB_URL=http://localhost:8086
   ```

3. Run the application:
   ```bash
   python -m data_fetcher.main
   ```

## Docker Deployment

See [README.Docker.md](README.Docker.md) for detailed instructions on building and deploying with Docker.

