from pysafebrowsing import SafeBrowsing
s = SafeBrowsing('AIzaSyBDA-z43Ru8UQZG4mJyk1PPKfL5XMxNIv0')
r = s.lookup_urls(['https://pollyaninru.click/#opros_yan'])
print(r)