import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from xsdata.formats.dataclass.parsers import XmlParser
from ndov_models import Kv6Posinfo, VvTmPush

parser = XmlParser()

with open("C:/Users/David/Desktop/ov_analytics/spark/schema/tmi80-posinfo-met-schema-v813.xml", "rb") as f:
    obj = parser.from_bytes(f.read(), VvTmPush)

print(obj) 