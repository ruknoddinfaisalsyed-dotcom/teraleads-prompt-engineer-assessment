import json

appointments_json = """
[
    {"name": "Rahul Sharma", "phone": "9876543210", "date": "March 12", "time": "4:00 PM"},
    {"name": "Priya Mehta", "phone": "9123456780", "date": "March 13", "time": "11:30 AM"},
    {"name": "Amit Verma", "phone": "9988776655", "date": "March 14", "time": "2:00 PM"}
]
"""

def generate_reminder(appointment_data):

    for appt in appointment_data:

        message = f"""
<friendly tone>

Hello {appt['name']},

<pause:400ms>

This is a reminder for your appointment on {appt['date']} at {appt['time']}.

<pause:500ms>

If you need to reschedule, please contact us.
"""

        print(message)

data = json.loads(appointments_json)
generate_reminder(data)
