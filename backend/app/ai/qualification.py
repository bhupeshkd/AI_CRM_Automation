class LeadQualification:

    @staticmethod
    def qualify(budget: int, timeline: str):

        score = 0

        if budget >= 1500000:
            score += 50
        elif budget >= 1000000:
            score += 35
        else:
            score += 20

        timeline = timeline.lower()

        if "immediate" in timeline:
            score += 50

        elif "1 month" in timeline:
            score += 35

        elif "3 month" in timeline:
            score += 20

        if score >= 80:
            status = "Hot"

        elif score >= 50:
            status = "Warm"

        else:
            status = "Cold"

        return score, status