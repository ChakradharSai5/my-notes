
from notion_client import Client
from datetime import datetime, timedelta

# ===== CONFIG =====
import os
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = "7fa4438ee3fc422aa2de05cb365624bc"

notion = Client(auth=NOTION_TOKEN)

# ===== QUERY =====
response = notion.databases.query(
    database_id=DATABASE_ID,
    filter={
        "and": [
            {
                "property": "Done",
                "checkbox": {
                    "equals": False
                }
            },
            {
                "or": [
                    {
                        "property": "Priority Type",
                        "select": {
                            "equals": "Urgent"
                        }
                    },
                    {
                        "property": "Thing of this Fortnight??",
                        "formula": {
                            "checkbox": {
                                "equals": True
                            }
                        }
                    }
                ]
            }
        ]
    }
)

# ===== PROCESS TASKS =====
for page in response["results"]:

    props = page["properties"]

    final_due_data = props["Final Due Date"]["formula"]["date"]

    if final_due_data is None:
        continue

    final_due = final_due_data["start"]

    # ===== CORRECT DATE HANDLING =====
    if "T" in final_due:
        # Case 1: UTC datetime → convert to IST
        dt = datetime.fromisoformat(final_due.replace("Z", ""))
        dt_ist = dt + timedelta(hours=5, minutes=30)
        date_only = dt_ist.date().isoformat()
    else:
        # Case 2: Already a date → TRUST it
        date_only = final_due


    # ===== UPDATE =====
    notion.pages.update(
        page_id=page["id"],
        properties={
            "Calendar Due Date": {
                "date": {
                    "start": date_only
                }
            }
        }
    )

print("\nCalendar sync completed.")
