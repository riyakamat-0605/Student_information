import sys

if len(sys.argv) != 3:
  print("Usage: python student.py <name> <roll>")
  sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
roll_no = sys.argv[2]

print("script name: ", script_name)
print("name: ", name)
print("roll no: ", roll_no)
