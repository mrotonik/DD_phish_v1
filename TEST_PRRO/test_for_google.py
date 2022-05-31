from pysafebrowsing import SafeBrowsing
s = SafeBrowsing(KEY)
r = s.lookup_urls(['http://malware.testing.google.test/testing/malware/'])
print(r)