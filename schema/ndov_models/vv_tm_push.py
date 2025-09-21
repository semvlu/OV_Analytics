from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class Delimiter:
    class Meta:
        name = "delimiter"
        namespace = "http://bison.connekt.nl/tmi8/kv6/core"

    since: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Arrival:
    class Meta:
        name = "ARRIVAL"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    punctuality: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: list[Delimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rd_x: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-x",
            "type": "Element",
            "sequence": 1,
        },
    )
    rd_y: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-y",
            "type": "Element",
            "sequence": 1,
        },
    )


@dataclass
class Delay:
    class Meta:
        name = "DELAY"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    punctuality: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "required": True,
        },
    )


@dataclass
class Departure:
    class Meta:
        name = "DEPARTURE"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    punctuality: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: list[Delimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rd_x: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-x",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rd_y: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-y",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass
class End:
    class Meta:
        name = "END"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "required": True,
        },
    )


@dataclass
class Init:
    class Meta:
        name = "INIT"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    blockcode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    wheelchairaccessible: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    numberofcoaches: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "required": True,
        },
    )


@dataclass
class Offroute:
    class Meta:
        name = "OFFROUTE"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rd_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "rd-x",
            "type": "Element",
            "required": True,
        },
    )
    rd_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "rd-y",
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "required": True,
        },
    )


@dataclass
class Onroute:
    class Meta:
        name = "ONROUTE"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    punctuality: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    distancesincelastuserstop: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rd_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "rd-x",
            "type": "Element",
            "required": True,
        },
    )
    rd_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "rd-y",
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "required": True,
        },
    )


@dataclass
class Onstop:
    class Meta:
        name = "ONSTOP"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    dataownercode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lineplanningnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operatingday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journeynumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reinforcementnumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    userstopcode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    passagesequencenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    vehiclenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    punctuality: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    delimiter: list[Delimiter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rd_x: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-x",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rd_y: list[int] = field(
        default_factory=list,
        metadata={
            "name": "rd-y",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    uitbreiding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Kv6Posinfo:
    class Meta:
        name = "KV6posinfo"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    delay: Optional[Delay] = field(
        default=None,
        metadata={
            "name": "DELAY",
            "type": "Element",
        },
    )
    init: Optional[Init] = field(
        default=None,
        metadata={
            "name": "INIT",
            "type": "Element",
        },
    )
    departure: list[Departure] = field(
        default_factory=list,
        metadata={
            "name": "DEPARTURE",
            "type": "Element",
            "sequence": 1,
        },
    )
    arrival: list[Arrival] = field(
        default_factory=list,
        metadata={
            "name": "ARRIVAL",
            "type": "Element",
            "sequence": 1,
        },
    )
    onroute: Optional[Onroute] = field(
        default=None,
        metadata={
            "name": "ONROUTE",
            "type": "Element",
        },
    )
    offroute: Optional[Offroute] = field(
        default=None,
        metadata={
            "name": "OFFROUTE",
            "type": "Element",
        },
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "name": "END",
            "type": "Element",
        },
    )
    onstop: Optional[Onstop] = field(
        default=None,
        metadata={
            "name": "ONSTOP",
            "type": "Element",
            "required": True,
        },
    )
    delimiter: Optional[Delimiter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://bison.connekt.nl/tmi8/kv6/core",
        },
    )


@dataclass
class VvTmPush:
    class Meta:
        name = "VV_TM_PUSH"
        namespace = "http://bison.connekt.nl/tmi8/kv6/msg"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    subscriber_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "required": True,
        },
    )
    dossier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DossierName",
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "required": True,
        },
    )
    kv6posinfo: list[Kv6Posinfo] = field(
        default_factory=list,
        metadata={
            "name": "KV6posinfo",
            "type": "Element",
            "min_occurs": 1,
        },
    )
