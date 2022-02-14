import re

pattern = re.compile(r"[8924763]", re.IGNORECASE)

snumbers = 'JGDN8923487854t6fnjhasfu555335udvb'

print(pattern.sub('', snumbers))
