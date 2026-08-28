from __future__ import annotations

import os

from flask import Flask, jsonify, request


STUDENTS = [
    {
        "student_name": "pranav",
        "parent_name": "Devaraaja.",
        "contact_number": "9686692994",
        "total_dues": 135000,
    },
    {
        "student_name": "nivas",
        "parent_name": "Devaraaja.",
        "contact_number": "7989559217",
        "total_dues": 135000,
    },
      {
            "student_name": "yukash",
            "parent_name": "Devaraaja.",
            "contact_number": "7989559217",
            "total_dues": 135000,
        }

]

ATTENDANCE_RECORDS = [
    {
        "school_name": "Dummy School",
        "student_name": "pranav",
        "date": "2026-08-25",
        "date_of_birth": "2008-08-28",
        "phone_number": "9686692994",
        "parent_name": "Devaraaja.",
        "ATTENDANCE_STATUS":"A"
    },
    {
        "school_name": "Dummy School",
        "student_name": "nivas",
        "date": "2026-08-25",
        "date_of_birth": "2008-08-28",
        "phone_number": "7989559217",
        "parent_name": "Devaraaja.",
        "ATTENDANCE_STATUS":"A"
    },
    {
        "school_name": "Dummy School",
        "student_name": "yukash",
        "date": "2026-08-25",
        "date_of_birth": "2009-01-27",
        "phone_number": "7708866836",
        "parent_name": "Devaraaja.",
        "ATTENDANCE_STATUS":"A"
    },
]


def create_app() -> Flask:
    app = Flask(__name__)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET,OPTIONS"
        return response

    @app.get("/")
    def root():
        return jsonify(
            {
                "service": "dummy-company-api",
                "status": "ok",
                "students_endpoint": "/api/students?school_id=<school_id>",
            }
        )

    @app.route("/api/students", methods=["GET", "OPTIONS"])
    def get_students():
        if request.method == "OPTIONS":
            return ("", 204)

        school_id = (request.args.get("school_id") or "").strip()
        return jsonify(
            {
                "status": True,
                "count": len(STUDENTS),
                "school_id": school_id,
                "data": STUDENTS,
            }
        )

    @app.route("/api/students/<school_id>", methods=["GET", "OPTIONS"])
    def get_students_by_path(school_id: str):
        if request.method == "OPTIONS":
            return ("", 204)

        return jsonify(
            {
                "status": True,
                "count": len(STUDENTS),
                "school_id": school_id,
                "data": STUDENTS,
            }
        )

    @app.route("/api/attendance", methods=["GET", "OPTIONS"])
    def get_attendance():
        if request.method == "OPTIONS":
            return ("", 204)

        school_id = (request.args.get("school_id") or "").strip()
        return jsonify(
            {
                "status": True,
                "count": len(ATTENDANCE_RECORDS),
                "school_id": school_id,
                "data": ATTENDANCE_RECORDS,
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
