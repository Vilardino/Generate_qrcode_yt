from pytube import Playlist

urls= Playlist('https://www.youtube.com/playlist?list=PLXP-A8qzEKQO0qE-eBqqRcaDkpMVyvH4Q')

links = open('links.txt','w')

for i in urls:
    links.write(i+'\n')