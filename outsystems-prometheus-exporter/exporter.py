"""Application exporter"""

import os
import time
from prometheus_client import start_http_server, Gauge, Info
import requests

class AppMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, app_port=80, polling_interval_seconds=5):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds

        # Prometheus metrics to collect
        self.outsystems_official_space_used = Gauge("outsystems_official_space_used", "Space Used")
        self.outsystems_production_space_used = Gauge("outsystems_production_space_used", "Space Used")
        self.outsystems_test_space_used = Gauge("outsystems_test_space_used", "Space Used")
        self.outsystems_dev_space_used = Gauge("outsystems_dev_space_used", "Space Used")


    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """

        try:
            # Fetch raw status data from the application
            resp = requests.get(url=f"https://hss.outsystemscloud.com/DBSpaceMonitor/rest/v1/GetSpace")        
            status_data = resp.json()
            # Update Prometheus metrics with application metrics
            self.outsystems_production_space_used.set(status_data["SpaceUsed"])
        except:
            self.outsystems_production_space_used.set(0.0)

        try:
            resp = requests.get(url=f"https://personal-8gsrdrii.outsystemscloud.com/DBSpaceMonitor/rest/v1/GetSpace")
            status_data = resp.json()
            self.outsystems_official_space_used.set(status_data["SpaceUsed"])
        except:
            self.outsystems_official_space_used.set(0.0)

        try:
            resp = requests.get(url=f"https://personal-kzik9eqs.outsystemscloud.com/DBSpaceMonitor/rest/v1/GetSpace")
            status_data = resp.json()
            self.outsystems_test_space_used.set(status_data["SpaceUsed"])
        except:
            self.outsystems_test_space_used.set(0.0)

        try:
            resp = requests.get(url=f"https://personal-tnshps7f.outsystemscloud.com/DBSpaceMonitor/rest/v1/GetSpace")
            status_data = resp.json()
            self.outsystems_dev_space_used.set(status_data["SpaceUsed"])
        except:
            self.outsystems_dev_space_used.set(0.0)

        
def main():
    """Main entry point"""

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    app_port = int(os.getenv("APP_PORT", "9877"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()