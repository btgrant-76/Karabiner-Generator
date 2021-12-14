import json
from typing import Dict, Any

MANDATORY = "mandatory"
MANIPULATORS = "manipulators"
L_ONE = "one"
L_TWO = "two"

simple_mappings = {
    "caps_lock": "escape",
    "tab": "grave_accent_and_tilde",
}

layers = {
    "one": {
        MANDATORY: [
            "right_command"
        ],
        "optional": [
            "any"
        ]
    },
    "two": {
        MANDATORY: [
            "right_command",
            "left_control"
        ],
        "optional": [
            "any"
        ]
    },
}

rule_sets: Dict[str, Dict[str, Any]] = {
    "Mercutio Layer 2 VIM navigation": {
        "layer": "two",
        MANIPULATORS: {
            "h": "left_arrow",
            "j": "down_arrow",
            "k": "up_arrow",
            "l": "right_arrow",
        }
    }, "Mercutio Layer 1 NumPad": {
        "layer": "one",
        MANIPULATORS: {
            "e": "1",
            "r": "2",
            "t": "3",
            "d": "4",
            "f": "5",
            "g": "6",
            "c": "7",
            "v": "8",
            "b": "9",
            "n": "0",
        }
    }, "Mercutio Layer 2 F Keys": {
        "layer": "two",
        MANIPULATORS: {
            "e": "f1",
            "r": "f2",
            "t": "f3",
            "d": "f4",
            "f": "f5",
            "g": "f6",
            "c": "f7",
            "v": "f8",
            "b": "f9",
            "n": "f10",
            "m": "f11",
            "comma": "f12",
        }
    }
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


print("[")

comma_mark = len(rule_sets) - 1

for i, rs_name in enumerate(rule_sets.keys()):
    rs = rule_sets[rs_name]
    layer_id: str = rs["layer"]
    layer = layers[rs["layer"]]

    manipulators = rs[MANIPULATORS]

    generated = [generate_rule(from_cd, to_cd, layer) for from_cd, to_cd in rs[MANIPULATORS].items()]
    print(json.dumps(
        {
            "description": rs_name,
            MANIPULATORS: generated
        }, indent=4
    ) + ("" if comma_mark == i else ","))

print("]")
