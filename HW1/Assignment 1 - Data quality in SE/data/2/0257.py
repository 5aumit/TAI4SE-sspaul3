def helloWorld():
  print "We are in DEMO land!"

for i in range(10):
  helloWorld()
print listBuilder()

def listBuilder():
  b = []
  for x in range(5):
    b.append(10 * x)
  return b

print "[done, for real]"
