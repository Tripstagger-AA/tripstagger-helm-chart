import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("app")
parser.add_argument("version")
args = parser.parse_args()

with open("tripstagger/values.yaml") as istream:
    ymldoc = yaml.safe_load(istream)
    ymldoc[args.app] = args.version

print(ymldoc)

with open("tripstagger/values.yaml", "w") as ostream:
    yaml.dump(ymldoc, ostream, default_flow_style=False, sort_keys=False)