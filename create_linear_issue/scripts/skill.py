"""Inert placeholder skill script.

Phase A ships a deterministic, non-executable placeholder. It performs no
network calls, reads no secret VALUES, and is replaced by a real generated
script in a later phase. It exists so scripts/ is a first-class trust-packet
artifact that the validator, publisher, and CI can enforce today.
"""

from __future__ import annotations

import os

# Required runtime environment-variable NAMES (never their values).
REQUIRED_ENV_VAR_NAMES = (
    "SKILL_RUNTIME_API_BASE_URL",
    "SKILL_RUNTIME_API_KEY_NAME",
)


def main() -> None:
    for env_var_name in REQUIRED_ENV_VAR_NAMES:
        # Read the NAME's presence only; never print or log the value.
        _is_present = os.environ.get(env_var_name) is not None
    print("not yet implemented")


if __name__ == "__main__":
    main()
