import json
import sys
from typing import Dict, Any

MANDATORY = "mandatory"
MANIPULATORS = "manipulators"
L_ONE = "one"
L_TWO = "two"
L_THREE = "three"

BASE_MODIFIER = "right_command"

simple_mappings = {
    # "caps_lock": "escape",
    # "tab": "grave_accent_and_tilde",
    "right_shift": "slash"
}


def generate_rule(from_code: str, to_code: str, modifiers: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "from": {
            "key_code": from_code,
            "modifiers": modifiers
        },
        "to": [
            {
                "key_code": to_code
            }
        ],
        "type": "basic"
    }


def generate_simple_modification(from_code: str, to_code: str) -> Dict[str, Any]:
    return {
        "from": {
            "key_code": from_code
        },
        "to": [
            {
                "key_code": to_code
            }
        ]
    }


if len(sys.argv) == 2:
    print("please provide layer definition and rule sets files")
    exit(-1)

layer_def_file = sys.argv[1].strip()
print(f"layer definition file is '{layer_def_file}'")
rule_sets_file = sys.argv[2].strip()
print(f"rule sets file is '{rule_sets_file}'")

with open(layer_def_file, encoding="utf8", mode="r") as layer_definitions:
    layers = json.load(layer_definitions)

    with open(rule_sets_file, encoding="utf8", mode="r") as rule_sets_file:
        json_rule_sets = json.load(rule_sets_file)

        complex_modification_rules = json_rule_sets["staticComplexRules"]

        rule_sets = json_rule_sets["complexModificationRules"]

        for i, rs_name in enumerate(rule_sets.keys()):
            rs = rule_sets[rs_name]
            layer_id: str = rs["layer"]
            layer = layers[rs["layer"]]

            manipulators = rs[MANIPULATORS]

            generated = [generate_rule(from_cd, to_cd, layer) for from_cd, to_cd in rs[MANIPULATORS].items()]
            complex_modification_rules.append(
                {
                    "description": rs_name,
                    MANIPULATORS: generated
                }
            )

        print(json.dumps(complex_modification_rules, indent=4))
