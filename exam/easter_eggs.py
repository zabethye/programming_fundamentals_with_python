import re
string = input()
pattern = r"[\@|\#]{1,}[a-z]{3,}[\@|\#]{1,}\W+[\/]{1,}[\d+]+[\/+]{1,}"
matches_wo_cut = re.findall(pattern, string)
colour_pattern = r"[a-z]+"
qty_pattern = r"\d+"
for match in matches_wo_cut:
    color = "".join(re.findall(colour_pattern, match))
    qty = "".join(re.findall(qty_pattern, match))
    print(f"You found {qty} {color} eggs!")
