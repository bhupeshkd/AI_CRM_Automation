from datetime import datetime, timedelta


class AppointmentRecommendation:

    @staticmethod
    def generate(
        priority: str,
        qualification_status: str,
        follow_up_in_hours: int,
        vehicle_interest: str,
        purchase_timeline: str,
    ):

        # Default recommendation time
        suggested_datetime = (
            datetime.utcnow() +
            timedelta(hours=follow_up_in_hours or 24)
        )

        # Default meeting type
        meeting_type = "Test Drive"

        # Recommendation status
        status = "Awaiting Confirmation"

        # High intent leads
        if (
            priority.lower() == "high"
            or qualification_status.lower() == "hot"
        ):

            suggested_datetime = datetime.utcnow() + timedelta(hours=24)

        # Medium intent
        elif priority.lower() == "medium":

            suggested_datetime = datetime.utcnow() + timedelta(days=3)

        # Low intent
        else:

            suggested_datetime = datetime.utcnow() + timedelta(days=7)

        return {
            "suggested_appointment_at": suggested_datetime,
            "suggested_meeting_type": meeting_type,
            "appointment_recommendation_status": status,
        }

