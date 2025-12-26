from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI(title="Enterprise Integration Platform Demo")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/services")
def list_services():
    return {
        "services": [
            {
                "id": "integration-001",
                "name": "Order Integration Service",
                "owner": "Integration Platform Team",
                "status": "active"
            }
        ]
    }

@app.get("/services/xml")
def services_xml():
    xml_data = """<?xml version="1.0"?>
<services>
  <service>
    <id>integration-001</id>
    <name>Order Integration Service</name>
    <status>active</status>
  </service>
</services>
"""
    return Response(content=xml_data, media_type="application/xml")
