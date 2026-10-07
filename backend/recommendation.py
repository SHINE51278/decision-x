from simulation.engine import SimulationEngine


class RecommendationEngine:
    """
    Compares cybersecurity response actions
    and recommends the best available decision.
    """

    def __init__(self):
        self.simulation_engine = SimulationEngine()

    def calculate_score(self, result):
        """
        Calculate a decision score from 0 to 100.

        Higher score = better cybersecurity decision.
        """

        # Normalize risk reduction
        risk_score = min(
            result.risk_reduction / 50,
            1
        ) * 40

        # Lower attack spread is better
        spread_score = max(
            0,
            1 - (result.spread_probability / 5)
        ) * 25

        # Lower business impact is better
        business_score = max(
            0,
            1 - (result.business_impact / 100)
        ) * 15

        # Faster recovery is better
        recovery_score = max(
            0,
            1 - (result.recovery_time_hours / 10)
        ) * 10

        # Lower cost is better
        cost_score = max(
            0,
            1 - (result.estimated_cost / 10000)
        ) * 10

        total_score = (
            risk_score
            + spread_score
            + business_score
            + recovery_score
            + cost_score
        )

        return round(
            max(0, min(total_score, 100)),
            2
        )

    def evaluate_actions(self, incident, actions):
        """
        Simulate every available action
        and rank them from best to worst.
        """

        results = []

        for action in actions:

            result = self.simulation_engine.simulate(
                incident,
                action
            )

            score = self.calculate_score(result)

            results.append({
                "action": action,
                "result": result,
                "score": score,
            })

        results.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return results

    def recommend(self, incident, actions):
        """
        Return the highest-scoring action.
        """

        ranked_actions = self.evaluate_actions(
            incident,
            actions
        )

        if not ranked_actions:
            raise ValueError(
                "No actions available for recommendation."
            )

        return ranked_actions[0]

    def explain(self, result):
        """
        Explain why an action is considered effective
        and identify important trade-offs.
        """

        reasons = []
        tradeoffs = []

        if result.risk_reduction >= 35:
            reasons.append(
                "Strong risk reduction"
            )

        if result.spread_probability <= 2:
            reasons.append(
                "Low attack spread probability"
            )

        if result.residual_risk == "LOW":
            reasons.append(
                "Low residual risk"
            )
        elif result.residual_risk == "HIGH":
            reasons.append(
                "Residual risk remains high"
            )
        elif result.residual_risk == "CRITICAL":
            tradeoffs.append(
                "Residual risk remains critical"
            )

        if result.recovery_time_hours <= 2:
            reasons.append(
                "Fast recovery"
            )
        else:
            tradeoffs.append(
                f"Recovery may take "
                f"{result.recovery_time_hours} hours"
            )

        if result.estimated_cost <= 3000:
            reasons.append(
                "Relatively low estimated cost"
            )
        else:
            tradeoffs.append(
                f"Estimated cost is "
                f"₹{result.estimated_cost}"
            )

        return {
            "reasons": reasons,
            "tradeoffs": tradeoffs,
        }