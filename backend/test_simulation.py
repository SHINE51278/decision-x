from simulation.engine import Incident, SimulationEngine


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

    # Create the simulation engine
    engine = SimulationEngine()

    # Actions we want to compare
    actions = [
        "isolate_device",
        "block_ip",
        "disable_account",
        "monitor",
    ]

    print()
    print("=" * 60)
    print("        DECISION X - CYBERSECURITY SIMULATION")
    print("=" * 60)

    print()
    print("Incident Type       :", incident.incident_type)
    print("Severity            :", incident.severity)
    print("Affected Systems    :", incident.affected_systems)
    print("Users Affected     :", incident.users_affected)
    print("Data Sensitivity    :", incident.data_sensitivity)
    print("Attack Spread       :", incident.attack_spread)

    print()
    print("-" * 60)
    print("                    SIMULATION RESULTS")
    print("-" * 60)

    for action in actions:

        result = engine.simulate(
            incident,
            action
        )

        print()
        print("Action              :", result.action)
        print("Risk Before         :", result.risk_before)
        print("Risk After          :", result.risk_after)
        print("Risk Reduction      :", result.risk_reduction)
        print("Spread Probability  :", result.spread_probability)
        print("Business Impact     :", result.business_impact)
        print("Recovery Time       :", result.recovery_time_hours, "hours")
        print("Estimated Cost      : ₹", result.estimated_cost)
        print("Residual Risk       :", result.residual_risk)

        print("-" * 60)


if __name__ == "__main__":
    main()