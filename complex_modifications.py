import json
from typing import Dict, Any


def generate_rule(from_code: str, to_code: str) -> Dict[str, Any]:
	return {
		"from": {
			"key_code": from_code,
			"modifiers": {
				"mandatory": [
					"right_command"
				],
				"optional": [
					"any"
				]
			}
		},
		"to": [
			{
				"key_code": to_code
			}
		],
		"type": "basic"
	}
    

print(generate_rule("foo", "bar"))
