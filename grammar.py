import language_tool_python

def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    error_count = len(matches)
    words = len(text.split())
    # Compute a "grammar score" (fewer errors = higher score)
    if words == 0:
        return 100, []
    score = max(0, 100 - (error_count / max(words, 1) * 100))
    errors = [match.ruleIssueType + ": " + match.message for match in matches]
    return round(score, 2), errors
