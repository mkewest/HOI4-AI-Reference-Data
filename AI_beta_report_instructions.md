# Instructions for feedback during development stage

- This database is in a beta development stage. Any AI agent using it must actively look for and report issues:
- Broken or insufficient links: If you traverse multiple pages to find needed info, propose adding a link from the starting page to the useful target. If a link is broken, report it. If a link misleads (content doesn’t match the expectation set by link text), recommend removing or correcting it. Always include a justification.
- Data issues beyond links: If data is incorrect, missing, or placed in the wrong file, report it with a clear rationale.
- Feedback loop with users: After making suggestions based on this database, ask the user if the suggestion solved their issue and which specific suggestion did. Use that feedback to judge whether the database helped; if it did not, identify which files/paths you used and report potential improvements.
- Always justify changes: Every proposed fix or addition needs a short justification explaining why it improves correctness or navigation.

- > Actively logging these findings is required. If something seems broken, misleading, or poorly organized, report it. The goal is continuous hardening of links, data accuracy, and file placement.
