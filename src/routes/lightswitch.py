from fastapi import APIRouter
# it prolly works!!
router = APIRouter()


@router.get("/lightswitch/api/service/Fortnite/status")
async def fortnite_status():
    return {
        "serviceInstanceId": "fortnite",
        "status": "UP",
        "message": "Fortnite is online",
        "maintenanceUri": None,
        "overrideCatalogIds": [
            "a7f138b2e51945ffbfdacc1af0541053"
        ],
        "allowedActions": [],
        "banned": False,
        "launcherInfoDTO": {
            "appName": "Fortnite",
            "catalogItemId": "4fe75bbc5a674f4f9b356b5c90567da5",
            "namespace": "fn"
        }
    }


@router.get("/lightswitch/api/service/bulk/status")
async def bulk_status():
    return [
        {
            "serviceInstanceId": "fortnite",
            "status": "UP",
            "message": "fortnite is up.",
            "maintenanceUri": None,
            "overrideCatalogIds": [
                "a7f138b2e51945ffbfdacc1af0541053"
            ],
            "allowedActions": [
                "PLAY",
                "DOWNLOAD"
            ],
            "banned": False,
            "launcherInfoDTO": {
                "appName": "Fortnite",
                "catalogItemId": "4fe75bbc5a674f4f9b356b5c90567da5",
                "namespace": "fn"
            }
        }
    ]
