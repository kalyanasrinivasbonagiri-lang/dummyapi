# Dummy Company API

This service mimics the company student and attendance APIs and returns fixed dummy data.

## Local run

```powershell
pip install -r requirements.txt
python app.py
```

## Local URLs

```text
http://127.0.0.1:8000/api/students?school_id=6
http://127.0.0.1:8000/api/students/6
http://127.0.0.1:8000/api/attendance?school_id=6
```

## Response shape

```json
{
  "status": true,
  "count": 3,
  "school_id": "6",
  "data": [
    {
      "student_name": "pranav",
      "parent_name": "Devaraaja.",
      "contact_number": "9686692994",
      "total_dues": 135000
    },
    {
      "student_name": "nivas",
      "parent_name": "Devaraaja.",
      "contact_number": "7989559217",
      "total_dues": 135000
    }
  ]
}
```

## Attendance and birthday data

```text
http://127.0.0.1:8000/api/attendance?school_id=6
```

The response includes `school_name`, `student_name`, `date`, `date_of_birth`,
`phone_number`, and `parent_name` for the same students.

## Hosting

Render is the fastest option for this small Flask service.

After deployment, use one of these as the backend base URL:

```text
https://your-service.onrender.com/api/students?school_id=
https://your-service.onrender.com/api/students/
```
