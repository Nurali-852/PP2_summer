import json

with open("Practice4\json_parsing\sample.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 90)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")