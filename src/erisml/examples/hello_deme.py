        expected_benefit=0.8,
    )
    print("  Option B: Violates rights, high benefit (0.8)")
    print()

    # Step 2: Instantiate an Ethics Module
    print("Step 2: Instantiating RightsFirstEM (rights-first ethics module)...")
    print()
    em = RightsFirstEM()
    print(f"  Ethics Module: {em.em_name}")
    print(f"  Stakeholder: {em.stakeholder}")
    print()

    # Step 3: Evaluate each option
    print("Step 3: Evaluating options with the ethics module...")
    print()

    judgement_a = em.judge(option_a)
    judgement_b = em.judge(option_b)

    # Step 4: Display results
    print("Step 4: Results")
    print()
    print("-" * 70)
    print(f"Option A: {option_a.option_id}")
    print(f"  Verdict: {judgement_a.verdict}")
    print(f"  Normative Score: {judgement_a.normative_score:.3f}")
    print("  Reasons:")
    for reason in judgement_a.reasons:
        print(f"    - {reason}")
    print()

    print("-" * 70)
    print(f"Option B: {option_b.option_id}")
    print(f"  Verdict: {judgement_b.verdict}")
    print(f"  Normative Score: {judgement_b.normative_score:.3f}")
    print("  Reasons:")
    for reason in judgement_b.reasons:
        print(f"    - {reason}")
    print()

    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print()
    print("Key Takeaway:")
    print(
        "  Option A (respects rights) ->",
        judgement_a.verdict,
        f"(score: {judgement_a.normative_score:.3f})",
    )
    print(
        "  Option B (violates rights) ->",
        judgement_b.verdict,
        f"(score: {judgement_b.normative_score:.3f})",
    )
    print()
    print("RightsFirstEM prioritizes rights protection - even if both options")
    print("have the same expected benefit, Option B is forbidden because it")
    print("violates rights.")
    print()
    print("Next Steps:")
    print("  - See triage_ethics_demo.py for multi-option governance")
    print("  - See greek_tragedy_pantheon_demo.py for complex scenarios")
    print("  - Write your own EthicsModule by implementing the EthicsModule protocol")
    print()


if __name__ == "__main__":
    main()
