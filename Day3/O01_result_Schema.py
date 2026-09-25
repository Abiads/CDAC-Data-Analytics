"""
Concepts used in this example:
1. XML Architecture & Prolog: Building valid XML with <?xml version="1.0" encoding="UTF-8"?> declaration.
2. Semi-Structured Hierarchy: Distinguishing between metadata (attributes) and payload (elements/sub-elements).
3. XML Generation: Programmatically creating XML nodes using xml.etree.ElementTree (Element, SubElement, set, text).
4. XML Serialization & Formatting: Converting ElementTree to formatted XML strings with proper encoding.
5. XML Parsing & XPath Search: Querying nodes and extracting match metadata using find(), findall(), and attributes (.attrib).
6. Pandas Integration: Converting semi-structured XML match results into a structured tabular DataFrame (pd.read_xml).
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd


def print_section(title: str):
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


# -------------------------------------------------------------------------
# 1. Programmatically Build XML Schema for Match Results with Metadata
# -------------------------------------------------------------------------
print_section("1. BUILDING XML MATCH RESULTS WITH METADATA")

# Root element: <results>
root = ET.Element("results")

# Metadata section: <metadata>
metadata = ET.SubElement(root, "metadata")
source = ET.SubElement(metadata, "source")
source.text = "Sports Analytics Cloud / Colab Pipeline"

timestamp = ET.SubElement(metadata, "timestamp")
timestamp.text = "2026-09-25T10:00:00Z"

version = ET.SubElement(metadata, "schema_version")
version.text = "1.0"

# Matches container: <matches>
matches = ET.SubElement(root, "matches")

# Sample match records dataset
match_records = [
    {
        "id": "M101",
        "date": "2026-04-10",
        "venue": "Wankhede Stadium, Mumbai",
        "format": "T20",
        "team1": "Mumbai Indians",
        "team2": "Chennai Super Kings",
        "winner": "Mumbai Indians",
        "win_margin": "5 wickets",
        "player_of_match": "Rohit Sharma"
    },
    {
        "id": "M102",
        "date": "2026-04-11",
        "venue": "M. Chinnaswamy Stadium, Bengaluru",
        "format": "T20",
        "team1": "Royal Challengers Bengaluru",
        "team2": "Kolkata Knight Riders",
        "winner": "Royal Challengers Bengaluru",
        "win_margin": "18 runs",
        "player_of_match": "Virat Kohli"
    },
    {
        "id": "M103",
        "date": "2026-04-12",
        "venue": "Narendra Modi Stadium, Ahmedabad",
        "format": "T20",
        "team1": "Gujarat Titans",
        "team2": "Delhi Capitals",
        "winner": "Gujarat Titans",
        "win_margin": "6 wickets",
        "player_of_match": "Shubman Gill"
    }
]

# Populate match elements
for item in match_records:
    # Match node with metadata attributes
    match_elem = ET.SubElement(matches, "match", attrib={
        "id": item["id"],
        "date": item["date"],
        "format": item["format"]
    })
    
    venue = ET.SubElement(match_elem, "venue")
    venue.text = item["venue"]
    
    teams = ET.SubElement(match_elem, "teams")
    t1 = ET.SubElement(teams, "team1")
    t1.text = item["team1"]
    t2 = ET.SubElement(teams, "team2")
    t2.text = item["team2"]
    
    result = ET.SubElement(match_elem, "result")
    winner = ET.SubElement(result, "winner")
    winner.text = item["winner"]
    margin = ET.SubElement(result, "margin")
    margin.text = item["win_margin"]
    pom = ET.SubElement(result, "player_of_match")
    pom.text = item["player_of_match"]


# -------------------------------------------------------------------------
# 2. Serialize XML with Prolog (<?xml version="1.0" encoding="UTF-8"?>)
# -------------------------------------------------------------------------
print_section("2. SERIALIZED XML OUTPUT (WITH PROLOG & PRETTY-PRINT)")

# Convert to raw byte string
raw_xml_bytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)

# Pretty print using minidom for visual inspection
parsed_dom = minidom.parseString(raw_xml_bytes)
pretty_xml = parsed_dom.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8")
print(pretty_xml)

import os

# Save to local XML file in the current script folder
script_dir = os.path.dirname(os.path.abspath(__file__))
xml_filename = os.path.join(script_dir, "match_results.xml")
with open(xml_filename, "w", encoding="utf-8") as f:
    f.write(pretty_xml)
print(f"Saved XML schema and data to '{xml_filename}'.")


# -------------------------------------------------------------------------
# 3. Parse XML & Extract Metadata via XPath
# -------------------------------------------------------------------------
print_section("3. PARSING XML & QUERYING METADATA VIA XPATH")

tree = ET.parse(xml_filename)
tree_root = tree.getroot()

# Extract global metadata
meta_source = tree_root.find("./metadata/source").text
meta_timestamp = tree_root.find("./metadata/timestamp").text
print(f"Dataset Metadata Source    : {meta_source}")
print(f"Dataset Metadata Timestamp : {meta_timestamp}")
print("-" * 65)

# Query match records
print("Extracted Match Results:")
for m in tree_root.findall("./matches/match"):
    m_id = m.attrib.get("id")
    m_date = m.attrib.get("date")
    winner = m.find("./result/winner").text
    margin = m.find("./result/margin").text
    print(f"  • Match [{m_id}] ({m_date}): Winner -> {winner} ({margin})")


# -------------------------------------------------------------------------
# 4. Ingest XML into Tabular Pandas DataFrame
# -------------------------------------------------------------------------
print_section("4. TABULAR INGESTION VIA PANDAS (pd.read_xml)")

# Flatten XML directly into a DataFrame
df_matches = pd.read_xml(
    xml_filename, 
    xpath="./matches/match"
)
print("DataFrame from XML (Flattened match records):")
print(df_matches[["id", "date", "format", "venue"]])

# Flatten detailed match results
df_results = pd.read_xml(
    xml_filename,
    xpath="./matches/match/result"
)
print("\nDataFrame from XML (Detailed result records):")
print(df_results)
print("-" * 65)