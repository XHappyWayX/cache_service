#!/usr/bin/env python3
import argparse
import sys
import json
import requests

def main():
    parser = argparse.ArgumentParser(description="CLI test tool")
    parser.add_argument("-H", "--host", default="http://127.0.0.1:8000", help="serverURL")
    parser.add_argument("-r", "--repeat", type=int, default=1, help="Amount of repetition")
    parser.add_argument("-i", "--input", help="Input file ('-' for stdin)")
    parser.add_argument("-j", "--json", help="JSON string like input data")
    parser.add_argument("-o", "--output", help="output file ('-' for stdout)")
    args = parser.parse_args()

    payload_data = {}
    if args.json:
        try:
            payload_data = json.loads(args.json)
        except json.JSONDecodeError:
            print("error: JSON is not valid", file=sys.stderr)
            sys.exit(1)

    elif args.input:
        if args.input == "-":
            payload_data = json.load(sys.stdin)
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                payload_data = json.load(f)

    result = None
    for _ in range(args.repeat):
        response = requests.post(f"{args.host}/payload/", json=payload_data)
        if response.status_code == 200:
            result = response.json()
        else:
            result = {"error": response.text}
            break

    if args.output:
        if args.output == "-":
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
