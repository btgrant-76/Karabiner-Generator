import json
from typing import Dict, Any

simple_mappings = {
    "caps_lock": "escape",
    "tab": "grave_accent_and_tilde",
}

layers = {
    "one": {
        "mandatory": [
            "right_command",
            "left_control"
        ],
        "optional": [
            "any"
        ]
    },
    "two": {
        "mandatory": [
            "right_command"
        ],
        "optional": [
            "any"
        ]
    },
}

rule_sets: Dict[str, Dict[str, Any]] = {
    "Mercutio Layer 2 VIM navigation": {
        "layer": "two",
        "manipulators": {
            "h": "left_arrow",
            "j": "down_arrow",
            "k": "up_arrow",
            "l": "right_arrow",
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


for rs_name in rule_sets.keys():
    rs = rule_sets[rs_name]
    layer_id: str = rs["layer"]
    layer = layers[rs["layer"]]
    # print(f"{rs_name} is in layer {layer_id}")

    manipulators = rs["manipulators"]
    # print(f"manipulators: {manipulators}")
    # for from_cd, to_cd in rs["manipulators"].items():
    # print(f"{from_cd} to {to_cd}")
    # print(generate_rule(from_cd, to_cd, layer))

    generated = [generate_rule(from_cd, to_cd, layer) for from_cd, to_cd in rs["manipulators"].items()]
    print(json.dumps(
        {
            "description": rs_name,
            "manipulators": generated
        }, indent=4
    ))

# print(generate_rule("foo", "bar"))

# for rule_desc in rule_sets.keys():
#     print(rule_desc)
