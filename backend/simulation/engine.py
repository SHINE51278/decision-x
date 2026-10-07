from dataclasses import dataclass


@dataclass
class Incident:
    incident_type: str
    severity: int
    affected_systems: int
    users_affected: int
    data_sensitivity: int
    attack_spread: int


@dataclass
class SimulationResult:
    action: str
    risk_before: float
    risk_after: float
    risk_reduction: float
    spread_probability: float
    business_impact: float
    recovery_time_hours: float
    estimated_cost: float
    residual_risk: str


class SimulationEngine:

    def calculate_risk(self, incident: Incident) -> float:
        """
        Calculate an initial risk score from 0 to 100.
        """

        score = (
            incident.severity * 20
            + min(incident.affected_systems * 5, 20)
            + min(incident.users_affected / 50, 20)
            + incident.data_sensitivity * 2
            + incident.attack_spread * 2
        )

        return round(min(score, 100), 2)

    def simulate(
        self,
        incident: Incident,
        action: str
    ) -> SimulationResult:

        risk_before = self.calculate_risk(incident)

        actions = {
            "isolate_device": {
                "risk_reduction": 0.45,
                "spread_reduction": 0.60,
                "business_impact": 20,
                "recovery_hours": 4,
                "cost_multiplier": 1.2,
            },
            "block_ip": {
                "risk_reduction": 0.30,
                "spread_reduction": 0.40,
                "business_impact": 10,
                "recovery_hours": 2,
                "cost_multiplier": 0.8,
            },
            "disable_account": {
                "risk_reduction": 0.35,
                "spread_reduction": 0.50,
                "business_impact": 15,
                "recovery_hours": 3,
                "cost_multiplier": 0.9,
            },
            "monitor": {
                "risk_reduction": 0.05,
                "spread_reduction": 0.05,
                "business_impact": 5,
                "recovery_hours": 1,
                "cost_multiplier": 0.3,
            },
        }

        if action not in actions:
            raise ValueError(f"Unknown action: {action}")

        config = actions[action]

        risk_after = risk_before * (
            1 - config["risk_reduction"]
        )

        spread_probability = max(
            0,
            incident.attack_spread
            * (1 - config["spread_reduction"])
        )

        business_impact = min(
            100,
            incident.severity * 10
            + config["business_impact"]
        )

        estimated_cost = round(
            (
                incident.affected_systems * 500
                + incident.users_affected * 10
            )
            * config["cost_multiplier"],
            2,
        )

        if risk_after >= 70:
            residual_risk = "CRITICAL"
        elif risk_after >= 50:
            residual_risk = "HIGH"
        elif risk_after >= 30:
            residual_risk = "MEDIUM"
        else:
            residual_risk = "LOW"

        return SimulationResult(
            action=action,
            risk_before=round(risk_before, 2),
            risk_after=round(risk_after, 2),
            risk_reduction=round(
                risk_before - risk_after, 2
            ),
            spread_probability=round(
                spread_probability, 2
            ),
            business_impact=round(
                business_impact, 2
            ),
            recovery_time_hours=config[
                "recovery_hours"
            ],
            estimated_cost=estimated_cost,
            residual_risk=residual_risk,
        )