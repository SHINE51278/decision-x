from simulation.engine import Incident
from recommendation import RecommendationEngine


def main():
    # Create a sample cybersecurity incident
    incident = Incident(
        incident_type="Ransomware",
        severity=5,
        affected_systems=5,
        users_affected=100,
        data_sensitivity=5,
        attack_spread=4,
    )

    # Available response actions
    actions = [
        "isolate_device",
        "block_ip",
        "disable_account",
        "monitor",
    ]

    # Create recommendation engine
    engine = RecommendationEngine()

    # Evaluate all possible actions
    ranked_actions = engine.evaluate_actions(
        incident,
        actions
    )

    # Display results
    print()
    print("=" * 65)
    print("              DECISION X")
    print("        DECISION RECOMMENDATION")
    print("=" * 65)

    print()
    print("Incident:", incident.incident_type)
    print("Severity:", incident.severity)

    print()
    print("-" * 65)

    # Display every action from best to worst
    for position, item in enumerate(
        ranked_actions,
        start=1
    ):
        result = item["result"]

        print()
        print(f"#{position} ACTION: {item['action']}")
        print(f"Decision Score     : {item['score']}")
        print(
            f"Risk               : "
            f"{result.risk_before} -> {result.risk_after}"
        )
        print(
            f"Risk Reduction     : "
            f"{result.risk_reduction}"
        )
        print(
            f"Spread Probability : "
            f"{result.spread_probability}"
        )
        print(
            f"Business Impact    : "
            f"{result.business_impact}"
        )
        print(
            f"Recovery Time      : "
            f"{result.recovery_time_hours} hours"
        )
        print(
            f"Estimated Cost     : "
            f"₹{result.estimated_cost}"
        )
        print(
            f"Residual Risk      : "
            f"{result.residual_risk}"
        )

        print("-" * 65)

    # Select the best action
    best = ranked_actions[0]

    print()
    print("=" * 65)
    print("                 FINAL DECISION")
    print("=" * 65)

    print()
    print(
        f"Recommended Action : "
        f"{best['action']}"
    )

    print(
        f"Decision Score     : "
        f"{best['score']}"
    )

    print()
    print(
        "Reason: This action provides the "
        "best overall balance between "
        "risk reduction, attack spread, "
        "business impact, and recovery time."
    )

    print()
    print("=" * 65)


if __name__ == "__main__":
    main()