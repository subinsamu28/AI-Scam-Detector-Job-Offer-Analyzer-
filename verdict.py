def get_final_score(
    rule_score,
    nlp_score,
    grammar_score,
    domain_flags,
    entity_flags
):
    # Normalize counts to scale of 0-100 (assume max 5 flags for scaling)
    domain_score = min(len(domain_flags) * 20, 100)
    entity_score = min(len(entity_flags) * 20, 100)

    final = (
        0.30 * rule_score +
        0.35 * nlp_score +
        0.15 * domain_score +
        0.10 * entity_score +
        0.10 * grammar_score
    )

    if final >= 80:
        verdict = "❌ Scam"
    elif final >= 50:
        verdict = "⚠️ Suspicious"
    else:
        verdict = "✅ Likely Safe"

    return int(final), verdict
