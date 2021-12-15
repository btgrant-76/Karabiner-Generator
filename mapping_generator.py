import json
from typing import Dict, Any

MANDATORY = "mandatory"
MANIPULATORS = "manipulators"
L_ONE = "one"
L_TWO = "two"

BASE_MODIFIER = "right_shift"

simple_mappings = {
    "caps_lock": "escape",
    "tab": "grave_accent_and_tilde",
}

layers = {
    "one": {
        MANDATORY: [
            BASE_MODIFIER
        ],
        "optional": [
            "any"
        ]
    },
    "two": {
        MANDATORY: [
            BASE_MODIFIER,
            "left_shift"
        ],
        "optional": [
            "any"
        ]
    },
    "three": {
        MANDATORY: [
            BASE_MODIFIER,
            "tab"
        ],
        "optional": [
            "any"
        ]
    }
}

rule_sets: Dict[str, Dict[str, Any]] = {
    "Mercutio Layer 2 VIM navigation": {
        "layer": "one",
        MANIPULATORS: {
            "h": "left_arrow",
            "j": "down_arrow",
            "k": "up_arrow",
            "l": "right_arrow",
        }
    },
    # "Mercutio Layer 1 NumPad": {
    #     "layer": "one",
    #     MANIPULATORS: {
    #         "e": "1",
    #         "r": "2",
    #         "t": "3",
    #         "d": "4",
    #         "f": "5",
    #         "g": "6",
    #         "c": "7",
    #         "v": "8",
    #         "b": "9",
    #         "n": "0",
    #     }
    # },
    # "Mercutio Layer 2 F Keys": {
    #     "layer": "two",
    #     MANIPULATORS: {
    #         "e": "f1",
    #         "r": "f2",
    #         "t": "f3",
    #         "d": "f4",
    #         "f": "f5",
    #         "g": "f6",
    #         "c": "f7",
    #         "v": "f8",
    #         "b": "f9",
    #         "n": "f10",
    #         "m": "f11",
    #         "comma": "f12",
    #     }
    # }
    "Mercutio Numbers": {
        "layer": "one",
        MANIPULATORS: {
            "q": "1",
            "w": "2",
            "e": "3",
            "r": "4",
            "t": "5",
            "y": "6",
            "u": "7",
            "i": "8",
            "o": "9",
            "p": "0",
        }
    },
    "Mercutio F-Keys": {
        "layer": "two",
        MANIPULATORS: {
            "q": "f1",
            "w": "f2",
            "e": "f3",
            "r": "f4",
            "t": "f5",
            "y": "f6",
            "u": "f7",
            "i": "f8",
            "o": "f9",
            "p": "f10",
            "a": "f11",
            "s": "f12",
        }
    },
    "Mercutio Navigation": {
        "layer": "two",
        MANIPULATORS: {
            "h": "page_up",
            "j": "page_down",
            "k": "home",
            "l": "end",
        }
    },
    "Mercutio Punctuation": {
        "layer": "one",
        MANIPULATORS: {
            "tab": "grave_accent_and_tilde",
            "x": "backslash",
            "c": "slash",
            "v": "quote",
            "b": "semicolon",
            "n": "hyphen",
            "m": "equal_sign",
            "comma": "open_bracket",
            "period": "close_bracket",
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
