import json
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

layers = {
    L_ONE: {
        MANDATORY: [
            BASE_MODIFIER
        ],
        "optional": [
            "any"
        ]
    },
    L_TWO: {
        MANDATORY: [
            BASE_MODIFIER,
            "left_control"
        ],
        "optional": [
            "any"
        ]
    },
    L_THREE: {
        MANDATORY: [
            "left_control",
            "left_shift"
        ],
        "optional": [
            "any"
        ]
    }
}

rule_sets: Dict[str, Dict[str, Any]] = {
    "Mercutio VIM navigation": {
        "layer": L_ONE,
        MANIPULATORS: {
            "h": "left_arrow",
            "j": "down_arrow",
            "k": "up_arrow",
            "l": "right_arrow",
        }
    },
    # "Mercutio Layer 1 NumPad": {
    #     "layer": L_ONE,
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
    #     "layer": L_TWO,
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
        "layer": L_ONE,
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
        "layer": L_THREE,
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
        "layer": L_THREE,
        MANIPULATORS: {
            "h": "home",
            "j": "page_down",
            "k": "page_up",
            "l": "end",
        }
    },
    "Mercutio Punctuation": {
        "layer": L_ONE,
        MANIPULATORS: {
            "tab": "grave_accent_and_tilde",
            "slash": "backslash",
            # "x": "backslash",
            # "c": "slash",
            # "d": "semicolon",
            # "f": "quote",
            "f": "semicolon",
            "d": "quote",
            "b": "quote",
            "n": "hyphen",
            "m": "equal_sign",
            "comma": "open_bracket",
            "period": "close_bracket",
        }
    },
    "Mercutio L Two Misc.": {
        "layer": L_TWO,
        MANIPULATORS: {
            "delete_or_backspace": "delete_forward",
            "b": "semicolon",
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


complex_modification_rules = [
    {
        "description": "Mercutio CapsLock to Hyper/Escape",
        "manipulators": [
            {
                "from": {
                    "key_code": "caps_lock",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "key_code": BASE_MODIFIER
                    }
                ],
                "to_if_alone": [
                    {
                        "key_code": "escape"
                    }
                ],
                "type": "basic"
            }
        ]
    },
]

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
